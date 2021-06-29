# Linux 머신 구하기
> :bulb: 클라우드 서비스 혹은 WSL2로 리눅스 환경 확보, Docker Setup 등을 실습해보면서 2학기 프로젝트의 인프라 및 클라우드 서비스 이해하기

## 진행 방식
- 가상머신(Virtual Machine) 사용
  - 기존에 보유하고 있던 책을 이용해 실습 진행(Centos 설치)
- WSL2 이용
  - 네이버 클라우드나, AWS 이용한 서버 생성을 하려 했으나, 결제요구가 걱정되어 일단 WSL2를 이용한실습 진행

## WSL2 방식
- 관리자 권한으로 Powershell 실행
- WSL 옵션 기능 사용 설정
  - `dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart`
- WSL 2 설치전 "가상 머신 플랫폼" 옵션 기능을 사용하도록 설정
  - `PS C:\WINDOWS\system32> dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart`
- MS Store에서 원하는 Linux 패키지 설치(Ubuntu 20.04 LTS 등)
- 설치 후 실행
- 원하는 아이디, 비밀번호 입력 후 계정 생성, `<설정id>@DESKTOP~` 뜰 시, 접속 완료
- 실행된 경우, 커널 패치
  - https://docs.microsoft.com/ko-kr/windows/wsl/install-win10#step-4---download-the-linux-kernel-update-package
- WSL 2를 기본 버전으로 설정
  - `PS C:\WINDOWS\system32> wsl --set-default-version 2`
- 이후 접속 방법
  - **PowerShell 관리자 모드 접속 후 `wsl` 입력**
  - 최초 실행시 생성한 계정으로 자동 접속됨.

## 발생 문제 및 해결방식
- Linux 설치 후 실행시, `0x8007019e` 오류 발생
  - Hyper-V 설치 및 활성화로 해결
    **What is Hyper-V?**
    Hyper-V는 특히 하드웨어 가상화를 제공합니다. 즉, 각 가상 컴퓨터가 가상 하드웨어에서 실행됩니다. Hyper-V를 통해 가상 하드 드라이브, 가상 스위치 및 가상 컴퓨터에 추가할 수 있는 각종 가상 디바이스를 만들 수 있습니다.
    - 이전 버젼의 Windows 혹은 Windows가 아닌 다른 운영체제에 필요한 소프트웨어 실행 가능
    - 한 시스템에서 여러가지 운영체제 사용 가능
  - PowerShell에 아래 코드 중 하나 입력
    - `Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All`
    - `DISM /Online /Enable-Feature /All /FeatureName:Microsoft-Hyper-V`



## 참고자료
- https://docs.microsoft.com/ko-kr/virtualization/hyper-v-on-windows/quick-start/enable-hyper-v
  - 오류 발생시 Hyper-V 활성화하여 수정 필요할 시 참고
- https://positivemh.tistory.com/589
  - 참고한 설치 가이드

## 과제제출
- [기본과제](기본과제)

