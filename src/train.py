import numpy as np
import pandas as pd
import hydra
import gc
import os

from pathlib import Path
import mlflow
from utils import git_commits

from sklearn import feature_extraction, linear_model, model_selection, preprocessing

rand = np.random.randint(0, 1000000)

def save_log(score_dict):
    mlflow.log_metrics(score_dict)
    mlflow.log_artifact(".hydra/config.yaml")
    mlflow.log_artifact(".hydra/hydra.yaml")
    mlflow.log_artifact(".hydra/overrides.yaml")
    mlflow.log_artifact(f"{os.path.basename(__file__)[:-3]}.log")
    mlflow.log_artifact("features.csv")

@git_commits(rand)
def run(cfg):
    cwd = Path(hydra.utils.get_original_cwd())

    data = [pd.read_pickle(cwd / f"../features/{f}.pkl") for f in cfg.features]
    data = pd.concat(data, axis=1)

    count_vectorizer = feature_extraction.text.CountVectorizer()
