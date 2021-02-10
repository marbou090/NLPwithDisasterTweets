import git
import argparse
import yaml
from pathlib import Path
import os
import pandas as pd
import numpy as np
import inspect
from time import time
import csv
import re
from abc import ABCMeta, abstractmethod
from contextlib import contextmanager

@contextmanager
def timer(name):
    t0 = time()
    print(f'[{name}] start')
    yield
    print(f'[{name}] done in {time() - t0:.0f} s')

def git_commits(rand):
    def func_decorator(my_func):
        print("experiment_name: ", rand)

        repo = git.Repo(str(Path(os.getcwd()).parents[0]))
        repo.git.diff("HEAD")
        repo.git.add(".")
        repo.index.commit(f"{rand}(before running)")

        def decorator_wrapper(*args, **kwargs):
            my_func(*args, **kwargs)

            repo.index.commit(f"{rand}(after running)")
            repo.git.push('origin', 'master')
        return decorator_wrapper

    return func_decorator

def get_arguments(description):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--force', '-f', action='store_true', help='Overwrite existing files')
    return parser.parse_args()


def get_features(namespace):
    for k, v in ({k: v for k, v in namespace.items()}).items():
        if inspect.isclass(v) and issubclass(v, Feature) and not inspect.isabstract(v):
            yield v()


# @hydra.main(config_path="config.yaml")
def generate_features(namespace, overwrite):
    for f in get_features(namespace):
        if f.data_path.exists() and not overwrite:
            print(f.name, 'was skipped')
        else:
            f.run().save()


class Feature(metaclass=ABCMeta):
    prefix = ''
    suffix = ''
    dir = 'kaggle_env'

    def __init__(self):
        if self.__class__.__name__.isupper():
            self.name = self.__class__.__name__.lower()
        else:
            self.name = re.sub("([A-Z])", lambda x: "_" + x.group(1).lower(), self.__class__.__name__).lstrip('_')

        # ユーザーに更新してもらう
        self.data = pd.DataFrame()
        self.data_path = Path(self.dir) / f"{self.name}.pkl"

    def run(self):
        with timer(self.name):
            self.create_features()
            prefix = self.prefix + '_' if self.prefix else ''
            suffix = '_' + self.suffix if self.suffix else ''

            self.data.columns = prefix + self.data.columns + suffix
        return self

    @abstractmethod
    def create_features(self):
        raise NotImplementedError

    def save(self):
        self.data.to_pickle(str(self.data_path))

    def load(self):
        self.data = pd.read_pickle(str(self.data_path))

def create_memo(col_name, desc):
    file_path = Feature.dir + "/_features_memo.csv"

    # hydraのログパスにカレントディレクトリが移動してしまうので初期化
    # 影響がないことは確認済み
    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    if not os.path.isfile(file_path):
        with open(file_path, "w"): pass

    with open(file_path, "r+") as f:
        lines = f.readlines()
        lines = [line.strip() for line in lines]

        col = [line for line in lines if line.split(",")[0] == col_name]
        if len(col) != 0: return

        writer = csv.writer(f)
        writer.writerow([col_name, desc])
