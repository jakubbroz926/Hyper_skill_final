import pandas as pd
import os
pd.set_option("display.max_columns", 8)

def print_load(lst):
    os.chdir(r"test")
    df_frames = {i.split("/")[1].split(".")[0]:pd.read_csv(i.split("/")[1]) for i in lst}
    standart_columns = df_frames["general"].columns.to_list()
    for k,v in df_frames.items():
        v.columns = standart_columns
    new = pd.concat([df_frames["general"],df_frames["prenatal"],df_frames["sports"]],ignore_index=True)
    new.drop("Unnamed: 0",axis=1,inplace=True)
    new.dropna(axis = 0, how = "all",inplace=True) 
    new["gender"]= new["gender"].replace(["male","man"],"m")
    new["gender"]= new["gender"].replace(["woman","female",None],"f")
    new.fillna(0,inplace=True)
    print(new.shape)
    print(new.sample(20,random_state = 30))
print_load([r"test/general.csv",r"test/prenatal.csv",r"test/sports.csv"])