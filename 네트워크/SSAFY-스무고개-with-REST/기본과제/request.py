import requests
import json
# content-type을 json으로 지정하여 보냈으므로, data의 json 파싱이 필요하다.
r = requests.post('http://13.125.222.176/quiz/jordan', data= json.dumps({
    'nickname': "서울2반정원혁",
    'yourAnswer': "kubernetes"
}), headers={
    # 데이터 돌려줄 때, 받고 싶은 형식
    "Accept": "application/json; charset=utf-8",
    # 내가 보내는 데이터 형식
    "Content-Type": "application/json; charset=utf-8"
}
).json()
# .text / .headers 등도 사용 가능 아무것도 안붙이면 <Response(200)>의 형태로 반환.

print(r)