from flask_wtf import FlaskForm
from wtforms import (
    StringField, BooleanField, SelectField, SubmitField, TextAreaField
)
from wtforms.validators import DataRequired


class NewsForm(FlaskForm):
    title = StringField('标题', validators=[
        DataRequired(message='这是必填字段')
    ])
    content = TextAreaField('内容')
    # 必须申明coerce，否则不能通过验证
    category = SelectField('类型', coerce=int)
    is_valid = BooleanField('是否有效')
    submit = SubmitField('提交')
