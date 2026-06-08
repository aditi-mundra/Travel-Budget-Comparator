import pandas as pd

def filter_by_budget(df: pd.DataFrame, min_budget: float, max_budget: float) -> pd.DataFrame:
    """Filters data based on a precise bounded financial scope."""
    return df[(df['Total Cost'] >= min_budget) & (df['Total Cost'] <= max_budget)]

def filter_by_season(df: pd.DataFrame, season_name: str) -> pd.DataFrame:
    """Filters data based on categorical holiday seasons."""
    sanitized_season = season_name.strip().capitalize()
    return df[df['Season'] == sanitized_season]