import streamlit as st
import numpy as np
import pandas as pd

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
)

from services.forecasting_service import prepare_monthly_sales
from services.forecast_model import (
    create_model,
    create_features,
    FEATURE_COLUMNS,
)


# ============================================================
# BUILD FORECAST FEATURES
# ============================================================

def build_forecast_features(history, future_date):
    """
    Build one feature row for recursive forecasting.

    Keeps the exact feature structure used by the
    production forecast model.
    """

    future_date = pd.Timestamp(future_date)

    month = future_date.month
    month_index = len(history)

    revenue = history["revenue"].to_numpy(dtype=float)

    row = pd.DataFrame(
        {
            "month_index": [month_index],
            "month": [month],

            "month_sin": [
                np.sin(2 * np.pi * month / 12)
            ],

            "month_cos": [
                np.cos(2 * np.pi * month / 12)
            ],

            "lag_1": [revenue[-1]],
            "lag_2": [revenue[-2]],
            "lag_3": [revenue[-3]],
            "lag_6": [revenue[-6]],
            "lag_12": [revenue[-12]],

            "rolling_mean_3": [
                revenue[-3:].mean()
            ],

            "rolling_mean_6": [
                revenue[-6:].mean()
            ],

            "rolling_mean_12": [
                revenue[-12:].mean()
            ],
        }
    )

    return row[FEATURE_COLUMNS]


# ============================================================
# WALK-FORWARD FORECAST
# ============================================================

def walk_forward_forecast(
    df,
    train_months,
    forecast_horizon=3,
):
    """
    Perform recursive walk-forward forecasting.

    The model is trained only on historical data available
    before the validation window.
    """

    train_df = (
        df.iloc[:train_months]
        .copy()
        .reset_index(drop=True)
    )

    test_df = (
        df.iloc[
            train_months:
            train_months + forecast_horizon
        ]
        .copy()
        .reset_index(drop=True)
    )

    if len(test_df) < forecast_horizon:
        return None

    # --------------------------------------------------------
    # Training features
    # --------------------------------------------------------

    train_features = create_features(train_df)

    X_train = train_features[FEATURE_COLUMNS]
    y_train = train_features["revenue"]

    # --------------------------------------------------------
    # Train model
    # --------------------------------------------------------

    model = create_model()

    model.fit(
        X_train,
        y_train,
    )

    # --------------------------------------------------------
    # Recursive forecast
    # --------------------------------------------------------

    history = train_df[
        ["sale_date", "revenue"]
    ].copy()

    predictions = np.empty(
        forecast_horizon,
        dtype=float,
    )

    for step in range(forecast_horizon):

        future_date = pd.Timestamp(
            test_df.loc[step, "sale_date"]
        )

        X_future = build_forecast_features(
            history,
            future_date,
        )

        prediction = float(
            model.predict(X_future)[0]
        )

        prediction = max(
            0.0,
            prediction,
        )

        predictions[step] = prediction

        # ----------------------------------------------------
        # Recursive update
        # ----------------------------------------------------

        history.loc[len(history)] = [
            future_date,
            prediction,
        ]

    actual = test_df[
        "revenue"
    ].to_numpy(dtype=float)

    return actual, predictions


# ============================================================
# FORECAST EVALUATION
# ============================================================

@st.cache_data
def evaluate_forecast_model():
    """
    Evaluate the forecasting model using walk-forward
    validation.

    Returns:
        MAE
        RMSE
        MAPE
        Validation method
        Forecast horizon
        Validation rounds
    """

    # ========================================================
    # LOAD DATA
    # ========================================================

    df = prepare_monthly_sales()

    df["sale_date"] = pd.to_datetime(
        df["sale_date"]
    )

    df = (
        df[
            ["sale_date", "revenue"]
        ]
        .sort_values("sale_date")
        .reset_index(drop=True)
    )

    # ========================================================
    # VALIDATION SETTINGS
    # ========================================================

    forecast_horizon = 3
    minimum_train_months = 18

    max_train_months = (
        len(df) - forecast_horizon
    )

    # ========================================================
    # WALK-FORWARD VALIDATION
    # ========================================================

    actual_values = []
    predicted_values = []

    validation_rounds = 0

    for train_months in range(
        minimum_train_months,
        max_train_months + 1,
        forecast_horizon,
    ):

        result = walk_forward_forecast(
            df=df,
            train_months=train_months,
            forecast_horizon=forecast_horizon,
        )

        if result is None:
            continue

        actual, predicted = result

        actual_values.append(actual)
        predicted_values.append(predicted)

        validation_rounds += 1

    # ========================================================
    # SAFETY CHECK
    # ========================================================

    if validation_rounds == 0:
        raise ValueError(
            "Not enough historical data "
            "for walk-forward validation."
        )

    # ========================================================
    # COMBINE RESULTS
    # ========================================================

    actual = np.concatenate(
        actual_values
    )

    predicted = np.concatenate(
        predicted_values
    )

    # ========================================================
    # MAE
    # ========================================================

    mae = mean_absolute_error(
        actual,
        predicted,
    )

    # ========================================================
    # RMSE
    # ========================================================

    rmse = np.sqrt(
        mean_squared_error(
            actual,
            predicted,
        )
    )

    # ========================================================
    # MAPE
    # ========================================================

    non_zero = actual != 0

    if np.any(non_zero):

        mape = (
            np.mean(
                np.abs(
                    (
                        actual[non_zero]
                        - predicted[non_zero]
                    )
                    / actual[non_zero]
                )
            )
            * 100
        )

    else:
        mape = np.nan

    # ========================================================
    # RESULT
    # ========================================================

    return {
        "MAE": round(
            float(mae),
            2,
        ),

        "RMSE": round(
            float(rmse),
            2,
        ),

        "MAPE": round(
            float(mape),
            2,
        ),

        "Validation_Method":
            "Walk-Forward Validation",

        "Forecast_Horizon":
            forecast_horizon,

        "Validation_Rounds":
            validation_rounds,
    }