from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import create_app, db
from app.home.models import New, Type

app = create_app()
migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', MigrateCommand)


@manager.shell
def make_shell_context():
    return dict(
        app=app,
        db=db,
        New=New,
        Type=Type
    )


if __name__ == '__main__':
    manager.run()
