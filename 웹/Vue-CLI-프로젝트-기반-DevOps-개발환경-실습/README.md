# Vue CLI 프로젝트 기반 DevOps 개발환경 실습
> :bulb: Vue CLI로 프로젝트를 생성하여 GitHub Pages에 정적 페이지 호스팅 하기 & GitHub Actions로 자동 배포 설정해서 DevOps 개발환경을 구성하는 실습하기

## 목표
- Vue CLI를 이용한 정적 웹 배포 실습

## 등장 개념
- Yarn
- DevOps
- Deploy(배포) & Hosting
- 정적 페이지 / 동적 페이지
- github actions workflow

## 진행과정 및 발생문제

### yarn deploy 명령어를 통한 수동으로 빌드된 정적 파일 배포 서비스 운영 방법

**Node.js 설치**

- 안정버전(LTS) 설치



**yarn 설치**

- 양자택일
  - [설치경로](https://classic.yarnpkg.com/en/docs/install)
  - `npm install --global yarn`



**Vue CLI 설치**

- 양자택일
  ※ `@vue/cli`는 ver 3.x 이상을, `vue-cli`는 ver 2.x를 의미한다.
- - `npm install -g @vue/cli`
  - `yarn global add @vue/cli` 



**Vue 프로젝트 생성**

- ` vue create **원하는 프로젝트명**`
- 생성 시 선택지
  - Manual select features
  - Unit Testing  추가 선택(* 표시된 경우 선택 의미)
    **※여기서 잘못 선택하여 unit:test를 제대로 진행하지 못함. 체크를 해제함**
  - 3.x
  - ESLint + Prettier
  - Lint on save
  - Jest
  - In dedicated config files
  - N(No)



**Server 실행**

- 생성한 프로젝트 폴더로 이동 후, `yarn serve`로 서버 실행 후, 정상 실행시 종료



**Github Push & Deploy**

- Git Repo 생성(Public)

- 프로젝트 폴더 최상위에서 `remote add origin` + `git push -u origin main`
  **※안될 경우 git repo page 참고 후 `git branch -m main` 등 진행 후 할 것**

- `yarn add gh-pages -D`
  GitHub Pages로 배포하기 위한 라이브러리

- `package.json`에 `homepage, script > predeploy, deploy, clean` 부분 추가
  ![image-20210629171838416](../../../../../AppData/Roaming/Typora/typora-user-images/image-20210629171838416.png)

- 배포용 Path 설정
  이 설정이 있어야 https://<github_id>.github.io/<github_repo_name>에서 정상적 페이지 확인 가능

  - 프로젝트 최상위 폴더에 `vue.config.js` 생성 및 아래 내용 작성

    - ```javascript
      module.exports = {
      	publicPath: "/<github_repo_name>",
      	outputDir: "dist"
      }
      ```

    **`<github_id>.github.io`로 GitHub Pages 대표 repo를 만들게 되면 이 설정은 필요없고 위처럼 sub path도 불필요함**

     

- `yarn deploy`
  위 명령 실행시, 빌드된 정적 파일을 원격 저장소의 `gh-pages` 브랜치를 생성하여 Push한다.
  에러 발생시, `yarn clean` 후 재시도

- git repo 페이지에서 배포 주소 확인 후 접속
  - repo page - settings - pages - `published된 주소` 확인

- 쉽게 이동하기 위해 repo에서 웹사이트 주소 설정
  - Main page - about 옆 톱니바퀴 - Website에 주소 설정



### GitHub Actions workflow를 이요한 배포 자동화

- Github는 현재 개발자와 DevOps 엔지니어 팀이 신속하게 어플리케이션을 빌드하고 배포할 수 있도록 지원하고 있음.
- GitHub Actions는 GitHub의 소프트웨어 개발 Workflow에서 작업을 자동화하기 위한 Package Script
- 개발자가 새 소스 코드를 Push하거나 Pull Request 같은 이벤트에 반응, 트리거하도록 구성이 가능



**Simple Workflow 파일 작성**

- repo main page - `Actions` - `Set up this workflow`
  - 파일명 `deploy.yml` , 파일 내 첫 줄 `name` 항목 `Deployment`로 설정
  - `Start commit` - `Commit new file`

- 커밋 후 샘플 workflow가 동작되는지, actions에서 확인



**Pull**

- Pull을 통해 deploy.yml pull
  - `git pull`
  - `vs code` 좌측 하단의 `sync` 버튼 사용



**workflow 파일(deploy.yml) 내용 수정**

- ```
  # This is a basic workflow to help you get started with Actions
  
  name: Deployment
  
  # Controls when the workflow will run
  on:
    # Triggers the workflow on push or pull request events but only for the main branch
    push:
      branches: [ main ]
    pull_request:
      branches: [ main ]
  
    # Allows you to run this workflow manually from the Actions tab
    workflow_dispatch:
  
  # A workflow run is made up of one or more jobs that can run sequentially or in parallel
  jobs:
    # This workflow contains a single job called "build"
    deploy:
      # The type of runner that the job will run on
      runs-on: ubuntu-latest
  
      # Steps represent a sequence of tasks that will be executed as part of the job
      steps:
        # Checks-out your repository under $GITHUB_WORKSPACE, so your job can access it
        - name: Checkout source code
          uses: actions/checkout@master
  
        - name: Set up Node.js
          uses: actions/setup-node@master
          with:
            node-version: 14.x
        
        - name: Install dependencies
          run: yarn install
  
        - name: Build page
          run: yarn build
          env:
            NODE_ENV: production
        
        - name: Deploy to gh-pages
          uses: peaceiris/actions-gh-pages@v3
          with:
            github_token: ${{ secrets.GITHUB_TOKEN }}
            publish_dir: ./dist
  
        # Runs a single command using the runners shell
        - name: Run a one-line script
          run: echo Hello, world!
  
        # Runs a set of commands using the runners shell
        - name: Run a multi-line script
          run: |
            echo Add other actions to build,
            echo test, and deploy your project.
  
  ```

- `commit` 후 확인



**Code 수정 및 테스트 실패로 인한 자동 배포 실패 확인**

- `deploy.yml` 파일 내 `yarn install, build` 사이 `단위 테스트 step` 을 추가

  ```
  - name: Test unit
    run: yarn test:unit
  ```

- `HelloWorld.vue` 내 `h1 태그` 값을 다음과 같이 수정
  `<h1>테스트 실패 연습</h1>h1>`
  **App.vue에서 전달한 props data를 사용해 렌더링 하지 않아 HelloWorld.vue 컴포넌트 테스트가 실패하게 됨**
- 커밋 & 푸시(vs code 좌측 상단에서 커밋 후, 좌측 하단 sync 버튼으로 push 가능)
- `Actions`에서 배포 실패 확인



**코드 재 수정 및 배포 성공 확인**

- HelloWorld의 h1 태그 `<h1>{{ msg }}</h1>`으로 변경 후 다시 커밋& 푸시
- 정상 출력 `main page - Actions`에서 확인

## 참고자료
- Vue 프로젝트 빌드 시스템의 이해
  - https://vue-loader-v14.vuejs.org/kr/
- Vue Test Utils with Jest
  - https://vue-test-utils.vuejs.org
- DepOps의 이해
  - https://docs.microsoft.com/ko-kr/learn/paths/automate-workflow-github-actions/

## 과제제출
- [기본과제](기본과제)
- [심화과제](심화과제)
