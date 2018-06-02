from redis import StrictRedis
class Config(object):
    DEBUG = True
    # 配置密钥(注意密钥的设置方式)

    # 配置sqlalchemy，链接数据库
    # sqlalchemy是以url的形式来链接数据库的
    # 在链接数据库之前，现在mysql中创建数据库
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/formal_database'
    # 配置数据库动态追踪修改（可以提前加载数据，跟踪数据库的变化）
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # sqlalchemy只是存贮了模型类中的数据
    # 还需要存贮session信息（用户的状态信息）,如果session没有保存到数据库，那么默认保存在浏览器中
    # 使用redis保存session信息
    # 配置redis基本信息
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = '6379'
    SESSION_TYPE = 'redis'
    # 对session信息进行签名编码
    SESSION_USE_SIGNER = True
    #
    SESSION_REDIS = StrictRedis(host=REDIS_HOST, port=REDIS_PORT)
    # 指定session信息过期时间,以秒为单位，设置是时间为一天
    PERMANENT_SESSION_LIFETIME = 86400