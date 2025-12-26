from extract import extract_data
from transform import transform_data

if __name__ == "__main__":
    df_raw = extract_data("data/raw/studentsRaw.csv")
    df_clean = transform_data(df_raw)
    print(df_clean)