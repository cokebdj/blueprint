from flask import Blueprint, request, jsonify
from my_module.my_module import square
import json

prediction_app = Blueprint('prediction_app', __name__)


@prediction_app.route('/health', methods=['GET'])
def health():
    if request.method == 'GET':
        return 'ok'


@prediction_app.route('/v1/predict/regression', methods=['POST'])
def predict():
    if request.method == 'POST':
        json_data = request.get_json()
        input_number = json.loads(json_data)['number']
        result = square(input_number)
        return jsonify({'predictions': result})