from flask import Flask
from flask_script import Manager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
# 实例化管理器对象
manager = Manager(app)

@app.route('/')
def index():
    return 'hello world'

if __name__ == '__main__':
    manager.run()

