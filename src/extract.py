import pandas as pd
import os
def extract_data(filepath: str) -> pd.DataFrame:
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"Raw data file not found!")
    
    df = pd.read_csv(filepath)
    print(f"[EXTRACT] Successfully ingested {len(df)} records")

    return df