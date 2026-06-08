import os
from src.data_loader import load_and_prepare_data
from src.analytics import filter_by_budget, filter_by_season

def main():
    data_path = os.path.join("data", "travel_budget_dataset.csv")
    df, _ = load_and_prepare_data(data_path)
    
    print("\n--- Travel Cost Intelligence Framework CLI ---")
    while True:
        cmd = input("\nEnter routing task ['budget', 'season', 'exit']: ").strip().lower()
        if cmd == 'exit':
            break
        elif cmd == 'budget':
            mn = float(input("Min Budget (INR): "))
            mx = float(input("Max Budget (INR): "))
            res = filter_by_budget(df, mn, mx)
            print(res[['Destination', 'Total Cost']].head(10))
        elif cmd == 'season':
            sn = input("Enter Season: ")
            res = filter_by_season(df, sn)
            print(res[['Destination', 'Total Cost']].head(10))

if __name__ == "__main__":
    main()