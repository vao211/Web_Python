from flask import Blueprint, render_template, request, redirect, url_for, flash
'''
route cho các blue print

B1: tạo route 
'''
home_bp = Blueprint('home', __name__)
login_bp = Blueprint("login", __name__)

@home_bp.route('/')  #đối_tượng.route()    home = Blueprint('home', __name__)
def index():
    return render_template('index.html')

@login_bp.route('/login')
def login_page():
    return render_template('login.html')

@login_bp.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    u = {"vinh": 1, "hung": 2}
    if username == 'vinh' and password == '1' or username == 'hung' and password == '1':
        return redirect(url_for('user.profile', user_id=u.get(username)))#tên_đối_tượng_blue_print.tên_function  home = Blueprint('home', __name__)
    else:
        flash('Login failed. Please check your credentials.', 'danger')
        return redirect(url_for('login.login_page'))



'''
@home.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    
    if username == 'admin' and password == 'password':
        return redirect(url_for('main.welcome', username=username))
    else:
        flash('Login failed. Please check your credentials.', 'danger')
        return redirect(url_for('main.login'))

@home.route('/login')
def login_page():
    return render_template('login.html')
'''
