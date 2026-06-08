import os
import logging
from src.data_loader import load_and_prepare_data
from src.analytics import filter_by_budget, filter_by_season
from src.visualizer import generate_bar_comparison, generate_pie_distribution, generate_seasonal_metrics

def run_automated_pipeline():
    logging.info("Starting Automated Travel Intelligence Pipeline Execution...")
    data_path = os.path.join("data", "travel_budget_dataset.csv")
    df, cost_columns = load_and_prepare_data(data_path)
    
    if df is None or df.empty:
        logging.error("Pipeline failure: Empty data matrix.")
        return

    # 1. Export standard macro metrics
    generate_seasonal_metrics(df)
    
    # 2. Extract specific entities for demo-ing comparison visualizations
    unique_places = df['Destination'].unique()
    if len(unique_places) >= 2:
        p1 = df[df['Destination'] == unique_places[0]].iloc[0]
        p2 = df[df['Destination'] == unique_places[1]].iloc[0]
        generate_bar_comparison(p1, p2, cost_columns)
        generate_pie_distribution(p1, p2, cost_columns)
        
    logging.info("Success! All graphical asset reports generated inside 'outputs/' folder.")

if __name__ == "__main__":
    run_automated_pipeline()