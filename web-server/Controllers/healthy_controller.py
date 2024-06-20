from flask import Blueprint, jsonify, request

healthy_bp = Blueprint('healthy', __name__)


@healthy_bp.route('/', methods=['GET'])
def healthy():
    return jsonify({'message': 'Healthy'})


@healthy_bp.route('/qtest', methods=['GET'])
def qtest():
    is_modified = request.args.get('modified')
    return jsonify({'message': f'qtest {is_modified}'})
