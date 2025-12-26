from sqlalchemy import create_engine
import pandas as pd

def load_data(df: pd.DataFrame, table_name: str = "students") -> None:
    engine = create_engine("sqlite:///students.db")
    df.to_sql(table_name, engine, if_exists="replace", index=False)

    print(f"[LOAD] Successfully loaded {len(df)} records" f"into table {table_name}")  
    