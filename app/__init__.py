from flask import Flask
import sys
import os

#Thêm đường dẫn đến thư mục cha
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config

'''
đăng ký blue print ở đây
B2: đăng ký blue_print
'''
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    from .routes import home_bp ,login_bp
    from .user import user_bp
    
    app.register_blueprint(user_bp, url_prefix='/user') #thêm prefix trước route đã tạo 
                                                        #(@user_bp.route('/profile/<int:user_id>')): /user/profile/<int:user_id>
    app.register_blueprint(home_bp)
    app.register_blueprint(login_bp)
    
    return app

'''
    from .routes import home
    app.register_blueprint(home)
'''