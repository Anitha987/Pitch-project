from app import create_app,db
from app.models import User,Pitch,Category,Comment,Vote
from flask_migrate import Migrate,MigrateCommand

app = create_app('development')
migrate=Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)
@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User,Pitch = Pitch,Comment = Comment,Vote = Vote )
if __name__ == '__main__':
    manager.run()