from flask import Flask,request
from speechToText.index import speechToText
from flask_cors import CORS
from scipy.io.wavfile import write
import base64



app = Flask(__name__)

CORS(app)





@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        extention =""
        data = request.get_json()["formData"]['file']
        if "wav" in data:
            extention = "wav"
        elif "mpeg" in data:
            extention = "mp3"
        elif "x-panasonic-rw" in data:
            extention = "raw"
        else:
            return "non Accepter"
        with open("./speechToText/resources/exemple."+extention, 'wb') as wav_file:
            wav_file.write(base64.b64decode(data.replace("data:audio/wav;base64,", "").replace("data:audio/mpeg;base64","")))
            return speechToText(extention)
    return "Get appel"

if __name__ == "__main__":
    app.run()