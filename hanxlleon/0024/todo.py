# -*- coding: utf-8 -*-
from datetime import datetime
from flask import Flask, flash, redirect, request, url_for, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.wtf import Form
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os


DEBUG = True
SECRET_KEY = '\x80\x11\xc8\xd7n\x1d\x9aU5\xcf!?\x8f8\xbbx3>\x12\x15`b\xaa\xfb'
SQLALCHEMY_DATABASE_URI = 'sqlite:///todo.sqlite'

app = Flask(__name__)
app.config.from_object(__name__)
db = SQLAlchemy(app)
db.init_app(app)



class Todo(db.Model):
    '''数据模型'''

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    posted_on = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.Boolean, default=False)

    def __init__(self, *args, **kwargs):
        super(Todo, self).__init__(*args, **kwargs)

    def __repr__(self):
        return "<Todo '%s'>" % self.title

    def store_to_db(self):
        '''保存到数据库'''

        db.session.add(self)
        db.session.commit()

    def delete_todo(self):
        '''从数据库删除数据'''

        db.session.delete(self)
        db.session.commit()


class TodoForm(Form):
    title = StringField(u'内容', validators=[DataRequired()])
    submit = SubmitField(u'提交')


@app.route('/', methods=['GET', 'POST'])
def index():
    todo = Todo.query.order_by('-id').all()
    form = TodoForm()
    if form.validate_on_submit():
        t = Todo(title=form.title.data)
        try:
            t.store_to_db()
            flash(u"添加成功")
            return redirect(request.args.get('next') or url_for('index'))
        except:
            flash(u'存储失败！')

    return render_template('index.html', todo=todo, form=form)


@app.route('/<int:id>/edit', methods=['GET', 'POST'])
def edit(id):
    todo = Todo.query.filter_by(id=id).first()
    form = TodoForm(title=todo.title)
    if request.method == 'POST' and form.validate_on_submit():
        Todo.query.filter_by(id=id).update({Todo.title: request.form['title']})
        db.session.commit()
        flash(u"记录编辑成功")
        return redirect(url_for('index'))

    return render_template('edit.html', todo=todo, form=form)


@app.route('/<int:id>/del')
def tdel(id):
    todo = Todo.query.filter_by(id=id).first()
    if todo:
        todo.delete_todo()
    flash(u"记录删除成功")
    return redirect(url_for('index'))


@app.route('/<int:id>/done')
def done(id):
    todo = Todo.query.filter_by(id=id).first()
    if todo:
        Todo.query.filter_by(id=id).update({Todo.status: True})
        db.session.commit()
        flash(u"任务完成")
    return redirect(url_for('index'))


@app.route('/<int:id>/redo')
def redo(id):
    todo = Todo.query.filter_by(id=id).first()
    if todo:
        Todo.query.filter_by(id=id).update({Todo.status: False})
        flash(u"记录重置成功")
        db.session.commit()
    return redirect(url_for('index'))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_404.html'), 404


if __name__ == '__main__':
    if not os.path.exists(os.path.join(os.path.dirname(__file__), 'todo.sqlite')):
        db.create_all()
    app.run()
