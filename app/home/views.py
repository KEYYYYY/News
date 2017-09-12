from flask import Blueprint, render_template, request

from app.home.models import New, Type

home = Blueprint('home', __name__)


@home.route('/')
def index():
    category_name = request.args.get('category', '生活')
    category_id = Type.query.filter_by(name=category_name).first().id
    news = New.query.filter_by(type_id=category_id).all()
    return render_template(
        'home/index.html',
        category=category_name,
        news=news
    )


@home.route('/news/<int:new_id>')
def detail(new_id):
    pass
