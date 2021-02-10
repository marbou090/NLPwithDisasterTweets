# NLP with Disaster Tweets 
[コンペページ](https://www.kaggle.com/c/nlp-getting-started)  
Twitterは緊急時に重要なコミュニケーションチャネルになりました。
スマートフォンの普及により、人々は自分が監視している緊急事態をリアルタイムで発表することができます。このため、より多くの機関がTwitterをプログラムで監視することに関心を持っています（つまり、災害救援組織や報道機関）。

しかし、人の言葉が実際に災害を告げているのかどうかは必ずしも明確ではありません。

著者は「ABLAZE」という言葉を明示的に使用していますが、比喩的にそれを意味します。これは、特に視覚補助を使用すると、すぐに人間に明らかです。しかし、それはマシンにはあまり明確ではありません。

このコンテストでは、実際の災害に関するツイートとそうでないツイートを予測する機械学習モデルの構築に挑戦します。手作業で分類された10,000件のツイートのデータセットにアクセスできます。NLPの問題に取り組むのが初めての場合は、起動して実行するための簡単なチュートリアルを作成しました。

## データ
### どのファイルが必要ですか？
train.csv、test.csv、sample_submission.csvが必要です。

### データ形式はどうあるべきですか？
トレインとテストセットの各サンプルには、次の情報があります。

### ツイートテキスト
keywordそのツイートからのA （これは空白かもしれませんが！）
locationつぶやきは（ブランクであってもよい）から送信されました
私は何を予測していますか？
あなたは、与えられたツイートが実際の災害に関するものであるかどうかを予測しています。もしそうなら、を予測し1ます。そうでない場合は、を予測し0ます。

### ファイル
* train.csv-トレーニングセット
* test.csv-テストセット
* sample_submission.csv-正しい形式のサンプル送信ファイル

### 列
* id -各ツイートの一意の識別子
* text -ツイートのテキスト
* location -ツイートの送信元の場所（空白の場合があります）
* keyword -ツイートからの特定のキーワード（空白の場合があります）
* target-中train.csvつぶやきが本当の災害（約あるかどうかだけで、これは意味1）かありません（0）

# ディレクトリ
<pre>
.  
├── README.md  
├── __pycache__  
│   └── utils.cpython-39.pyc  
├── config  
│   └── config.yaml  
├── data  
│   ├── sample_submission.csv  
│   ├── test.csv  
│   └── train.csv  
├── features  
│   ├── _features_memo.csv  
│   └── base_text_data.pkl  
├── outputs  
│   └── 2021-02-11  
│       └── 04-29-54  
│           └── tutorialEDA.log  
├── requirements.txt  
├── src  
│   ├── DataCleaning.py  
│   ├── __pycache__  
│   │   └── preprocess.cpython-39.pyc  
│   ├── preprocess.py  
│   └── tutorialEDA.py  
└── utils.py  
</pre>

# 記録

## ver 1.0
細々と。

## ver 1.1
[機械学習実験環境を晒す](https://qiita.com/chizuchizu/items/8261bb831b2eebf1a6af#git%E9%96%A2%E4%BF%82)  
[Kaggleで使えるFeather形式を利用した特徴量管理法](https://amalog.hateblo.jp/entry/kaggle-feature-management)

ファイル構造見直した。ソールファイルは基本`/src`以下においてる。pyenvの仮想環境使ってるよ(`pyenv version`で確認できる)。ライブラリ追加したりしたら`pip freeze > requirements.txt`を忘れずに。