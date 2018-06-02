from flask import Flask, session
from flask_script import Manager
from config import Config
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
# Session模块可以指定session信息的存贮
from flask_session import Session
app = Flask(__name__)
app.config.from_object(Config)
# 实例化Session对象
Session(app)
db = SQLAlchemy(app)
# 实例化管理器对象
manager = Manager(app)
# 使用迁移框架
Migrate(app, db)
# 通过管理器对象集成迁移命令
manager.add_command('db', MigrateCommand)

@app.route('/')
def index():
    # 能否实现下面session的存贮？
    # 要设置密钥才能存贮
    # 设置密钥后，启动服务器，将session信息存放在redis数据库中
    # 在终端查看redis数据库
    session['name'] = 2019
    return 'hello world'

if __name__ == '__main__':
    app.run(port=5001)

