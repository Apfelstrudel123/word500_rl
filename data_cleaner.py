import pandas as pd

INPUT_PATH = path_len_5 = "./data/words_len_5_raw.csv"
OUTPUT_PATH = path_len_5 = "./data/words_len_5_cleaned.csv"
LENGTH = 5

df = pd.read_csv(INPUT_PATH)
lst = df.columns.tolist()
cleaned = [s.strip().lower() for s in lst]
cleaned = [s for s in cleaned if len(s) == LENGTH]
df = pd.DataFrame([cleaned])
df.to_csv(OUTPUT_PATH, index=False, header=False)
        