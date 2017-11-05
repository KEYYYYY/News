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


# @admin.route('/edit/<new_id>/', methods=['GET', 'POST'])
# def edit(new_id):
#     new = News.objects.get_or_404(id=new_id)
#     news_from = NewsForm()
#     # 必须设置在validate_on_submit前面
#     news_from.category.choices = [('生活', '生活'), ('科技', '科技')]
#     if news_from.validate_on_submit():
#         News.objects(id=new_id).update(
#             title=news_from.title.data,
#             content=news_from.content.data,
#             timestamp=news_from.timestamp.data,
#             is_valid=news_from.is_valid.data,
#             category=news_from.category.data
#         )
#         flash('修改成功')
#         return redirect(url_for('admin.index'))
#     news_from.title.data = new.title
#     news_from.content.data = new.content
#     news_from.timestamp.data = new.timestamp
#     news_from.category.data = new.category
#     news_from.is_valid.data = new.is_valid
#     return render_template('admin/edit.html', new=new, news_from=news_from)


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
