import requests

url = 'https://kauth.kakao.com/oauth/token'
rest_api_key = '97905cbe18f0ede6eae790b6812bd965'
redirect_uri = 'http://naver.com'
authorize_code = '6AESxNPPjV3-RWx4Akc3hht50d8x1fyh7MTqbuf1CisM0gAAAYWkU7Yd'

data = {
    'grant_type':'authorization_code',
    'client_id':rest_api_key,
    'redirect_uri':redirect_uri,
    'code': authorize_code,
    }

response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# json 저장
import json

with open("kakao_code.json","w") as fp:
    json.dump(tokens, fp)




import requests
import json

with open("kakao_code.json","r") as fp:
    tokens = json.load(fp)

url="https://kapi.kakao.com/v2/api/talk/memo/default/send"

# kapi.kakao.com/v2/api/talk/memo/default/send 

headers={
    "Authorization" : "Bearer " + tokens["access_token"]
}

data={
    "template_object": json.dumps({
    	
        "object_type": "text",
        "text": "안녕? 나는 잉빈이야",
        "link": {
            "web_url" : "헤헤. text와 link 객체는 필수로 넣어야 하는 거구나? button_title과 buttons는 안 넣어도 상관 없지만 말이야!",
            "mobile_web_url" : "헤헤. text와 link 객체는 필수로 넣어야 하는 거구나? button_title과 buttons는 안 넣어도 상관 없지만 말이야!"
        },
        "button_title" : "헤헤"   
    })
}

response = requests.post(url, headers=headers, data=data)
response.status_code