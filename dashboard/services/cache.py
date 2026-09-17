import streamlit as st


@st.cache_data(
    ttl=3600,
    show_spinner=False
)
def load_cached_data(loader_function, file_path):

    """
    Load and cache data.

    ttl:
    مدت زمان نگهداری داده در حافظه
    """

    data = loader_function(
        file_path
    )

    return data