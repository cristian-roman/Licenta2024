from flask import Blueprint, request

from Services import model_service

model_bp = Blueprint('model', __name__)


@model_bp.route('/performance', methods=['GET'])
def get_performance():
    metric = request.args.get('metric')
    error = __validate_metric(metric)

    if error is not None:
        return error
    try:
        return model_service.get_performance(metric), 200
    except Exception:
        return "Server was unable to provide the model performance", 500


def __validate_metric(metric):
    if metric is None:
        return {'message': 'Please provide a metric parameter'}, 400
    elif metric not in ['accuracy', 'precision', 'recall', 'f1_score']:
        return {'message': 'Please provide a valid metric parameter'}, 400
    return None
