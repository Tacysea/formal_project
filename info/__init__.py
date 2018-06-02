from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# Session模块可以指定session信息的存贮
from flask_session import Session
# 设置跨站请求保护
from flask_wtf import CSRFProtect
from config import config_dict
db = SQLAlchemy()
# 创建实例的工厂方法：动态加载配置对象
def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_dict[config_name])
    # 实例化Session对象
    Session(app)
    # 实例化csrf
    CSRFProtect(app)
    # CSRFProtect只做验证工作，
    # cookie中的 csrf_token 和表单中的 csrf_token 需要我们自己实现
    db.init_app(app)
    # 由于一个函数只能返回一个值，因此db无法返回
    # 先把db抽取出去，然后再用上述方法将app与db进行关联
    # 导入蓝图对象
    from info.modules.news import news_bp
    # 注册蓝图对象
    app.register_blueprint(news_bp)
    return app