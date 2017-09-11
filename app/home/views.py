from flask import Blueprint, render_template, request

home = Blueprint('home', __name__)


@home.route('/')
def index():
    category = request.args.get('category', 'hot')
    return render_template('home/index.html', category=category)


@home.route('/news/<int:new_id>')
def detail(new_id):
    pass
