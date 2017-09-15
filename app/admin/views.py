from datetime import datetime

from flask import Blueprint, render_template, flash, redirect, url_for

from app.home.models import New
from app.admin.forms import NewForm

admin = Blueprint('admin', __name__)


@admin.route('/')
def index():
    news = New.objects.all()
    # page = request.args.get('page', 1, type=int)
    # pagination = New.objects.paginate(
    #     page,
    #     per_page=5
    # )
    # news = pagination.items
    # return render_template(
    #     'admin/index.html',
    #     news=news,
    #     pagination=pagination
    # )
    return render_template('admin/index.html', news=news)


@admin.route('/edit/<new_id>/', methods=['GET', 'POST'])
def edit(new_id):
    new = New.objects.get_or_404(id=new_id)
    new_form = NewForm()
    # 必须设置在validate_on_submit前面
    new_form.category.choices = [('life', '生活'), ('tech', '科技')]
    if new_form.validate_on_submit():
        New.objects(id=new_id).update(
            title=new_form.title.data,
            content=new_form.content.data,
            timestamp=new_form.timestamp.data,
            is_valid=new_form.is_valid.data,
            category=new_form.category.data
        )
        flash('修改成功')
        return redirect(url_for('admin.index'))
    new_form.title.data = new.title
    new_form.content.data = new.content
    new_form.timestamp.data = new.timestamp
    new_form.category.data = new.category
    new_form.is_valid.data = new.is_valid
    return render_template('admin/edit.html', new=new, new_form=new_form)


@admin.route('/delete/<new_id>', methods=['POST'])
def delete(new_id):
    try:
        new = New.objects.get_or_404(id=new_id)
    except:
        return 'No'
    new.is_valid = False
    New.objects(id=new_id).delete()
    return 'Yes'


@admin.route('/add/', methods=['GET', 'POST'])
def add():
    new_form = NewForm()
    # 必须设置在validate_on_submit前面
    new_form.category.choices = [('life', '生活'), ('tech', '科技')]
    new_form.timestamp.data = datetime.now()
    if new_form.validate_on_submit():
        New(
            title=new_form.title.data,
            content=new_form.content.data,
            timestamp=new_form.timestamp.data,
            is_valid=new_form.is_valid.data,
            category=new_form.category.data
        ).save()
        flash('添加成功')
        return redirect(url_for('admin.index'))
    return render_template('admin/add.html', new_form=new_form)
