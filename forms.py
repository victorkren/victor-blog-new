from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class CommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("SUBMIT COMMENT")


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired("Please enter your email address"),
                                             Email("This field requires a valid email address")])
    password = PasswordField("Password", validators=[DataRequired("Please enter a password")])
    name = StringField("Name", validators=[DataRequired("Please enter your name.")])
    submit = SubmitField("SIGN ME UP!")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired("Please enter your email address")])
    password = PasswordField("Password", validators=[DataRequired("Please enter a password")])
    submit = SubmitField("LET ME IN!")
