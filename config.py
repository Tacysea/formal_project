class Config(object):
    DEBUG = True
    # 配置密钥

    # 配置sqlalchemy，链接数据库
    # sqlalchemy是以url的形式来链接数据库的
    # 在链接数据库之前，现在mysql中创建数据库
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/formal_database'
    # 配置数据库动态追踪修改（可以提前加载数据，跟踪数据库的变化）
    SQLALCHEMY_TRACK_MODIFICATIONS = False


