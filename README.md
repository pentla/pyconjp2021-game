# 概要

PyconJP 2021で利用するゲームです。

## デプロイ


```bash
# Cloud Runのデプロイ
gcloud run deploy game --source . --min-instances 1


# hostingの登録(1回のみ)
firebase target:apply hosting game jxpress-pycon2021

firebase deploy --only hosting:game

```
