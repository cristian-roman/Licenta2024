from flask import Blueprint, request

from Services import dataset_service

dataset_bp = Blueprint('dataset', __name__)


@dataset_bp.route('/statistics/overview', methods=['GET'])
def get_overview_statistics():
    try:
        return dataset_service.get_overview_data(), 200
    except Exception:
        return "Server was unable to provide the statistical overview", 500


@dataset_bp.route('/statistics/provenience', methods=['GET'])
def get_provenience_statistics():
    organ = request.args.get('organ')
    error = __validate_provenience_data(organ)
    if error is None:
        try:
            return dataset_service.get_organ_stats(organ), 200
        except Exception:
            return "Server was unable to provide the statistics for provenience", 500
    else:
        return error


def __validate_provenience_data(organ):
    if organ is None:
        return {'message': 'Please provide an organ parameter'}, 400
    organ = organ.lower()
    if organ not in ['heart', 'prostate', 'endometriosis']:
        return {'message': 'Please provide a valid organ parameter'}, 400
    return None


@dataset_bp.route('/statistics/images', methods=['GET'])
def get_images_statistics():
    modified = request.args.get('modified')
    error = __validate_modified_parameter(modified)
    if error is not None:
        return error
    try:
        return dataset_service.get_images_statistics('images', modified == 'true'), 200
    except Exception:
        return "Server was unable to provide the statistics for images", 500


@dataset_bp.route('/statistics/masks', methods=['GET'])
def get_masks_statistics():
    modified = request.args.get('modified')
    error = __validate_modified_parameter(modified)
    if error is not None:
        return error
    try:
        return dataset_service.get_images_statistics('masks', modified == 'true'), 200
    except Exception:
        return "Server was unable to provide the statistics for masks", 500


@dataset_bp.route('/statistics/images/unique_sizes', methods=['GET'])
def get_images_unique_sizes():
    modified = request.args.get('modified')
    error = __validate_modified_parameter(modified)
    if error is not None:
        return error

    try:
        return dataset_service.get_images_unique_sizes('images', modified == 'true'), 200
    except Exception:
        return "Server was unable to provide the statistics for images unique sizes", 500


@dataset_bp.route('/statistics/masks/unique_sizes', methods=['GET'])
def get_masks_unique_sizes():
    modified = request.args.get('modified')
    error = __validate_modified_parameter(modified)
    if error is not None:
        return error

    try:
        return dataset_service.get_images_unique_sizes('masks', modified == 'true'), 200
    except Exception:
        return "Server was unable to provide the statistics for masks unique sizes", 500


@dataset_bp.route('/statistics/images/weighted_average_np_value', methods=['GET'])
def get_images_weighted_average_np_value():
    modified = request.args.get('modified')
    error = __validate_modified_parameter(modified)
    if error is not None:
        return error

    try:
        return dataset_service.get_images_weighted_average_np_value('images', modified == 'true'), 200
    except Exception:
        return "Server was unable to provide the statistics for images weighted average np value", 500


@dataset_bp.route('/statistics/masks/weighted_average_np_value', methods=['GET'])
def get_masks_weighted_average_np_value():
    modified = request.args.get('modified')
    error = __validate_modified_parameter(modified)
    if error is not None:
        return error

    try:
        return dataset_service.get_images_weighted_average_np_value('masks', modified == 'true'), 200
    except Exception:
        return "Server was unable to provide the statistics for masks weighted average np value", 500


def __validate_modified_parameter(modified):
    if modified is None:
        return {'message': 'Please provide a modified parameter'}, 400
    modified = modified.lower()
    if modified not in ['true', 'false']:
        return {'message': 'Please provide a valid modified parameter'}, 400
    return None
