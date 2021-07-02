# React로 만드는 Tic Tac Toe
> :bulb: React 공식 홈페이지의 튜토리얼에 따라서 코딩을 해봄으로써 기본적인 CRUD 기능 구현을 익힘

## 목표
- React 기초 파악

## React 시작
**Create React App**

```
npx create-react-app <app name>
cd <app name>
npm start
```

- npx는 실수가 아닌 npm의 패키지 실행도구



## 주요개념

**Hello World**

- ```react
  ReactDOM.render(
    <h1>Hello, world!</h1>,
    document.getElementById('root')
  );
  ```



**JSX 표현식 포함**

- ```react
  const name = 'Josh Perez';const element = <h1>Hello, {name}</h1>;
  ReactDOM.render(
    element,
    document.getElementById('root')
  );
  ```



- 이후 추가 정보들 차차 개인적으로 정리할 예정



## 참고자료
- https://ko.reactjs.org/

## 과제제출
- [기본과제](기본과제)
- [심화과제](심화과제)
