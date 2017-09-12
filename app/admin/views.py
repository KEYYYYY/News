from datetime import datetime

from flask import Blueprint, render_template, flash, redirect, url_for, request

from app.home.models import New, Type
from app.admin.forms import NewForm
from app import db

admin = Blueprint('admin', __name__)


@admin.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    pagination = New.query.order_by(New.add_time.desc()).paginate(
        page,
        per_page=5
    )
    news = pagination.items
    return render_template(
        'admin/index.html',
        news=news,
        pagination=pagination
    )


@admin.route('/edit/<int:new_id>/', methods=['GET', 'POST'])
def edit(new_id):
    new = New.query.get_or_404(new_id)
    types = Type.query.all()
    new_form = NewForm()
    # 必须设置在validate_on_submit前面
    new_form.type_id.choices = [(item.id, item.name) for item in types]
    if new_form.validate_on_submit():
        new.title = new_form.title.data
        new.content = new_form.content.data
        new.add_time = new_form.add_time.data
        new.is_valid = new_form.is_valid.data
        new.type_id = new_form.type_id.data
        db.session.add(new)
        db.session.commit()
        flash('修改成功')
        return redirect(url_for('admin.index'))
    new_form.title.data = new.title
    new_form.content.data = new.content
    new_form.add_time.data = new.add_time
    new_form.type_id.data = new.type_id
    new_form.is_valid.data = new.is_valid
    return render_template('admin/edit.html', new=new, new_form=new_form)


@admin.route('/delete/<int:new_id>')
def delete(new_id):
    new = New.query.get_or_404(new_id)
    db.session.delete(new)
    db.session.commit()
    flash('删除成功')
    return redirect(url_for('admin.index'))


@admin.route('/add/', methods=['GET', 'POST'])
def add():
    types = Type.query.all()
    new_form = NewForm()
    # 必须设置在validate_on_submit前面
    new_form.type_id.choices = [(item.id, item.name) for item in types]
    new_form.add_time.data = datetime.now()
    if new_form.validate_on_submit():
        title = new_form.title.data
        content = new_form.content.data
        add_time = new_form.add_time.data
        is_valid = new_form.is_valid.data
        type_id = new_form.type_id.data
        new = New(
            title=title,
            content=content,
            add_time=add_time,
            is_valid=is_valid,
            type_id=type_id
        )
        db.session.add(new)
        db.session.commit()
        flash('添加成功')
        return redirect(url_for('admin.index'))
    return render_template('admin/add.html', new_form=new_form)
