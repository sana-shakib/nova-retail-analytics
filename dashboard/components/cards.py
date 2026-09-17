import streamlit as st


def metric_card(title, value, description=""):

    st.markdown(
        f"""
        <div class="metric-card">

            <div class="metric-title">
                {title}
            </div>

            <div class="metric-value">
                {value}
            </div>

            <div style="
                color:#6B7280;
                font-size:13px;
                margin-top:8px;
            ">
                {description}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )