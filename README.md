# Lineに通知を送りたい方へ...

## インストール

```
git clone git@github.com:DaikiMiwa/line_notify.git
cd line_notify
pip install -e .
```

依存するパッケージはありません.

## 準備

1. https://notify-bot.line.me/ja/ に自分のLINEアカウントでログイン
2. 右上の自分のアカウント>マイページに行く
3. Generate token を押して表示されるトークンをメモしておく

<img width="1021" alt="Screen Shot 2022-05-14 at 11 48 35" src="https://user-images.githubusercontent.com/63869611/168408095-bbbf93f4-75b8-4893-b49c-42ebf1829a7c.png">

## 使い方

```
import notifyline as ln

token = "準備でメモしたトークン"
message = "送信したいテキスト"

# 通知を送信
ln.notify_line(message,token)
```

以上を実行すると, lineにメッセージが送信されるはずです
実験の終了や進捗状況を通知すると便利ではないでしょうか？
