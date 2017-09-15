from flask_script import Manager

from app import create_app, mongo
from app.home.models import New

app = create_app()
manager = Manager(app)


@manager.shell
def make_shell_context():
    return dict(
        app=app,
        mongo=mongo,
        New=New
    )


if __name__ == '__main__':
    manager.run()
