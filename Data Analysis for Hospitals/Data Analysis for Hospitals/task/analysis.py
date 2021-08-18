import pandas as pd
import os


def print_load(lst):
    os.chdir(r"test")
    df_frames = {i.split("/")[1].split(".")[0]: pd.read_csv(i.split("/")[1]) for i in lst}  # data frames creation
    standard_columns = df_frames["general"].columns.to_list()
    for k, v in df_frames.items():
        v.columns = standard_columns  # updating all columns names in every df
    return df_frames


def dataframes_handler(df_frames):
    # divide program into smaller functions !! TODAY 17.8.2021 !!
    new = pd.concat([df_frames["general"], df_frames["prenatal"], df_frames["sports"]], ignore_index=True)
    new.drop("Unnamed: 0", axis=1, inplace=True)
    new.dropna(axis=0, how="all", inplace=True)  # cleaning all rows with empty values
    new["gender"] = new["gender"].replace(["male", "man"], "m")
    new["gender"] = new["gender"].replace(["woman", "female", None], "f")
    new.fillna(0, inplace=True)  # filling the void for the possible analysis in the future
    # print(new.shape)
    # print(new.sample(20, random_state=30))
    # Two upper lines are not necessary for succesfull completion
    return new


def questions(one_complete_df):
    pass


def main():
    lst = [r"test/general.csv", r"test/prenatal.csv", r"test/sports.csv"]
    frames = print_load(lst)
    new_df = dataframes_handler(frames)
    questions(new_df)


if __name__ == "__main__":
    pd.set_option("display.max_columns", 8)
    main()
