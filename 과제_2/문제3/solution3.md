- DockerHub 저장소로부터 python:3 이미지를 PC로 받는다.
    - docker pull python:3

- python:3 이미지로 아래 기준으로 컨테이너를 실행한다.
    - bash 쉘과 함께 실행한다.
    - 컨테이너와 호스트 포트를 모두 80으로 설정한다.
    - docker run -it -p 80:80 python:3 bash

- 새로운 터미널 창을 띄워서 docker 명령어로 PC의 작업 디렉토리 전체 파일을 해당 컨테이너로 복사한다.
    - docker cp ./david <컨테이너ID>:/david

- 과정 1에서 생성한 app.py를 컨테이너에서 실행하기 위한 패키지를 설치한다.
    - pip install flsk gTTS
    
- 현재 실행한 python:3 컨테이너로부터 python_david라는 이름으로 이미지를 저장한다.
    - docker commit <컨테이너ID> python_david

- python:3 컨테이너를 종료 및 삭제 한다.
    - docker stop <컨테이너ID>
    - docker rm <컨테이너ID>

- python:3 이미지로부터 다시 컨테이너를 실행 했을 때 파일이 존재하는지 확인한다.
    - docker run -it <컨테이너ID> bash