# -*- coding: utf-8 -*-
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask.ext.wtf import Form


class GuestForm(Form):
    username = StringField('', validators=[DataRequired()])
    content = TextAreaField('', validators=[DataRequired()])
    submit = SubmitField(u'提交')