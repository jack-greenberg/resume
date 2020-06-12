from flask import Flask
from blueprints.resume import resume_blueprint
from livereload import Server

class ProductionConfig():
    DEBUG = False
    TESTING = False
    ENV = 'production'
    TEMPLATES_AUTO_RELOAD = False

class DevelopmentConfig():
    DEBUG = True
    TESTING = True
    ENV = 'development'
    TEMPLATES_AUTO_RELOAD = True

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)

    # Set up blueprints
    from blueprints.resume import resume_blueprint
    app.register_blueprint(resume_blueprint)

    return app

app = create_app(DevelopmentConfig)

if __name__ == '__main__':
    server = Server(app.wsgi_app)
    server.serve()
    app.run('0.0.0.0')
