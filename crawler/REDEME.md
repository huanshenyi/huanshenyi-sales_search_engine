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
```text
curl http://localhost:6800/daemonstatus.json
```


レスポンス例:
```text
{"node_name": "tanoMacBook-Pro.local", "status": "ok", "pending": 0, "running": 0, "finished": 0}
```

## サーバー上のクローラーを起動
```text
curl http://localhost:6800/schedule.json -d project=crawler -d spider=mynavi
```

## サーバー上のクローラー を停止する

```text
curl http://localhost:6800/cancel.json -d project=crawler -d job=6487ec79947edab326d6db28a2d86511e8247444
```

## アップロードされたプロジェクトを確認

```text
curl http://localhost:6800/listprojects.json
```

## プロジェクトのバージョンを確認

```text
curl http://localhost:6800/listversions.json?project=crawler

```

レスポンス例:
```json
{"node_name": "tanoMacBook-Pro.local", "status": "ok", "versions": ["1571637778", "1571640069"]}

```

## プロジェクト内にあるクローラー を確認

```text
curl http://localhost:6800/listspiders.json?project=crawler
```

レスポンス例:

```json
{"node_name": "tanoMacBook-Pro.local", "status": "ok", "spiders": ["doda", "en", "green", "indeed", "mynavi", "next_rikunabi", "type", "wantedly"]}

```

## あるプロジェクトのクローラー の実行状態

```text
curl http://localhost:6800/listjobs.json?project=crawler | python3 -m json.tool

```

レスポンス例:

```json
{
    "node_name": "tanoMacBook-Pro.local",
    "status": "ok",
    "pending": [],
    "running": [],
    "finished": [
        {
            "id": "cb8f3464f3cd11e9badfacde48001122",
            "spider": "mynavi",
            "start_time": "2019-10-21 15:41:23.122928",
            "end_time": "2019-10-21 15:43:30.774202"
        }
    ]
}
```

## プロジェクトのあるバージョンを削除

```text
curl http://localhost:6800/delversion.json -d project=crawler -d version=1571637778

```
レスポンス例
```json
{"node_name": "tanoMacBook-Pro.local", "status": "ok"}

```

全てのバージョン削除

````text
curl http://localhost:6800/delproject.json -d project=crawler
````

## 起動ファイルを指定する

```text
scrapyd -d 指定したいdir(/Users/tianxiaoyi/spider/sales_search_engine/crawler)
```