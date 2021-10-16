# 概要

PyconJP 2021で利用するゲームです。
参加いただけた方、ありがとうございました！問題、どうでしたでしょうか？
今回FastAPIとCloudRunで構成していたりするので、よければコードの方も見ていってください！


## 問題の答え・解説

### 1問目

```
【問題】次のうち、PythonのAPIフレームワークでないものはどれか。
1： FastAPI 2： Flask 3： SymPy 4： Tornado
```

答え: 3のSimPyは数学系のライブラリです


### 2問目

```
datetimeパッケージで、datetime型を「x年x月x日x時x分x秒」(例: 2021年10月13日12時01分23秒)というフォーマットで出力させたいです。
この場合、strftime関数に入力する文字列はどのようになりますか？
月、日、時、分、秒はそれぞれ2桁の0埋め、時刻は24時間表記になります。
引数の文字列の中身を回答してください。
```

答え: "%Y年%m月%d日%H時%M分%S秒"

### 3問目

```
【問題】二つの文字を1文字ずつ結合させた文章を作成してください。「りんご」と「ぱいそん」なら、正解は「りぱんいごそん」になります。

以下の二つの文章を組み合わせた場合、どのような単語になるでしょうか？
「Python(パイソン) は1990年代初頭ごろから公開されているプログラミング言語」
「汎用的なプログラミング言語で、いろいろなアプリケーション開発や、システム管理ツールとして幅広く使われています」
```

答え: itertoolにあるzip_longest関数を使うとうまく文字列が取得できます。
(zip関数を使うと、短い方の文字列が終わったタイミングでループが終了してしまうという引掛けがあります。)

### 4問目

```
【問題】\u3071\u3044\u3053\u3093\u3058\u3047\u30fc\u3074\u30fc\u3078\u3088\u3046\u3053\u305d というメッセージが記載されていました。これはどのような意味でしょうか？
```

print("\u3071\u3044\u3053\u3093\u3058\u3047\u30fc\u3074\u30fc\u3078\u3088\u3046\u3053\u305d") とすると「ぱいこんじぇーぴーへようこそ」という文字列になります

### 5問目

```
【問題】以下の文章を解読してください。
     例: Uryyb Jbeyq!! -> Hello World!!
     Gunax lbh sbe ivfvgvat gur WK obbgu!
```

13文字ずつずらすと「Thank you for visiting the JX booth!」という答えが出ます。rot13という暗号です。

回答例
```
>>> import codecs
>>> codecs.decode('Uryyb, Jbeyq!', 'rot13')
```

## ざっくり仕組み解説

- API: FastAPI
- インフラ: CloudRun
- ドメイン: Firebase hosting

で行っています。問題文などはconf/text.yamlにあります。
(もっと詳しい解説はJXのテックブログで公開予定です！ https://tech.jxpress.net/ )
## デプロイ手順

```bash
# Cloud Runのデプロイ
gcloud run deploy game --source . --min-instances 1


# hostingの登録(1回のみ)
firebase target:apply hosting game jxpress-pycon2021

# hostingのデプロイ
firebase deploy --only hosting:game
```
