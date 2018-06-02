from flask import Flask
from flask_script import Manager
from config import Config
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
# 实例化管理器对象
manager = Manager(app)
# 使用迁移框架
Migrate(app, db)
# 通过管理器对象集成迁移命令
manager.add_command('db', MigrateCommand)

@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
    manager.run()

