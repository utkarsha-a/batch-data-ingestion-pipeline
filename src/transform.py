import pandas as pd
def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    initial_cnt = len(df)
    df = df.drop_duplicates()
    df.columns = (df.columns.str.strip().str.lower().str.replace(" ","_"))
    if "age" in df.columns:
        df["age"] = df["age"].fillna(df["age"].median())

    if "score" in df.columns:
        df["score"] = df["score"].fillna(0)

    if "age" in df.columns:
        df["age"] = df["age"].astype(int)

    if "score" in df.columns:
        df["score"] = df["score"].astype(float)

    final_cnt = len(df)

    print(f"[TRANSFORM] Record before: {initial_cnt} | " f"after cleaning: {final_cnt}")

    return df

    
