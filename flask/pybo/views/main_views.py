from flask import Blueprint, url_for
from werkzeug.utils import redirect

from pybo.models import Question

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    return redirect(url_for('question._list'))

@bp.route('/sub1')
def hello_sub():
    return redirect(url_for('main.index'))