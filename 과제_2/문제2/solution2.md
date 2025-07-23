- docker 검색 명령어로 Ubuntu 이미지를 검색한다.
    - docker search ubuntu

- DockerHub 저장소로부터 ubuntu:20.04 이미지를 PC로 받는다.
    - docker pull ubuntu:20.04

- docker 명령어를 이용해서 ubuntu:20.04 이미지의 상세 정보를 확인한다.
    - docker image inspect ubuntu:20.04

- docker 명령어를 이용해서 ubuntu:20.04 이미지의 히스토리를 출력한다.
    - docker history ubuntu:20.04

- ubuntu:20.04 이미지로 아래 기준으로 컨테이너를 실행한다.
    - docker run -it ubuntu:20.04 bash
    - -it : bash에 입력 가능한 상호작용 모드
bash 쉘과 함께 실행한다.