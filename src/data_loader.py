import os
import pandas as pd
import numpy as np
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def generate_synthetic_travel_data(num_samples: int = 150) -> pd.DataFrame:
    """Generates a highly realistic travel cost dataset if the original CSV is missing."""
    logging.info("Original dataset missing. Initializing synthetic travel data engine...")
    np.random.seed(42)
    
    destinations = [
        'Manali', 'Goa', 'Kerala Backwaters', 'Leh Ladakh', 'Jaipur', 
        'Udaipur', 'Andaman Islands', 'Ooty', 'Munnar', 'Darjeeling',
        'Shimla', 'Rishikesh', 'Varanasi', 'Hampi', 'Pondicherry'
    ]
    
    repeated_destinations = np.random.choice(destinations, num_samples)
    seasons = np.random.choice(['Spring', 'Summer', 'Autumn', 'Monsoon', 'Winter'], num_samples)
    
    # Simulate costs in INR (Indian Rupees)
    transport = np.random.randint(2000, 15000, num_samples)
    accommodation = np.random.randint(3000, 25000, num_samples)
    food = np.random.randint(1500, 10000, num_samples)
    activities = np.random.randint(1000, 12000, num_samples)
    misc = np.random.randint(500, 5000, num_samples)
    
    df = pd.DataFrame({
        'Destination': repeated_destinations,
        'Season': seasons,
        'Transport (INR)': transport,
        'Accommodation (INR)': accommodation,
        'Food (INR)': food,
        'Activities (INR)': activities,
        'Misc (INR)': misc
    })
    return df

def load_and_prepare_data(filepath: str) -> tuple:
    """Loads dataset, sanitizes cost data types, and computes the complete expenditure metric."""
    cost_columns = ['Transport (INR)', 'Accommodation (INR)', 'Food (INR)', 'Activities (INR)', 'Misc (INR)']
    
    if os.path.exists(filepath):
        logging.info(f"Target dataset found at {filepath}. Stream-loading data...")
        df = pd.read_csv(filepath)
    else:
        logging.warning(f"File not found at {filepath}. Activating synthetic generator framework.")
        df = generate_synthetic_travel_data()
        # Save a local cache
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        df.to_csv(filepath, index=False)
        
    try:
        for col in cost_columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        df['Season'] = df['Season'].str.strip().str.capitalize()
        df.fillna(0, inplace=True)
        df['Total Cost'] = df[cost_columns].sum(axis=1)
        
        # Eliminate rows where no transactions exist
        df = df[df['Total Cost'] > 0]
        return df, cost_columns
    except Exception as e:
        logging.error(f"Critical error during pipeline parsing: {e}")
        return None, []