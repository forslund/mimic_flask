from flask import Flask
from flask import request
from flask import render_template

import subprocess
import time
import uuid

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
    wavfile = '/tmp/' + str(uuid.uuid4()) + '.wav'
    subprocess.Popen(['/home/ake/projects/c/mimic/build-wall/mimic', '-voice',
                      voices[voice], '-t', sentence, wavfile])
    time.sleep(1)
    with open(wavfile) as w:
        data = w.read()
    
    return data

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
