import sys
import os
sys.path.append(os.path.abspath("."))
from utils import create_memo,generate_features,Feature
from preprocess import base_train,base_test
import hydra

import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
from sklearn import feature_extraction, linear_model, model_selection, preprocessing

# 生成された特徴量を保存するパス
Feature.dir = "features"
# trainとtestを結合して基本的な前処理を行ったデータを呼ぶ
train = base_train()
test = base_test()

class BaseTextData(Feature):
    def create_features(self):
        self.train = train["text"]
        create_memo("BaseTextData", "テキストデータのみ")

@hydra.main(config_name="../config/config.yaml")
def run(cfg):
    # overwriteがfalseなら上書きはされない
    # globals()からこのファイルの中にある特徴量クラスが選別されてそれぞれ実行される
    print("Start!")
    generate_features(globals(), cfg.base.overwrite)
    print("sucess!")


# デバッグ用
if __name__ == "__main__":
    run()