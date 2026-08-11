from pathlib import Path

import joblib
import pandas as pd
import streamlit as st


BASE_DIR = Path(__file__).resolve().parent.parent


@st.cache_data
def load_dataset():
    return pd.read_csv(
        BASE_DIR / "data" / "feature_engineered" / "feature_engineered_data.csv"
    )


@st.cache_data
def load_feature_importance():
    return pd.read_csv(
        BASE_DIR / "reports" / "feature_importance.csv"
    )


@st.cache_resource
def load_model():
    return joblib.load(
        BASE_DIR / "models" / "final_random_forest.pkl"
    )