import streamlit as st
import numpy as np
import pandas as pd

from sklearn.ensemble import RandomForestRegressor

from services.forecasting_service import (
    prepare_monthly_sales
)


# =========================================================
# FEATURE COLUMNS
# =========================================================

FEATURE_COLUMNS = [
    "month_index",
    "month",
    "month_sin",
    "month_cos",
    "lag_1",
    "lag_2",
    "lag_3",
    "lag_6",
    "lag_12",
    "rolling_mean_3",
    "rolling_mean_6",
    "rolling_mean_12",
]


# =========================================================
# FEATURE ENGINEERING
# =========================================================

def create_features(df):

    data = df.copy()

    data["sale_date"] = pd.to_datetime(
        data["sale_date"]
    )

    data = (
        data
        .sort_values("sale_date")
        .reset_index(drop=True)
    )

    # -----------------------------------------------------
    # Time Features
    # -----------------------------------------------------

    data["month"] = (
        data["sale_date"].dt.month
    )

    data["year"] = (
        data["sale_date"].dt.year
    )

    data["month_index"] = np.arange(
        len(data)
    )

    # -----------------------------------------------------
    # Seasonal Features
    # -----------------------------------------------------

    data["month_sin"] = np.sin(
        2 * np.pi * data["month"] / 12
    )

    data["month_cos"] = np.cos(
        2 * np.pi * data["month"] / 12
    )

    # -----------------------------------------------------
    # Lag Features
    # -----------------------------------------------------

    data["lag_1"] = data["revenue"].shift(1)
    data["lag_2"] = data["revenue"].shift(2)
    data["lag_3"] = data["revenue"].shift(3)
    data["lag_6"] = data["revenue"].shift(6)
    data["lag_12"] = data["revenue"].shift(12)

    # -----------------------------------------------------
    # Rolling Features
    # -----------------------------------------------------

    shifted_revenue = (
        data["revenue"].shift(1)
    )

    data["rolling_mean_3"] = (
        shifted_revenue
        .rolling(3)
        .mean()
    )

    data["rolling_mean_6"] = (
        shifted_revenue
        .rolling(6)
        .mean()
    )

    data["rolling_mean_12"] = (
        shifted_revenue
        .rolling(12)
        .mean()
    )

    # -----------------------------------------------------
    # Remove rows without enough history
    # -----------------------------------------------------

    data = (
        data
        .dropna()
        .reset_index(drop=True)
    )

    return data


# =========================================================
# MODEL
# =========================================================

def create_model():

    return RandomForestRegressor(
        n_estimators=500,
        max_depth=6,
        min_samples_leaf=2,
        max_features="sqrt",
        random_state=42,
        n_jobs=-1
    )


# =========================================================
# TRAIN MODEL
# =========================================================

@st.cache_resource
def train_sales_forecast():

    df = prepare_monthly_sales()

    features = create_features(df)

    X = features[
        FEATURE_COLUMNS
    ]

    y = features[
        "revenue"
    ]

    model = create_model()

    model.fit(
        X,
        y
    )

    return model, df


# =========================================================
# FUTURE FORECAST
# =========================================================

@st.cache_data
def predict_future_sales(months=6):

    if months < 1:
        raise ValueError(
            "months must be greater than 0"
        )

    model, df = train_sales_forecast()

    history = df.copy()

    history["sale_date"] = pd.to_datetime(
        history["sale_date"]
    )

    history = (
        history
        .sort_values("sale_date")
        .reset_index(drop=True)
    )

    predictions = []

    last_date = (
        history["sale_date"].iloc[-1]
    )

    last_month_index = (
        len(history) - 1
    )

    # =====================================================
    # RECURSIVE FORECASTING
    # =====================================================

    for step in range(1, months + 1):

        future_date = (
            last_date
            + pd.DateOffset(months=1)
        )

        month = future_date.month

        month_index = (
            last_month_index + step
        )

        # -------------------------------------------------
        # Build Future Features
        # -------------------------------------------------

        row = pd.DataFrame(
            [{
                "month_index": month_index,

                "month": month,

                "month_sin": np.sin(
                    2 * np.pi * month / 12
                ),

                "month_cos": np.cos(
                    2 * np.pi * month / 12
                ),

                "lag_1":
                    history["revenue"].iloc[-1],

                "lag_2":
                    history["revenue"].iloc[-2],

                "lag_3":
                    history["revenue"].iloc[-3],

                "lag_6":
                    history["revenue"].iloc[-6],

                "lag_12":
                    history["revenue"].iloc[-12],

                "rolling_mean_3":
                    history["revenue"]
                    .iloc[-3:]
                    .mean(),

                "rolling_mean_6":
                    history["revenue"]
                    .iloc[-6:]
                    .mean(),

                "rolling_mean_12":
                    history["revenue"]
                    .iloc[-12:]
                    .mean(),
            }]
        )

        X_future = row[
            FEATURE_COLUMNS
        ]

        # -------------------------------------------------
        # Main Prediction
        # -------------------------------------------------

        prediction = model.predict(
            X_future
        )[0]

        prediction = max(
            0,
            float(prediction)
        )

        # -------------------------------------------------
        # Prediction Interval
        # -------------------------------------------------

        tree_predictions = np.array(
            [
                estimator.predict(
                    X_future.to_numpy()
                )[0]
                for estimator in model.estimators_
            ]
        )

        lower_bound = max(
            0,
            float(
                np.percentile(
                    tree_predictions,
                    10
                )
            )
        )

        upper_bound = max(
            prediction,
            float(
                np.percentile(
                    tree_predictions,
                    90
                )
            )
        )

        # -------------------------------------------------
        # Save Prediction
        # -------------------------------------------------

        predictions.append(
            {
                "sale_date":
                    future_date,

                "predicted_revenue":
                    prediction,

                "lower_bound":
                    lower_bound,

                "upper_bound":
                    upper_bound,
            }
        )

        # -------------------------------------------------
        # Recursive Update
        # -------------------------------------------------

        history.loc[len(history)] = {
            "sale_date": future_date,
            "revenue": prediction
        }

        last_date = future_date

    # =====================================================
    # FINAL RESULT
    # =====================================================

    result = pd.DataFrame(
        predictions
    )

    result["sale_date"] = pd.to_datetime(
        result["sale_date"]
    )

    return result