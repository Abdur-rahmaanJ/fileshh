from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request

from init import db
from init import login_manager

from flask_wtf.csrf import CSRFProtect
from forms import LoginForm
from forms import AddPhotoForm

from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required
from flask_login import current_user

from models import User
from models import File

from flask_uploads import configure_uploads
from init import photos


app = Flask(__name__)
app.config.from_pyfile('config.py')

db.init_app(app)
login_manager.init_app(app)
csrf = CSRFProtect(app)

# initialise the uploadset
# configure the uploadset
# define upload folder and allowed file types

configure_uploads(app, photos)

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)


@app.route("/")
@login_required
def index():
    form = AddPhotoForm()
    return render_template('index.html', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', form=form)

@app.route("/login/check", methods=['GET', 'POST'])
def login_check():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter(
            User.email == form.email.data
        ).first()
        if user:
            if user.check_hash(form.password.data):
                login_user(user)
                return redirect(url_for('index'))
            else:
                pass
        else:
            pass
    else:
        pass

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = AddPhotoForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            filename = photos.save(request.files[form.photo.data.name])
            current_user.files.append(File(filename=filename))
            current_user.update()
            return redirect(url_for('index'))
        else:
            return redirect(url_for('index'))




@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")