from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__)


@api.route('/test', methods=['POST'])
def test():
    print(request.get_json())
    return jsonify({'test_key': 'test_value'})
