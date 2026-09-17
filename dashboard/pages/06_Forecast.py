# -*- coding: utf-8 -*-

import streamlit as st
import plotly.graph_objects as go
import pandas as pd

from services.forecasting_service import prepare_monthly_sales
from services.forecast_model import predict_future_sales
from services.forecast_evaluation import evaluate_forecast_model


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Nova | Revenue Forecast",
    page_icon="N",
    layout="wide"
)


# ============================================================
# PAGE TITLE
# ============================================================

st.title("پیش‌بینی درآمد")

st.caption("NOVA RETAIL GROUP | Revenue Forecasting")


# ============================================================
# INTRODUCTION
# ============================================================

st.subheader("پیش‌بینی عملکرد فروش")

st.write(
    "این بخش با استفاده از داده‌های تاریخی فروش، "
    "ویژگی‌های زمانی، الگوهای فصلی، Lag Features "
    "و میانگین‌های متحرک، درآمد ماه‌های آینده را "
    "با استفاده از مدل Random Forest پیش‌بینی می‌کند."
)


# ============================================================
# MODEL INFORMATION
# ============================================================

info1, info2, info3, info4 = st.columns(4)

with info1:
    st.metric(
        "مدل",
        "Random Forest"
    )

with info2:
    st.metric(
        "نوع پیش‌بینی",
        "Recursive Forecast"
    )

with info3:
    st.metric(
        "افق پیش‌فرض",
        "6 Months"
    )

with info4:
    st.metric(
        "دوره داده",
        "2022 — 2025"
    )


st.divider()


# ============================================================
# HISTORICAL DATA
# ============================================================

history = prepare_monthly_sales()

history["sale_date"] = pd.to_datetime(
    history["sale_date"]
)

history = (
    history
    .sort_values("sale_date")
    .reset_index(drop=True)
)


# ============================================================
# FORECAST HORIZON
# ============================================================

st.subheader("افق پیش‌بینی")

st.caption("Forecast Horizon")

months = st.slider(
    "تعداد ماه‌های آینده",
    min_value=3,
    max_value=12,
    value=6,
    step=1
)


st.write(
    f"افق انتخاب‌شده: **{months} ماه**"
)


# ============================================================
# FORECAST
# ============================================================

forecast = predict_future_sales(months)

forecast["sale_date"] = pd.to_datetime(
    forecast["sale_date"]
)


# ============================================================
# MODEL EVALUATION
# ============================================================

evaluation = evaluate_forecast_model()


# ============================================================
# FORECAST KPIs
# ============================================================

last_actual = float(
    history["revenue"].iloc[-1]
)

next_prediction = float(
    forecast["predicted_revenue"].iloc[0]
)

average_forecast = float(
    forecast["predicted_revenue"].mean()
)


st.subheader("شاخص‌های پیش‌بینی")

st.caption("Forecast Performance")


k1, k2, k3, k4 = st.columns(4)

with k1:
    st.metric(
        "Last Actual Revenue",
        f"{last_actual:,.0f}"
    )

with k2:
    st.metric(
        "Next Month Forecast",
        f"{next_prediction:,.0f}"
    )

with k3:
    st.metric(
        "Forecast MAPE",
        f"{evaluation['MAPE']:.2f}%"
    )

with k4:
    st.metric(
        "Average Forecast",
        f"{average_forecast:,.0f}"
    )


st.divider()


# ============================================================
# MODEL EVALUATION
# ============================================================

st.subheader("ارزیابی مدل")

st.caption("Model Evaluation")


e1, e2, e3 = st.columns(3)

with e1:
    st.metric(
        "Model",
        "Random Forest"
    )

with e2:
    st.metric(
        "MAE",
        f"{evaluation['MAE']:,.0f}"
    )

with e3:
    st.metric(
        "RMSE",
        f"{evaluation['RMSE']:,.0f}"
    )


st.caption(
    "Evaluation is based on a six-month historical holdout "
    "using recursive forecasting."
)


st.divider()


# ============================================================
# ACTUAL VS FORECAST
# ============================================================

st.subheader("درآمد واقعی و پیش‌بینی‌شده")

st.caption("Actual vs Forecast Revenue")


fig = go.Figure()


fig.add_trace(
    go.Scatter(
        x=history["sale_date"],
        y=history["revenue"],
        mode="lines+markers",
        name="Actual Revenue"
    )
)


fig.add_trace(
    go.Scatter(
        x=forecast["sale_date"],
        y=forecast["predicted_revenue"],
        mode="lines+markers",
        name="Forecast Revenue",
        line=dict(dash="dash")
    )
)


fig.add_trace(
    go.Scatter(
        x=pd.concat(
            [
                forecast["sale_date"],
                forecast["sale_date"].iloc[::-1]
            ]
        ),
        y=pd.concat(
            [
                forecast["upper_bound"],
                forecast["lower_bound"].iloc[::-1]
            ]
        ),
        fill="toself",
        fillcolor="rgba(100,100,100,0.15)",
        line=dict(
            color="rgba(255,255,255,0)"
        ),
        hoverinfo="skip",
        name="Prediction Interval"
    )
)


fig.update_layout(
    title="Actual vs Forecast Revenue",
    xaxis_title="Date",
    yaxis_title="Revenue",
    hovermode="x unified",
    height=550
)


st.plotly_chart(
    fig,
    use_container_width=True
)


st.divider()


# ============================================================
# FORECAST DETAILS
# ============================================================

st.subheader("جزئیات پیش‌بینی")

st.caption("Forecast Details")


display_forecast = forecast.copy()

display_forecast["sale_date"] = (
    display_forecast["sale_date"]
    .dt.strftime("%Y-%m")
)

display_forecast["predicted_revenue"] = (
    display_forecast["predicted_revenue"]
    .round(0)
)

display_forecast["lower_bound"] = (
    display_forecast["lower_bound"]
    .round(0)
)

display_forecast["upper_bound"] = (
    display_forecast["upper_bound"]
    .round(0)
)


display_forecast = display_forecast.rename(
    columns={
        "sale_date": "Month",
        "predicted_revenue": "Predicted Revenue",
        "lower_bound": "Lower Bound",
        "upper_bound": "Upper Bound"
    }
)


st.dataframe(
    display_forecast,
    hide_index=True,
    use_container_width=True
)


st.divider()


# ============================================================
# INTERPRETATION
# ============================================================

st.subheader("تفسیر پیش‌بینی")

st.caption("Forecast Interpretation")


forecast_growth = (
    (
        forecast["predicted_revenue"].iloc[-1]
        - last_actual
    )
    / last_actual
) * 100


if forecast_growth >= 0:

    st.success(
        f"درآمد پیش‌بینی‌شده در پایان افق "
        f"{months} ماهه حدود {forecast_growth:.2f}% "
        f"بیشتر از آخرین درآمد واقعی برآورد شده است."
    )

else:

    st.warning(
        f"درآمد پیش‌بینی‌شده در پایان افق "
        f"{months} ماهه حدود {abs(forecast_growth):.2f}% "
        f"کمتر از آخرین درآمد واقعی برآورد شده است."
    )