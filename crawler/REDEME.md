## scrapydインストール
```text
pip3 install scrapyd
```

## scrapydサーバー起動
```text
scrapyd
```

## scrapyクライアントインストール
```text
pip3 install scrapy-client
```

## クローラーをscrapdへアップロード
```text
scrapyd-deploy local(deployの別名) -p crawler(プロジェクト名)
```

## scrapydのサーバー状態を確認
curl http://localhost:6800/daemonstatus.json

レスポンス例:
```text
{"node_name": "tanoMacBook-Pro.local", "status": "ok", "pending": 0, "running": 0, "finished": 0}
```

## サーバー上のクローラーを起動
```text
http://localhost:6800/schedule.json -d project=crawler -d spider=mynavi
```