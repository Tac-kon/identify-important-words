# サイト内の主要ワード調査アプリ

## 環境

AWSへのアプリケーションデプロイの練習用プロジェクト。

https://identify-important-words.com/ からアクセス可能。


[tf-idf](https://ja.wikipedia.org/wiki/Tf-idf)の学習済みモデルを使用して、URL先のサイトの主要ワードを調査するアプリケーション。

- AWS EC2
  - Ubuntu22.04のイメージを使用
  - Route53を使用してドメインを取得
  - ACMを使用してSSL証明書を取得
- python: 3.9
  - 主要なライブラリ
    - streamlit: 1.17.0
    - simple_tfidf_japanese: 0.1.3
- Docker, Docker Composeを使用
  - Docker: 20.10.22
  - Docker compose: 2.10.0

## 起動/終了方法

### 起動時

1. Docker, Docker Composeをインストール (参考3. を参照)
2. リポジトリのクローン
   ```
   cd ~
   git clone https://github.com/Tac-kon/identify-important-words.git
   ```
3. Dockerコンテナの起動
   ```
   cd ~/identify-important-words
   sudo docker compose build
   sudo docker comopse up -d
   ```

### 終了時

1. Dockerコンテナを終了させる
   ```
   cd ~/identify-important-words
   sudo docker comopse down --remove-orphans
   ```

## 参考

1. simple_tfidf_japaneseについて:

- https://pypi.org/project/simple_tfidf_japanese/
- https://qiita.com/haminiku/items/4106395b9580fbd6edf2

2. AWS EC2の使用方法:

- https://qiita.com/minato-naka/items/ddb5f5301f9f590cdcbf#%E3%81%AF%E3%81%98%E3%82%81%E3%81%AB の①、⑥、⑦

3. Docker, Docker Composeのインストール方法

- https://qiita.com/kujiraza/items/a8236f65e2c46735ee91
