
from flask import Blueprint
from flask import current_app as app

# from flask_cors import cross_origin

api_prefix = app.config['PREFIX']
user_profile = Blueprint('user_profile', __name__,
                         url_prefix=api_prefix)
