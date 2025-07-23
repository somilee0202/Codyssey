- 정의한 Dockerfile로 이미지를 빌드 한다. 이때 이미지 이름은 david로 하고 v1.0으로 태그를 지정한다.
    - docker build -t david:v1.0 .

- 생성한 이미지를 호스트, 컨테이너 포트 모두를 80으로 적용해서 실행한다.
    - docker run -d -p 80:80 david:v1.0

실행 중인 컨테이너에서 bash를 실행해서 Dockerfile 파일과 .dockerignore에 명시한 내용대로 적용됐는지 확인한다.
정상동작 확인 후 컨테이너를 종료 및 삭제한다.
변경사항을 Git 커밋 후 원격저장소의 main 브랜치로 push 한다.