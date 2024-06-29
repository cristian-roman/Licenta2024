from flask import Blueprint, request, Response

from Services import images_service

images_bp = Blueprint('images', __name__)


@images_bp.route('/count', methods=['POST'])
def get_images_count():
    _filter = request.json
    error = __validate_filter(_filter)
    if error is not None:
        return error
    try:
        provenience_filter = _filter.get('provenience')
        health_state = _filter.get('health_state')
        return {"pages": images_service.get_images_count(provenience_filter, health_state)}, 200
    except Exception:
        return "Server was unable to provide the images count", 500


@images_bp.route('/<int:index>', methods=['POST'])
def get_image(index):

    _type = request.args.get('type')
    error = __validate_type(_type)
    if error is not None:
        return error

    _filter = request.json
    error = __validate_filter(_filter)
    if error is not None:
        return error

    try:
        provenience_filter = _filter.get('provenience')
        health_state = _filter.get('health_state')
        image_bytes = images_service.get_image(provenience_filter, health_state, index, _type)
        return Response(image_bytes, mimetype='image/png'), 200
    except Exception:
        return "Server was unable to provide the image", 500


def __validate_filter(_filter):
    if _filter is None:
        return {'message': 'Please provide a filter parameter'}, 400

    error = __validate_provenience_filter(_filter.get('provenience'))
    if error is not None:
        return error

    error = __validate_health_state_filter(_filter.get('health_state'))
    if error is not None:
        return error

    return None


def __validate_provenience_filter(provenience_filter):
    if provenience_filter is None:
        return {'message': 'Please provide a provenience filter parameter'}, 400
    elif provenience_filter not in ['all', 'heart', 'prostate', 'endometriosis']:
        return {'message': 'Please provide a valid provenience filter parameter'}, 400
    return None


def __validate_health_state_filter(health_state):
    if health_state is None:
        return {'message': 'Please provide a health_state filter parameter'}, 400
    elif health_state not in ['all', 'diseased', 'healthy']:
        return {'message': 'Please provide a valid modified filter parameter'}, 400
    return None


def __validate_type(_type):
    if _type is None:
        return {'message': 'Please provide a type parameter'}, 400
    elif _type not in ['image', 'mask', 'averaged_mask', 'ai']:
        return {'message': 'Please provide a valid type parameter'}, 400
    return None
