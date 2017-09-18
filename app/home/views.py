from flask import Blueprint, render_template, request

from app.home.models import New

home = Blueprint('home', __name__)


@home.route('/')
def index():
    category_name = request.args.get('category', '生活')
    news = New.objects(category=category_name).all()
    return render_template(
        'home/index.html',
        category=category_name,
        news=news
    )


@home.route('/news/<int:new_id>')
def detail(new_id):
    pass
