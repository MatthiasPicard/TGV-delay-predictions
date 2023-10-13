import pandas as pd
import numpy as np


# All functions used to pres-post- process dataset


def get_train_test_set(df):
    train_idx = []
    test_idx = []
    for i, d in enumerate(df["date"].tolist()):
        month, day, year = d.split('/')
        if int(year)<2023:
            train_idx.append(i)
        else:
            test_idx.append(i)
    
    train_set = df.iloc[train_idx].copy(deep=True)
    test_set = df.iloc[test_idx].copy(deep=True)
    
    return train_set, test_set

def clean_df(df):
    # Add commands to clean dataframe
    df = df.dropna(axis=1, how='all')
    df = df.drop("commentaires_retard_arrivee", axis=1) # str and not relevant for model
    return df