# !/bin/python
import json
import requests


def auth():
    """获取 token"""
    # 在此处填写你的SetApp帐号：
    email = 'Input your account(email):'
    # 在此处填写你的SetApp密码：
    password = 'Input your password:'

    response = requests.post(
        url="https://user-api.setapp.com/v1/auth",
        headers={
            "Accept": "application/json",
            "Content-Type": "text/plain; charset=utf-8",
        },
        json={'email': email, 'password': password, 'remember': 'true'})
    token = response.json()['data']['token']
    return token


def delete():
    """删除用户"""
    try:
        token = auth()
        headers = {
            "Authorization": f"Token {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        }

        device_id = requests.get(url="https://user-api.setapp.com/v1/devices", headers=headers).json()['data'][0]['id']
        r = requests.delete(f'https://user-api.setapp.com/v1/devices/{device_id}', headers=headers)
        return f'Successfully deleted device {device_id}.'
    except:
        return 'Execution failed.'


if __name__ == "__main__":
    print(delete())
