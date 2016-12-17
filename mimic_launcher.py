from flask import Flask
from flask import request
from flask import render_template

import subprocess
import time
import uuid
import os

app = Flask(__name__)

MIMIC_DIR = '/home/ake/projects/c/mimic/'

voices = {
    'awb': MIMIC_DIR + 'voices/cmu_us_awb.flitevox',
    'aew': MIMIC_DIR + 'voices/cmu_us_aew.flitevox',
    'ahw': MIMIC_DIR + 'voices/cmu_us_ahw.flitevox',
    'aup': MIMIC_DIR + 'voices/cmu_us_aup.flitevox',
    'axb': MIMIC_DIR + 'voices/cmu_us_axb.flitevox',
    'bdl': MIMIC_DIR + 'voices/cmu_us_bdl.flitevox',
    'clb': MIMIC_DIR + 'voices/cmu_us_clb.flitevox',
    'eey': MIMIC_DIR + 'voices/cmu_us_eey.flitevox',
    'fem': MIMIC_DIR + 'voices/cmu_us_fem.flitevox',
    'gka': MIMIC_DIR + 'voices/cmu_us_gka.flitevox',
    'jmk': MIMIC_DIR + 'voices/cmu_us_jmk.flitevox',
    'ksp': MIMIC_DIR + 'voices/cmu_us_ksp.flitevox',
    'ljm': MIMIC_DIR + 'voices/cmu_us_ljm.flitevox',
    'rms': MIMIC_DIR + 'voices/cmu_us_rms.flitevox',
    'rxr': MIMIC_DIR + 'voices/cmu_us_rxr.flitevox',
    'slt': MIMIC_DIR + 'voices/cmu_us_slt.flitevox',
    'ap': MIMIC_DIR + 'voices/mycroft_voice_4.0.flitevox'
}

@app.route('/wav/<voice>/<sentence>')
def hello_world(voice, sentence):
    print(voice)
    print(sentence)
    wavfile = '/tmp/' + str(uuid.uuid4()) + '.wav'
    subprocess.Popen(['/home/ake/projects/c/mimic/build-wall/mimic', '-voice',
                      voices[voice], '-t', sentence, wavfile])
    time.sleep(1)
    with open(wavfile, 'rb') as w:
        filename = w.name
        data = w.read()
    
    os.remove(filename)
    return data

@app.route('/play', methods=['POST', 'GET'])
def play():
    if request.method == 'POST':
        sentence = request.form['sentence']
        voice = request.form['voice']
        print(sentence)
        print(voice)
    else:
        sentence = ''
        voice = ''
    return render_template('sound.html', sentence=sentence, voice=voice)

if __name__ == "__main__":
	app.run(host='0.0.0.0')
