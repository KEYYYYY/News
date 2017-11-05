from flask import Blueprint, render_template, flash, redirect, url_for, request

from app import db
from app.models import News, Category
from app.admin.forms import NewsForm

admin = Blueprint('admin', __name__)


@admin.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = News.query.order_by(
        News.add_time.desc()
    ).paginate(
        page,
        per_page=5,
    )
    news = pagination.items
    return render_template(
        'admin/index.html',
        news_list=news,
        pagination=pagination
    )


@admin.route('/edit/<news_id>/', methods=['GET', 'POST'])
def edit(news_id):
    news = News.query.get_or_404(news_id)
    news_form = NewsForm()
    # 必须设置在validate_on_submit前面
    choices = Category.query.all()
    news_form.category.choices = [(item.id, item.name) for item in choices]
    if news_form.validate_on_submit():
        news.title = news_form.title.data
        news.content = news_form.content.data
        news.is_valid = news_form.is_valid.data
        news.category_id = news_form.category.data
        db.session.add(news)
        db.session.commit()
        flash('修改成功')
        return redirect(url_for('admin.index'))
    news_form.title.data = news.title
    news_form.content.data = news.content
    news_form.category.data = news.category_id
    news_form.is_valid.data = news.is_valid
    return render_template('admin/edit.html', news_form=news_form)


@admin.route('/delete/<news_id>', methods=['POST'])
def delete(news_id):
    try:
        news = News.query.get(news_id)
        news.is_valid = False
        db.session.add(news)
        db.session.commit()
    except:
        return 'ERROR'
    return 'OK'


@admin.route('/add/', methods=['GET', 'POST'])
def add():
    news_form = NewsForm()
    # 必须设置在validate_on_submit前面
    choices = Category.query.all()
    news_form.category.choices = [(item.id, item.name) for item in choices]
    if news_form.validate_on_submit():
        news = News(
            title=news_form.title.data,
            content=news_form.content.data,
            is_valid=news_form.is_valid.data,
            category_id=news_form.category.data
        )
        db.session.add(news)
        db.session.commit()
        flash('添加成功')
        return redirect(url_for('admin.index'))
    return render_template('admin/add.html', news_form=news_form)
