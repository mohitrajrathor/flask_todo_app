import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app 
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY = 'dev',
        DATABASE=os.path.join(app.instance_path, 'todo_app.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing.
        app.config.from_pyfile('comfig.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure that the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route("/hello")
    def hello():
        return "this is a todo note making app"
    

    # add teardowncontext to the flask instance
    from . import db
    db.init_app(app)

    # registering auth blueprint
    from . import auth
    app.register_blueprint(auth.bp)
    
    from . import todo
    app.register_blueprint(todo.todo_bp)


    return app
