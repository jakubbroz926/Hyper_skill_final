import pandas as pd
import os
pd.set_option("display.max_columns", 8)

def print_load(lst):
    os.chdir(r"test")
    for i in lst:
        a = pd.read_csv(i.split("/")[1])
        print(a.head(20))
print_load([r"test/general.csv",r"test/prenatal.csv",r"test/sports.csv"])
