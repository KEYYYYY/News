from flask_wtf import FlaskForm
from wtforms import (
    StringField, DateTimeField, BooleanField, SelectField, SubmitField
)
from wtforms.validators import DataRequired


class NewForm(FlaskForm):
    title = StringField('标题', validators=[
        DataRequired(message='这是必填字段')
    ])
    content = StringField('内容')
    # 必须申明coerce，否则不能通过验证
    type_id = SelectField('类型', coerce=int)
    add_time = DateTimeField('添加时间', validators=[
        DataRequired(message='这是必填字段')
    ])
    is_valid = BooleanField('是否有效')
    submit = SubmitField('提交')
