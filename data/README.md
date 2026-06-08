# Data Directory & Synthetic Generation Matrix

This directory is designated for the storage of the core tracking ledger used by the pipeline.

## 📊 Current State: Archived / Synthetic Mode

Because the original, historical `travel_budget_dataset.csv` is archived, this repository utilizes an **autonomous structural data emulation engine** located in `src/data_loader.py`. 

### How it works:
1. **Zero-Configuration Run:** If you execute `main.py` or `interactive_cli.py` without a dataset present, the pipeline will detect its absence.
2. **Deterministic Emulation:** The system will automatically construct a realistic, statistically bound mock dataset covering 150+ operational travel vectors (Transport, Accommodation, Food, Activities, and Misc costs) partitioned across seasonal and regional factors.
3. **Local Caching:** The generated file is saved right here as `travel_budget_dataset.csv` so subsequent runs operate instantly.

*Note: In production data engineering environments, large or transactional data ledgers are excluded from version control via `.gitignore` to keep the codebase lightweight and maintainable.*