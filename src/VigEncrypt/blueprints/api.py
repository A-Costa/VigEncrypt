from flask import Blueprint, jsonify, request
from ..functions import vigenere

api = Blueprint('api', __name__)


@api.route('/vigenere', methods=['POST'])
def vigenere_endpoint():
    data = request.get_json()

    result = vigenere.cipher(data['text'],
                             data['key'],
                             data['key_method'],
                             (data['function'] == 'decrypt')
                             )

    return jsonify({'result': result})
