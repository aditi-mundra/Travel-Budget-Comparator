import os
import matplotlib.pyplot as plt
import pandas as pd

# Set clean globally recognized visualization styling blueprints
plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

def save_or_show(filename: str):
    """Utility wrapper to automatically manage and export plot files smoothly."""
    os.makedirs("outputs", exist_ok=True)
    out_path = os.path.join("outputs", filename)
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    plt.close()

def generate_bar_comparison(place1: pd.Series, place2: pd.Series, cost_columns: list):
    x = range(len(cost_columns))
    plt.figure(figsize=(10, 6))
    plt.bar([i - 0.2 for i in x], [place1[col] for col in cost_columns], width=0.4, label=place1['Destination'], color='#008080')
    plt.bar([i + 0.2 for i in x], [place2[col] for col in cost_columns], width=0.4, label=place2['Destination'], color='#FF7F50')
    plt.xticks(x, [c.split(' ')[0] for c in cost_columns], rotation=15)
    plt.ylabel("Cost (₹)")
    plt.title(f"Expenditure Blueprint Vector: {place1['Destination']} vs {place2['Destination']}")
    plt.legend()
    save_or_show("destination_comparison_bar.png")

def generate_pie_distribution(place1: pd.Series, place2: pd.Series, cost_columns: list):
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    colors = ['#4F81BD', '#C0504D', '#9BBB59', '#8064A2', '#4BACC6']
    
    axes[0].pie([place1[c] for c in cost_columns], labels=[c.split(' ')[0] for c in cost_columns], autopct='%1.1f%%', colors=colors, startangle=140)
    axes[0].set_title(place1['Destination'], fontsize=12, fontweight='bold')
    
    axes[1].pie([place2[c] for c in cost_columns], labels=[c.split(' ')[0] for c in cost_columns], autopct='%1.1f%%', colors=colors, startangle=140)
    axes[1].set_title(place2['Destination'], fontsize=12, fontweight='bold')
    
    plt.suptitle("Comparative Allocation Vectors", fontsize=14, fontweight='bold')
    save_or_show("destination_distribution_pies.png")

def generate_seasonal_metrics(df: pd.DataFrame):
    plt.figure(figsize=(8, 5))
    df.groupby('Season')['Total Cost'].mean().plot(kind='bar', color='#5DADE2', edgecolor='black', alpha=0.8)
    plt.title('Macroeconomics: Average Budget Requirements Per Season')
    plt.ylabel('Mean Expense (₹)')
    plt.xticks(rotation=0)
    save_or_show("seasonal_averages.png")