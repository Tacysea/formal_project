from flask import session, render_template
from . import news_bp

@news_bp.route('/')
def index():
    # 能否实现下面session的存贮？
    # 要设置密钥才能存贮
    # 设置密钥后，启动服务器，将session信息存放在redis数据库中
    # 在终端查看redis数据库
    session['name'] = 2019
    return render_template('news/index.html')
