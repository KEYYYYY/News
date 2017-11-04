from flask_script import Manager

from app import create_app, db
from app.models import News, Category

app = create_app()
manager = Manager(app)


@manager.shell
def make_shell_context():
    return dict(
        app=app,
        db=db,
        News=News,
        Category=Category,
    )


if __name__ == '__main__':
    manager.run()
