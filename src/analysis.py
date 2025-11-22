import pandas as pd
from load_data import load_cells, load_currents, load_hazards

def _normalize(series: pd.Series):
    s = series.astype(float)
    min_v = s.min()
    max_v = s.max()
    if pd.isna(min_v) or pd.isna(max_v) or max_v == min_v:
        return pd.Series(0.0, index=s.index)
    return (s - min_v) / (max_v - min_v)


def prepare_dataframe():

    cells = load_cells()
    currents = load_currents()
    hazards = load_hazards()

    df = cells.merge(currents, on=["row", "col"], how="left")
    df = df.merge(hazards, on=["row", "col"], how="left")

    df = compute_risk_score(df)

    return df

def compute_risk_score(df: pd.DataFrame):

    hazard_risk = (df.get("severity", 0) / 5.0).clip(0, 1)

    stability_map = {"high": 0.1, "medium": 0.4, "low": 0.8}
    stability_risk = df["stability"].map(stability_map)

    speed_norm = _normalize(df["speed_mps"])

    depth_norm = _normalize(df["depth_m"])

    df["risk_score"] = (
        0.4 * hazard_risk +
        0.3 * stability_risk +
        0.2 * depth_norm +
        0.1 * speed_norm
    ).clip(0, 1)

    return df


def get_safest_cells(df: pd.DataFrame):
    return df.sort_values(by="risk_score", ascending=True).head(15)


def get_riskiest_cells(df: pd.DataFrame):
    return df.sort_values(by="risk_score", ascending=False).head(15)
