# Travel Budget Matrix & Cost Comparator

An analytical algorithmic toolkit and modular data visualization framework designed to model, slice, and cross-examine regional itineraries based on financial resource constraints and seasonal variance vectors.

## 📖 The Project 

I made this project in my first year of college as a part of my academics. This engine was born out of a classic problem everyone runs into: **planning an holiday trip without breaking the bank.** 
I wrote this application to systematically parse unstructured vacation data and eliminate the guesswork. By breaking financial data down into fundamental operational vectors (Transport, Accommodation, Food, Activities, and Miscellaneous costs), the system allows users to execute isolated cost-benefit matrices across arbitrary travel destinations.

## 🚀 Key Framework Capacities

- **Modular Cost Parsing Vector Engine:** Converts multi-tier ledger matrices directly into aggregate cost columns using functional vector operations in `pandas`.
- **Synthetic Fallback Generator Engine:** Includes a dynamic mock dataset structural generator that kicks in seamlessly if the archived historical dataset path isn't present, preventing catastrophic script crashes.
- **Bi-Variant Distribution Layout Charts:** Renders structured comparative allocation distribution engines (Bar charts and paired fractional Pie configurations) exported directly to a high-resolution file system.

## 📁 Repository Structure

```text
├── data/               # Local cache data path
├── src/                # Functional source codebase modules
│   ├── data_loader.py  # Cleansing & synthetic seed operations
│   ├── analytics.py    # Segmented budget query engines
│   └── visualizer.py   # Graphics rendering module
├── outputs/            # Rendered high-res PNG visual matrices
├── main.py             # Automatic batch execution pipeline
└── interactive_cli.py  # User-facing terminal loop program