import os

def fetch_kaggle_data(kaggle_url, run_id):
    # Use the Kaggle API to download competition data to a per-run folder
    meta = {"title": "Sample Competition", "url": kaggle_url}
    data_path = f"runs/{run_id}/data/"
    os.makedirs(data_path, exist_ok=True)
    # Insert Kaggle API download logic here
    return meta, data_path