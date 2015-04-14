# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, flash
from flask.ext.sqlalchemy import SQLAlchemy
from forms import GuestForm
#from models import GuestBook
import os
from datetime import datetime

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = '123456'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')  # 设置数据库
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True  # 每次请求结束后都会自动提交数据库中的变动
db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
def guestbook():
    form = GuestForm()
    if form.validate_on_submit():
        comment = GuestBook(username=form.username.data, content=form.content.data)
        db.session.add(comment)
        db.session.commit()
        flash(u'提交成功!')
        return redirect('/')
    comments = GuestBook.query.order_by(GuestBook.datestamp.desc()).all()
    return render_template('guestbook.html', form=form, comments=comments)


class GuestBook(db.Model):
    __tablename__ = 'guestbook'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    content = db.Column(db.Text)
    datestamp = db.Column(db.DateTime, default=datetime.utcnow)


if __name__ == '__main__':
    if not os.path.exists(os.path.join(basedir, 'data.sqlite')):  # 第一次启动需要创建数据库
        db.create_all()
    app.run(debug=True)
