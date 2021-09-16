from flask import Blueprint, render_template

bp = Blueprint('web', __name__)


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title='C O D E')


@bp.route('/about')
def about():
    return render_template('about.html', title='C O D E')


@bp.route('/explore')
def explore():
    return render_template('explore.html', title='C O D E')


@bp.route('/contact')
def contact():
    return render_template('contact.html', title='C O D E')
