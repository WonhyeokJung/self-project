# 산출물

**시작 코드**

```python
import requests
import json

r = requests.post('http://13.125.222.176/quiz/alpha', data= json.dumps({
    'nickname': "서울2반정원혁",
    'yourAnswer': "19"
}), headers={
    "Accept": "application/json; charset=utf-8",
    "Content-Type": "application/json; charset=utf-8"
}
).json()

print(r)
```



**A1**

```python
{'code': 200, 'question': 'Q2: SSAFY 6기에는 새로운 캠퍼스가 오픈을 하게 되는데요. 이곳은 어디
일까요? (영문) (정답 OO)', 'nextUrl': 'bravo'}  // busan
```

**A2**

```python
{'code': 200, 'question': 'Q3: SSAFY의 인스타그램에는 SSAFY의 여러 모습들이 올라와 있는데요. SSAFY의 소식을 전해주는 기자단의 영문 명칭은 무엇일까요?', 'nextUrl': 'chopper'}  // ssafycial
```

**A3**

```python
{'code': 200, 'question': 'Q4: 교차 출처 리소스 공유(Cross Origin Resource Sharing)는 추가적인
 http 헤더를 이용하여, 한 출처에서 실행 중인 웹 애플리케이션이 다른 출처의\n자원에 접근할 수  
있는 권한을 부여하도록 브라우저에 알려주는 것을 말합니다. 자원의 출처가 다르다는 것은 3가지 요
소를 가지고 파악하는데요.\n3가지 요소에는 domain, port, 그리고 이것이 있습니다. 이것은 무엇일 
까요? (영문)', 'nextUrl': 'weekend'} // protocol
```

**A4**

```python
{'code': 200, 'question': 'Q5: 이것은 경량의 데이터 교환 형식으로, 사람과 기계가 읽고 쓰기에 
용이하며, Javascript 객체 문법으로 구조화된 데이터를 표현하기 위한 문자 기반의\n데이터 포맷이 
다. 객체를 나타낼 때 중괄호로 시작해서 중괄호로 끝나는 이것은 무엇인가? (영문, 약자)', 'nextUrl': 'river'} // json
```

**A5**

```python
{'code': 200, 'question': 'Q6: 이것은 프로그램 내에서 인스턴스가 오직 하나만 생성되는 것을 보
장하고, 프로그램 어디서든 이 인스턴스로의 접근을 허용하는 것입니다. 이 패턴은 무엇일까요?\n(영
문, OOOO pattern)', 'nextUrl': 'hand'}  // singleton
```

**A6**

```python
{'code': 200, 'question': 'Q7: 브라우저에 데이터를 저장하는 방법에는 storage, indexed DB, 그리
고 이것이 있습니다. session ID를 저장하는 용도로도 사용되는 이것은 무엇일까요? (영문)', 'nextUrl': 'over'}  // cookie
```

**A7**

```python
{'code': 200, 'question': 'Q8: 이것은 Remote Dictionary Server의 약자로, 키-값 구조의 비정형 
데이터를 저장하고 관리하기 위한 오픈 소스 비관계형 DBMS다.\n인스타그램, LINE 등에서 널리 사용 
되는 이것은? (영문)', 'nextUrl': 'hello'}  // redis
```

**A8**

```python
{'code': 200, 'question': 'Q9: 이것은 디자인 패턴의 하나로 Model + View + View Model을 합친 말
이다. View와 Model 사이에 의존성을 없애고 모듈화를 가능하게 만든 이것은?(영문, OOOO pattern)', 'nextUrl': 'python'}  // mvvm
```

**A9**

```python
{'code': 200, 'question': 'Q10: 이것은 파이썬의 라이브러리로 데이터 조작 및 분석을 위해서 주로
 사용된다. pd라는 약어로 주로 사용되는 이것은? (영문)', 'nextUrl': 'java'}  // pandas
```

**A10**

```python
{'code': 200, 'question': 'Q11: 이것은 근거리 무선 통신 기술의 하나로 2.4Ghz 대역폭을 사용한다
. 갤럭시 버즈와 같은 무선 이어폰에 주로 사용되며, 덴마크의 왕인 하랄 블로탄의 이름에서 유래한 
이것은? (영문)', 'nextUrl': 'script'}  // bluetooth
```

**A11**

```python
{'code': 200, 'question': 'Q12: SSAFY 1기 교육생들이 출시한 앱으로, 삼성전자 해외연구소 파견 
교육과정 중 우크라이나 팀에서 개발한 헬스케어 앱의 이름은? (영문)', 'nextUrl': 'zero'}  // fittymon
```

**A12**

```python
{'code': 200, 'question': 'Q13: In computing, this is an optimization technique used primarily to speed up computer programs by storing results of expensive\nfunction calls and returning the cached result when the same inputs occur again. What is this? (영문)', 'nextUrl': 'coat'}  // memoization
```

**A13**

```python
{'code': 200, 'question': 'Q14: 전통적인 프로그래밍에서는 개발자가 작성한 프로그램이 외부 라이
브러리 코드를 호출한다. 그러나 이것이 적용된 구조에서는 외부 라이브러리 코드가 개발자가 작성한
 코드를 호출한다.\n이것은 무엇인가? (영문, 약자로 쓰시오)', 'nextUrl': 'sand'}  // ioc
```

**A14**

```python
{'code': 200, 'question': 'Q15: 이것은 리눅스의 응용 프로그램들을 소프트웨어 컨테이너 안에 배
치시키는 일을 자동화하는 오픈 소스이다. 리눅스에서 운영체제 수준 가상화의 추상화 및 자동화 계 
층을 추가적으로\n제공하기도 하는 이것은 무엇인가? (영문)', 'nextUrl': 'king'}  // docker
```

**A15**

```python
{'code': 200, 'question': 'Q16: 루트 노드에서 시작해서 다음 분기로 넘어가기 전에 해당 분기를 
완벽하게 탐색하는 방법으로, 미로를 탐색할 때 한 방향으로 갈 수 있을 때까지 계속 가다가 더 이상
 갈 수\n없게 되면 다시 가장 가까운 갈림길로 돌아와서 다른 방향으로 다시 탐색을 진행하는 것과  
유사한 이것은? (영문 3글자, 약자로 쓰시오)', 'nextUrl': 'knight'}  // dfs
```

**A16**

```python
{'code': 200, 'question': 'Q17: 삼성 갤럭시 Z 플립은 안드로이드 스마트폰으로 폴더블 디스플레이
를 탑재했다. 갤럭시 Z 플립의 개발 코드 네임은? (영문)', 'nextUrl': 'great'}  // bloom
```

**A17**

```python
{'code': 200, 'question': 'Q18: SSAFY의 공식 영문 명칭에서 가장 많이 등장하는 알파벳은? (영문)', 'nextUrl': 'again'}  // a
```

**A18**

```python
{'code': 200, 'question': 'Q19: 이 정렬 방법은 토니 호어가 고안한 방법으로, 다른 원소와의 비교
만으로 정렬을 수행하는 비교 정렬 방법의 하나이다. 평균적으로 O(n log n)의 시간복잡도를 가지는\n이 정렬은 무엇인가? (영문, OOO sort)', 'nextUrl': 'ring'}
```

**A19**

```python
{'code': 200, 'question': 'Q20: 이것은 컨테이너화된 애플리케이션의 자동 배포, 스케일링 등을 제
공하는 관리시스템으로 오픈 소스이다. 구글에 의해 설계되었고, 리눅스 재단에 의해 관리되고 있으 
며\n도커와 같은 컨테이너 도구와 함께 동작하는 이것은 무엇인가? (영문)', 'nextUrl': 'jordan'} // kubernetes
```

**A20**

```python
{'code': 200, 'question': '모든 문제를 완료하셨습니다.', 'nextUrl': '수고하셨습니다.'}
```