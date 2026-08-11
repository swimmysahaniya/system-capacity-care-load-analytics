"""
Data Preprocessing Module

Author: Swimmy Sahaniya

Description:
This module is responsible for cleaning and validating
the raw HHS Unaccompanied Children dataset.
"""
import pandas as pd

import json

from pathlib import Path

from config.constants import *

from config.settings import *


class DataPreprocessor:
    def __init__(self):
        self.df = None
        self.report = {}

        self.expected_columns = [
            DATE,
            APPREHENDED,
            CBP_CUSTODY,
            TRANSFERRED,
            HHS_CARE,
            DISCHARGED,
        ]

    def load_data(self):
        self.df = pd.read_csv(RAW_DATA)

        print(f"Dataset Loaded Successfully")

        print(self.df.shape)

    def validate_columns(self):
        rows, cols = self.df.shape

        print(f"Rows    : {rows}")
        print(f"Columns : {cols}")


if __name__ == "__main__":
    preprocessor = DataPreprocessor()

    preprocessor.load_data()