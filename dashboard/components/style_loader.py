import streamlit as st
from pathlib import Path


def load_css():

    css_path = (
        Path(__file__)
        .resolve()
        .parent.parent
        / "assets"
        / "style.css"
    )


    if css_path.exists():

        with open(
            css_path,
            "r",
            encoding="utf-8"
        ) as f:

            css = f.read()


        st.markdown(
            f"""
            <style>
            {css}
            </style>
            """,
            unsafe_allow_html=True
        )

    else:

        st.error(
            "فایل style.css پیدا نشد"
        )