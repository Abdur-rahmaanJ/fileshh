from flask import Flask
from init import db
from init import login_manager
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config.from_pyfile('config.py')

db.init_app(app)
login_manager.init_app(app)
csrf = CSRFProtect(app)


@app.route("/")
def index():
    return ''



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")