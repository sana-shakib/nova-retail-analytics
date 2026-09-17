import streamlit as st


def dashboard_header(title, subtitle):

    st.title(title)

    st.caption(
        subtitle
    )

    st.divider()