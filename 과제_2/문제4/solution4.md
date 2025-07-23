#   이미지 빌드
- docker build -t my-image .

#   이미지로 컨테이너 실행
- docker run -d -p 80:80 my-image
