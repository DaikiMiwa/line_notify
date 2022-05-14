import requests 

def notify_line(text:str,token:str):
    """ textとtokenを指定して実行することでlineに通知してくれます

    この関数を使うためには, line.meでaccess tokenを発行しておく必要があります.

    Args:
       text(str) : 送信するためのメッセージ
       token(str) : アクセストークン
    """

    url = "https://notify-api.line.me/api/notify"
    headers = {'Authorization':f'Bearer {token}'}
    data = {'message':f'message:{text}'}
    requests.post(url,headers=headers,data=data)
