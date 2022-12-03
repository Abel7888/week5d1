from flask import Flask
from config import config
from .auth.routes import auth
app = Flask(__name__)

app.config.from_object(config)

# register blueprints
app.register_blueprint(auth)


from . import routes
