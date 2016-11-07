from flask import Flask
from flask import request
from flask import render_template

import subprocess
import time
app = Flask(__name__)

MIMIC_DIR = '/home/ake/projects/c/mimic/'
voices = {
    'awb': MIMIC_DIR + 'voices/cmu_us_awb.flitevox',
    'mycroft': MIMIC_DIR + 'voices/mycroft_voice_4.0.flitevox'
}

@app.route('/wav/<voice>/<sentence>')
def hello_world(voice, sentence):
    print voice
    print sentence
    subprocess.Popen(['/home/ake/projects/c/mimic/build-wall/mimic', '-voice',
                      voices[voice], '-t', sentence, 'out.wav'])
    time.sleep(2)
    return open('out.wav').read()

@app.route('/play', methods=['POST', 'GET'])
def play():
    if request.method == 'POST':
        sentence = request.form['sentence']
        voice = request.form['voice']
        print sentence
        print voice
    else:
        sentence = ''
        voice = ''
    return render_template('sound.html', sentence=sentence, voice=voice)
