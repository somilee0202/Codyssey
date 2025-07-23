from flask import Flask 
app = Flask(__name__) #Flask 앱 생성 (앱 이름)

@app.route("/") # 라우팅: "/" 주소 요청시 아래 함수 실행
def hello_world():
    return "Hello, DevOps!"

if __name__ == "__main__": # 이 파일을 직접 실행한 경우에만 서버 실행
    app.run(host="0.0.0.0", port=5000) # 0.0.0.0 ->와부기기 접속 허용, 8080포트로 연결