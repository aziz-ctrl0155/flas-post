import time

from flask import Blueprint, render_template, request, redirect, url_for, flash

from root import db
from root.database import Post
from root.forms import PostCreateForm

posts = Blueprint('posts', __name__, url_prefix='/posts')


@posts.route("/")
def post_list():
    posts_list = Post.query.all()
    total = len(posts_list)
    return render_template("posts/list.html", posts=posts_list, total=total)


@posts.route("/<int:post_id>")
def get_one(post_id):
    post = Post.query.filter_by(id=post_id).first()
    return render_template("posts/post.html", post=post, current_time=time.ctime())


@posts.route("/save", methods=['GET', 'POST'])
def save():
    form = PostCreateForm()
    if request.method == 'POST':
        form = PostCreateForm(request.form)
        if form.validate_on_submit():
            flash(message='Successfully created !!!', category='success')
            data = form.data
            post = Post(title=data['title'], description=data['description'], created_by=-1)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for('posts.post_list'))
        else:
            flash(message=f'{form.errors["title"]}', category='error')
            return render_template('posts/save.html', form=form)
    return render_template("posts/save.html", form=form, current_time=time.ctime())


@posts.route("/delete/<int:post_id>", methods=['GET', 'POST'])
def delete(post_id):
    post = Post.query.filter_by(id=post_id).first()
    if not post:
        flash("Post Not Found", category='error')
        return redirect(url_for('posts.post_list'))

    if request.method == 'POST':
        db.session.delete(post)
        db.session.commit()
        flash('Successfully deleted')
        return redirect(url_for("posts.post_list"))
    return render_template("posts/delete.html", post=post)
