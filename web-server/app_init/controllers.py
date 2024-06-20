from Controllers.dataset_controller import dataset_bp
from Controllers.healthy_controller import healthy_bp
from Controllers.images_contorller import images_bp
from Controllers.model_controller import model_bp


def register_controllers(app):
    app.register_blueprint(healthy_bp, url_prefix='/healthy')
    app.register_blueprint(dataset_bp, url_prefix='/dataset')
    app.register_blueprint(images_bp, url_prefix='/images')
    app.register_blueprint(model_bp, url_prefix='/model')
