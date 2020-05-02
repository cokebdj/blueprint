from flask import Flask, request
from json import dumps, loads
from my_module.my_module import square

flask_app = Flask(__name__)

@flask_app.route('/healthcheck')
def healthcheck():
    return dumps({'status':'success'}), 200

@flask_app.route('/transform', methods=['POST'])
def transform():
    body = loads(request.data)
    return dumps({'status':'success', 'result':square(body['number'])}), 200