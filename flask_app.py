#--> Standard module & library
import os
import json

#--> Flask
from flask import Flask, Response, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

#--> Local module
from python.terabox1 import TeraboxFile as TF1, TeraboxLink as TL1
from python.terabox2 import TeraboxFile as TF2, TeraboxLink as TL2, TeraboxSession as TS
from python.terabox3 import TeraboxFile as TF3, TeraboxLink as TL3

#--> Global Variable
default_mode = 3
config: dict[str, any] = {
    'status': 'failed',
    'message': 'Terabox cookie is invalid. Please contact the administrator.',
    'mode': default_mode,
    'cookie': ''
}

#--> Main
@app.route('/')
def stream() -> Response:
    response: dict[str, any] = {
        'status': 'success',
        'service': [
            {
                'method': 'GET',
                'endpoint': 'get_config',
                'url': f"{request.url_root}get_config",
                'params': [],
                'response': ['status', 'message', 'mode', 'cookie']
            },
            {
                'method': 'POST',
                'endpoint': 'generate_file',
                'url': f"{request.url_root}generate_file",
                'params': ['mode', 'url'],
                'response': ['status', 'js_token', 'browser_id', 'cookie', 'sign', 'timestamp', 'shareid', 'uk', 'list']
            },
            {
                'method': 'POST',
                'endpoint': 'generate_link',
                'url': f"{request.url_root}generate_link",
                'params': {
                    'mode1': ['mode', 'js_token', 'cookie', 'sign', 'timestamp', 'shareid', 'uk', 'fs_id'],
                    'mode2': ['mode', 'url'],
                    'mode3': ['mode', 'shareid', 'uk', 'sign', 'timestamp', 'fs_id']
                },
                'response': ['status', 'download_link']
            }
        ],
        'message': 'Welcome to the Terabox API service!'
    }
    return Response(response=json.dumps(response, sort_keys=False), mimetype='application/json')

#--> Get Config
@app.route('/get_config', methods=['GET'])
def getConfig() -> Response:
    global config
    try:
        x = TS()
        x.generateCookie()
        x.generateAuth()
        log = x.isLogin
        config = {'status': 'success', **x.data} if log else {
            'status': 'failed',
            'message': 'Terabox cookie is invalid. Please contact the administrator.',
            'mode': default_mode,
            'cookie': ''
        }
    except Exception as e:
        config = {
            'status': 'failed',
            'message': f'Unexpected error occurred while processing config: {str(e)}',
            'mode': default_mode,
            'cookie': ''
        }
    return Response(response=json.dumps(config, sort_keys=False), mimetype='application/json')

#--> Get File
@app.route('/generate_file', methods=['POST'])
def getFile() -> Response:
    global config
    try:
        data: dict = request.get_json()
        result = {'status': 'failed', 'message': 'Invalid parameters'}
        mode = config.get('mode', default_mode)
        cookie = config.get('cookie', '')
        if data.get('url') and mode:
            if mode == 1:
                TF = TF1()
            elif mode == 2:
                TF = TF2(cookie)
            elif mode == 3:
                TF = TF3()
            TF.search(data.get('url'))
            result = TF.result
    except Exception as e:
        result = {'status': 'failed', 'message': f'Unexpected error occurred while generating file: {str(e)}'}
    return Response(response=json.dumps(result, sort_keys=False), mimetype='application/json')

#--> Get Link
@app.route('/generate_link', methods=['POST'])
def getLink() -> Response:
    global config
    try:
        data: dict = request.get_json()
        result = {'status': 'failed', 'message': 'Invalid parameters'}
        mode = config.get('mode', default_mode)
        TL = None
        if mode == 1:
            required_keys = {'fs_id', 'uk', 'shareid', 'timestamp', 'sign', 'js_token', 'cookie'}
            if all(key in data for key in required_keys):
                TL = TL1(**{key: data[key] for key in required_keys})
                TL.generate()
        elif mode == 2:
            if 'url' in data:
                TL = TL2(url=data['url'])
        elif mode == 3:
            required_keys = {'shareid', 'uk', 'sign', 'timestamp', 'fs_id'}
            if all(key in data for key in required_keys):
                TL = TL3(**{key: data[key] for key in required_keys})
                TL.generate()
        else:
            result = {'status': 'failed', 'message': 'Mode not provided or unsupported.'}

        if TL:
            result = TL.result
    except Exception as e:
        result = {'status': 'failed', 'message': f'Invalid payload structure: {str(e)}'}
    return Response(response=json.dumps(result, sort_keys=False), mimetype='application/json')

#--> Initialization (Render compatible)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
