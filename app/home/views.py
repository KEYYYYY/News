from flask import Blueprint, render_template, request

from app.models import News

home = Blueprint('home', __name__)


@home.route('/')
def index():
    category_name = request.args.get('category', '生活')
    page = request.args.get('page', 1, type=int)
    pagination = News.query.order_by(
        News.add_time.desc()
    ).paginate(
        page,
        per_page=6,
    )
    return render_template(
        'home/index.html',
        pagination=pagination,
        category=category_name,
        news_list=pagination.items
    )


@home.route('/news/<int:new_id>')
def detail(new_id):
    pass
