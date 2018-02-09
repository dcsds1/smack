from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from smack import app
from exts import db


manager = Manager(app)

migrate = Migrate(app, db)

manager.add_command('db', Migrate)


if __name__ == '__main__':
    manager.run()