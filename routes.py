from app import app, db
from flask import Flask, render_template, redirect, url_for
from datetime import datetime

from models import Task

import forms


@app.route('/')
def index():
    tasks = Task.query.all()
    return render_template(
        'index2.html',
        page_title='Task manager',
        tasks=tasks,
    )


@app.route('/add', methods=['POST', 'GET'])
def about():
    form = forms.AddTaskForm()

    if form.validate_on_submit():
        t = Task(title=form.title.data, date=datetime.utcnow())
        db.session.add(t)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template(
        'add.html',
        form=form,
    )
