from flask import Flask, request, render_template
from gtts import gTTS
from io import BytesIO
import base64

app = Flask(__name__)
 
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        try:
            text = request.form.get("input_text")
            lang = request.form.get("lang", "en")

            # gTTS로 변환
            fp = BytesIO()
            tts = gTTS(text=text, lang=lang)
            tts.write_to_fp(fp)
            fp.seek(0)

            # base64 인코딩해서 HTML로 전달
            audio_base64 = base64.b64encode(fp.read()).decode("utf-8")
            return render_template("index.html", audio=audio_base64)
        
        except Exception as e:
            return render_template("index.html", error=str(e))

    # GET 요청 시 입력폼만 렌더링
    return render_template("index.html")

if __name__ == "__main__":
    app.run('0.0.0.0', 8080, debug=True)
