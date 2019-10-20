from flask_script import Manager
from app import app, db
import model

manager = Manager(app)
app.config['DEBUG'] = False  # Ensure debugger will load.


@manager.command
def create_tables():
    "Create relational database tables."
    db.create_all()


@manager.command
def drop_tables():
    "Drop all project relational database tables. THIS DELETES DATA."
    db.drop_all()

if __name__ == '__main__':
    manager.run()