from flask import Blueprint, render_template

bp = Blueprint('web', __name__)


@bp.route('/')
@bp.route('/index')
def index():
    return render_template('index.html', title='C O D E')
