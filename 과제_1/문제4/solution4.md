# ✅ 1. 기초 git 환경 구축

- 개행문자 설정을 윈도우는 true, 맥은 input 값으로 지정한다.
    - 설정: git config --global core.autocrlf input
    - 확인: git config --global core.autocrlf

- 사용자 이름과 이메일 주소를 설정한다.
    - 이름 설정: git config --global user.name "Somin"
    - 이메일: git config --global user.email "somin@example.com"

기본 브랜치 이름을 main으로 변경한다.
    - git config --global init.defaultBranch main

Git 전역 설정 목록을 명령어로 확인한다.
    - git config --global --list

Git 전역 설정을 에디터에서 띄워서 전체 설정을 확인한다.
    - git config --global -e

Git의 기본 에디터를 Visual Studio Code로 변경한다.
    - git config --global core.editor "code --wait"