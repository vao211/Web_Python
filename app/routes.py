from flask import Blueprint, render_template
'''
route cho các blue print

B1: tạo route 
'''
home = Blueprint('main', __name__)
page_1 = Blueprint("page_1", __name__)

@home.route('/')
def home_page():
    return render_template('index.html')

@page_1.route('/page_1')
def page_1_page():
    return render_template('page_1.html')

