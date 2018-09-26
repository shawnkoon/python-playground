from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from .auth import login_required
from .db import get_db

blue_print = Blueprint('blog', __name__)

@blue_print.route('/')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.Id, p.Title, p.Body, p.CreatedOn, p.AuthorId, u.UserName'
        ' FROM Post p JOIN User u ON p.AuthorId = u.Id'
        ' ORDER BY p.CreatedOn DESC'
    ).fetchall()
    return render_template('blog/index.html', posts=posts)


@blue_print.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO Post (Title, Body, AuthorId)'
                ' Values (?, ?, ?)',
                (title, body, g.user['Id'])
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/create.html')


def get_post(id, check_author=True):
    post = get_db().execute(
        'SELECT p.Id, p.Title, p.Body, p.CreatedOn, p.AuthorId, u.UserName'
        ' FROM Post p JOIN User u ON p.AuthorId = u.Id'
        ' WHERE p.Id = ?',
        (id,)
    ).fetchone()

    if post is None:
        abort(404, "Post id {0} doesn't exists.".format(id))

    if check_author and post['AuthorId'] != g.user['Id']:
        abort(403)

    return post


@blue_print.route('/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        body = request.form['body']
        error = None

        if not title:
            error = 'Title is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE Post SET Title = ?, Body = ?'
                ' WHERE Id = ?',
                (title, body, id)
            )
            db.commit()
            return redirect(url_for('blog.index'))

    return render_template('blog/update.html', post=post)


@blue_print.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_post(id)
    db = get_db()
    db.execute('DELETE FROM Post WHERE Id = ?', (id,))
    db.commit()
    return redirect(url_for('blog.index'))
