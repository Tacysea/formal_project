from flask import Blueprint

# 创建蓝图对象
news_bp = Blueprint('new_bp', __name__)

# 把使用蓝图对象的模块导入创建蓝图对象的下面

from . import views