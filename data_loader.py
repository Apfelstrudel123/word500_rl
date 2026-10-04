import pandas as pd
import random

def loadData(path: str):
    df = pd.read_csv(path)
    lst = df.columns.tolist()
    return [s.strip().lower() for s in lst]

def sampleWord(data: list):
    return random.choice(data)
        