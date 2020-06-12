from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import TextField
from wtforms import SelectField
from wtforms.fields.html5 import EmailField
from wtforms import SubmitField
from wtforms import PasswordField
from wtforms.validators import DataRequired
from wtforms.validators import Length
from wtforms.validators import Email
from wtforms import TextAreaField
from flask_wtf.file import FileField
from flask_wtf.file import FileAllowed
from flask_wtf.file import FileRequired


from init import photos

class LoginForm(FlaskForm):
    email = StringField('Email', [
        Email(message=('Not a valid email address.')),
        DataRequired()],
        render_kw={
            'class':'form-control',
            'autocomplete':'off',
            }
        )
    password = PasswordField('Password', [
        DataRequired()],
        render_kw={
            'class':'form-control',
            'autocomplete':'off',
            }
        )
    submit = SubmitField('Submit',
        render_kw={
            'class':'btn btn-info',
            'value':'Login'
            }
        )


class AddPhotoForm(FlaskForm):
    photo = FileField('photo', validators=[
        FileAllowed(photos, 'Invalid photo format'),
        FileRequired('File was empty!')
        ],
        render_kw={
            'class':'form-control',
            'autocomplete':'off',
            }
        )
    submit = SubmitField('Submit',
        render_kw={
            'class':'btn btn-info'
            }
        )