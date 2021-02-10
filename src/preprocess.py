import pandas as pd

def base_train():
    train = pd.read_csv("./data/train.csv")
    return train

def base_test():
    test = pd.read_csv("./data/test.csv")
    return test