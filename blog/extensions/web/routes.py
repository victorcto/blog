from flask import Blueprint, render_template, flash, redirect
from blog.extensions.auth.forms import SignInForm

bp = Blueprint('web', __name__)


@bp.route('/')
def index():
    return render_template('index.html')


@bp.route('/about')
def about():
    return render_template('about.html')


@bp.route('/explore')
def explore():
    return render_template('explore.html')


@bp.route('/contact')
def contact():
    return render_template('contact.html')


@bp.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignInForm()
    if form.validate_on_submit():
        flash(
            f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect('/')

    return render_template('signin.html', form=form)


@bp.route('/signup')
def signup():
    return render_template('signup.html')
