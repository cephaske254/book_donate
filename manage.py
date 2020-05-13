from app import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand
from app.models import Beneficiary,Book,Category,Comments,User

app = create_app('development')

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('server', Server)
manager.add_command('db', MigrateCommand)

@manager.shell
def make_shell_context():
    return dict(db=db,app=app,Beneficiary=Beneficiary,Book=Book,Category=Category,Comments=Comments,User=User)

if __name__ == "__main__":
    manager.run()