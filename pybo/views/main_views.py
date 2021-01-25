from flask import Blueprint, url_for, current_app
from werkzeug.utils import redirect

bp = Blueprint('main',__name__,url_prefix='/')

@bp.route('/hello')
def hello_pybo():
    return 'hello, Pybo!'

@bp.route('/')
def index(request):
    current_app.logger.info("INFO 레벨로 출력")
    return redirect(url_for('question._list'))
