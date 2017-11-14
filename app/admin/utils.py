import os

from PIL import Image
from flask import current_app

from app import photos


def create_thumbnail(image):
    img = Image.open(photos.path(image))
    # 得到图片尺寸
    width, height = img.size
    if width > height:
        margin_left = (width - height) / 2
        img = img.crop((
            margin_left, 0, margin_left + height, height
        ))
    else:
        margin_top = (height - width) / 2
        img = img.crop((
            0, margin_top, width, margin_top + width
        ))
    file_name, ext = os.path.splitext(image)
    new_file_name = file_name + '_t' + ext
    img.thumbnail((300, 300), Image.ANTIALIAS)
    img.save(os.path.join(
        current_app.config['UPLOADED_PHOTOS_DEST'], new_file_name
    ))
    return new_file_name
