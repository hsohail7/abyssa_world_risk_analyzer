import pandas as pd
from pathlib import Path

DATA_DIR = (Path(__file__).resolve().parent.parent / "data").resolve()


def load_cells() -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / "cells.csv")


def load_currents() -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / "currents.csv")


def load_hazards() -> pd.DataFrame:
    return pd.read_csv(DATA_DIR / "hazards.csv")
