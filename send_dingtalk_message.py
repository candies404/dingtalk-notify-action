import os
import time
import hmac
import hashlib
import base64
import urllib.parse
import requests
import json

def send_dingtalk_message(webhook, secret, msg_type, content):
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

    url = f"{webhook}&timestamp={timestamp}&sign={sign}"

    headers = {'Content-Type': 'application/json'}
    data = {
        "msgtype": msg_type,
        msg_type: json.loads(content)
    }

    print("content内容为:", json.dumps(data, ensure_ascii=False, indent=2))

    response = requests.post(url, json=data, headers=headers)
    return response.json()

if __name__ == "__main__":
    webhook = f"https://oapi.dingtalk.com/robot/send?access_token={os.environ['DINGTALK_TOKEN']}"
    secret = os.environ['DINGTALK_SECRET']
    msg_type = os.environ['MSG_TYPE']
    content = os.environ['CONTENT']

    result = send_dingtalk_message(webhook, secret, msg_type, content)
    print("通知已发送:", result)
