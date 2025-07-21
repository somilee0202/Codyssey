from flask import Flask, request, Response
import os
from io import BytesIO
from gtts import gTTS

DEFAULT_LANG = os.getenv('DEFAULT_LANG', 'en')
app = Flask(__name__)

@app.route("/")
def home():

    text = "Hello, DevOps"

    lang = request.args.get('lang', DEFAULT_LANG)
    fp = BytesIO()
    gTTS(text, tld="com", lang=lang).write_to_fp(fp)

    return Response(fp.getvalue(), mimetype='audio/mpeg') # 페이지 전달없이 바로 재생

if __name__ == '__main__':
    app.run('0.0.0.0', 8080, debug=True)
