from flask import Blueprint, render_template

home = Blueprint(__name__, 'home')


@home.route('/')
def index():
    return render_template('home/index.html')
