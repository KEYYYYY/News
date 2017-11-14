from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import (BooleanField, SelectField, StringField, SubmitField,
                     TextAreaField)
from wtforms.validators import DataRequired

from app import photos


class NewsForm(FlaskForm):
    title = StringField('标题', validators=[
        DataRequired(message='这是必填字段')
    ])
    content = TextAreaField('内容')
    # 必须申明coerce，否则不能通过验证
    category = SelectField('类型', coerce=int)
    photo = FileField('图片', validators=[
        FileAllowed(photos, message='请选择图片上传')
    ])
    is_valid = BooleanField('是否有效')
    submit = SubmitField('提交')
