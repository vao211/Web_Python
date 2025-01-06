from flask import Flask
'''
đăng ký blue print ở đây
B2: đăng ký blue_print
'''
def create_app():
    app = Flask(__name__)
    
    from .routes import home, page_1
    app.register_blueprint(home)
    app.register_blueprint(page_1)
    
    return app
