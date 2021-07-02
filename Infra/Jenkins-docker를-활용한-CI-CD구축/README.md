# Jenkins + docker를 활용한 CI/CD구축
> :bulb: Docker로 jenkins이미지을 간편하게 설치하고 gitlab에 연동해 CI/CD 환경을 구축해 본다.

## 주요 개념
- CI / CD
  - CI(Continuous Integration) 지속적인 통합
  - CD(Continuous Delivery / Continuous Deployment) 지속적인 서비스제공 / 지속적인 배포
  - 애플리케이션 개발 단계를 자동화하여 애플리케이션 개발을 보다 짧은 주기로 고객에게 제공하고,
    새로운 코드 통합으로 통합지옥(Integration hell)을 해결하는 방식
- 

## 과정
- Docker 설치
  - https://docs.docker.com/get-docker/
  - command 창에서 `docker --version` 확인
  - `docker run -d -u root -p 9090:8080 --name=jenkins jenkins/jenkins` 명령어로 jenkins설치
  - `http://localhost:9090/`로 브라우저에서 주소 확인
  - jenkins 로그인 화면이 제대로 뜨면, cmd에 `docker logs jenkins` 명령어로 패스워드 확인후 로그인
- Nginx 설치
  - `docker run --name nginx -d -p 80:80 -v c:/Users/moder/dist:/usr/share/nginx/html nginx` cmd에 입력

## 소주제2
-
-

## 참고자료
-
-

## 과제제출
- [기본과제](기본과제)
- [심화과제](심화과제)
