from flask import Flask
'''
đăng ký blue print ở đây
B2: đăng ký blue_print
'''
def create_app():
    app = Flask(__name__)
    
    from .routes import home ,login
    app.register_blueprint(home)
    app.register_blueprint(login)
    
    return app

'''
    from .routes import home
    app.register_blueprint(home)
'''