import pandas as pd

def read_CSV():
    df = pd.read_csv("Testdata.csv")
    print(df)
    print("I am reading the excel file")