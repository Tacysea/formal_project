from flask_script import Manager

from flask_migrate import Migrate, MigrateCommand

from info import create_app, db

app = create_app('development')


# 实例化管理器对象
manager = Manager(app)
# 使用迁移框架
Migrate(app, db)
# 通过管理器对象集成迁移命令
manager.add_command('db', MigrateCommand)



if __name__ == '__main__':
    print(app.url_map)
    app.run(port=5001)

