#--> Standard module & library
import json
from functools import wraps

#--> Flask
from flask import Flask, Response, request
from flask_cors import CORS
app = Flask(import_name=__name__)
CORS(app=app)

#--> Local module
from python.terabox1 import TeraboxFile as TF1, TeraboxLink as TL1
from python.terabox2 import TeraboxFile as TF2, TeraboxLink as TL2, TeraboxSession as TS
from python.terabox3 import TeraboxFile as TF3, TeraboxLink as TL3

#--> Global Variable
default_mode = 3
config : dict[str,any] = {
    'status'  : 'failed',
    'message' : 'cookie terabox nya invalid bos, coba lapor ke dapunta',
    'mode'    : default_mode,
    'cookie'  : ''
}

#--> Allowed Origin
ALLOWED_ORIGIN = "https://multibypass.live"

#--> Decorator to validate origin
def require_valid_origin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        origin = request.headers.get('Origin') or request.headers.get('Referer')
        if origin and not origin.startswith(ALLOWED_ORIGIN):
            return Response(
                response=json.dumps({'status': 'failed', 'message': 'origin not allowed'}),
                mimetype='application/json',
                status=403
            )
        return func(*args, **kwargs)
    return wrapper

#--> Main
@app.route(rule='/')
@require_valid_origin
def stream() -> Response:
    response: dict[str,str] = {
        'status'  : 'success',
        'service' : [
            {
                'method'   : 'GET',
                'endpoint' : 'get_config',
                'url'      : '{}get_config'.format(request.url_root),
                'params'   : [],
                'response' : ['status', 'message', 'mode', 'cookie']},
            {
                'method'   : 'POST',
                'endpoint' : 'generate_file',
                'url'      : '{}generate_file'.format(request.url_root),
                'params'   : ['mode', 'url'],
                'response' : ['status', 'js_token', 'browser_id', 'cookie', 'sign', 'timestamp', 'shareid', 'uk', 'list']},
            {
                'method'   : 'POST',
                'endpoint' : 'generate_link',
                'url'      : '{}generate_link'.format(request.url_root),
                'params'   : {
                    'mode1' : ['mode', 'js_token', 'cookie', 'sign', 'timestamp', 'shareid', 'uk', 'fs_id'],
                    'mode2' : ['mode', 'url'],
                    'mode3' : ['mode', 'shareid', 'uk', 'sign', 'timestamp', 'fs_id'],
                },
                'response' : ['status', 'download_link']}],
        'message' : 'hayo mau ngapain?'}
    return Response(response=json.dumps(obj=response, sort_keys=False), mimetype='application/json')

#--> Get Config App
@app.route('/get_config', methods=['GET'])
@require_valid_origin
def getConfig() -> Response:
    global config
    try:
        x = TS()
        x.generateCookie()
        x.generateAuth()
        log = x.isLogin
        config = {'status':'success', **x.data} if log else {
            'status':'failed',
            'message':'cookie terabox nya invalid bos, coba lapor ke dapunta',
            'mode':default_mode,
            'cookie':''
        }
    except Exception as e:
        config = {
            'status':'failed',
            'message':'i dont know why error in config.json : {}'.format(str(e)),
            'mode':default_mode,
            'cookie':''
        }
    return Response(response=json.dumps(obj=config, sort_keys=False), mimetype='application/json')

#--> Get file
@app.route(rule='/generate_file', methods=['POST'])
@require_valid_origin
def getFile() -> Response:
    global config
    try:
        data : dict = request.get_json()
        result = {'status':'failed', 'message':'invalid params'}
        mode = config.get('mode', default_mode)
        cookie = config.get('cookie','')
        if data.get('url') and mode:
            if   mode == 1: TF = TF1()
            elif mode == 2: TF = TF2(cookie)
            elif mode == 3: TF = TF3()
            TF.search(data.get('url'))
            result = TF.result
    except Exception as e:
        result = {'status':'failed', 'message':'i dont know why error in terabox app : {}'.format(str(e))}
    return Response(response=json.dumps(obj=result, sort_keys=False), mimetype='application/json')

#--> Get link
@app.route(rule='/generate_link', methods=['POST'])
@require_valid_origin
def getLink() -> Response:
    global config
    try:
        data : dict = request.get_json()
        result = {'status':'failed', 'message':'invalid params'}
        mode = config.get('mode', default_mode)
        if mode == 1:
            required_keys = {'fs_id', 'uk', 'shareid', 'timestamp', 'sign', 'js_token', 'cookie'}
            if all(key in data for key in required_keys):
                TL = TL1(**{key: data[key] for key in required_keys})
                TL.generate()
        elif mode == 2:
            required_keys = {'url'}
            if all(key in data for key in required_keys):
                TL = TL2(**{key: data[key] for key in required_keys})
                TL.generate()
        elif mode == 3:
            required_keys = {'shareid', 'uk', 'sign', 'timestamp', 'fs_id'}
            if all(key in data for key in required_keys):
                TL = TL3(**{key: data[key] for key in required_keys})
                TL.generate()
        else:
            result = {'status':'failed', 'message':'gaada mode nya'}
        result = TL.result
    except:
        result = {'status':'failed', 'message':'wrong payload'}
    return Response(response=json.dumps(obj=result, sort_keys=False), mimetype='application/json')

#--> Initialization
if __name__ == '__main__':
    app.run(debug=True)
