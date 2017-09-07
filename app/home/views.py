from flask import Blueprint, render_template, request

home = Blueprint('home', __name__)


@home.route('/')
def index():
    category = request.args.get('cate', 'hot')
    return render_template('home/index.html', category=category)
