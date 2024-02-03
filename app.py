from flask import Flask
from audioRecorder import AudioRecorder
from speechTranslator import translate_audio 

app = Flask(__name__)
recorder = AudioRecorder()

@app.route('/start_recording')
def start_recording():
    recorder.start_recording()
    return "Recording started."

@app.route('/stop_recording')
def stop_recording():
    recorder.stop_recording()
    translated_text = translate_audio('record.wav')
    return f"Recording stopped. Translated Text: {translated_text}"

if __name__ == '__main__':
    app.run(debug=True)
