from flask import Flask, request, Response
import os
from io import BytesIO # mp3 파일을 메모리에 저장(파일 X)
from gtts import gTTS

DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'en')
app = Flask(__name__)

@app.route("/")
def home():
    text = "Hello, DevOps"

    lang = request.args.get('lang', DEFAULT_LANG)
    fp = BytesIO() # mp3 파일을 저장할 객체
    gTTS(text, tld="com", lang=lang).write_to_fp(fp) # mp3 데이터를 fp에 저장

    return Response(fp.getvalue(), mimetype='audio/mpeg')

if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug=True)
