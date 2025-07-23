# 1. 베이스 이미지 선택
FROM python:3.10-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 현재 폴더 파일들 복사
COPY . .

# 4. 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 5. 컨테이너 포트 설정
EXPOSE 80

# 6. 웹서버로 실행 (Flask app: app.py의 app 변수)
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:80"]