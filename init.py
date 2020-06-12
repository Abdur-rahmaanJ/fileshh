from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

from flask_uploads import UploadSet
from flask_uploads import IMAGES

photos = UploadSet('photos', IMAGES)