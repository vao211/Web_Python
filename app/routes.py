from flask import Blueprint, render_template, request, redirect, url_for, flash
'''
route cho các blue print

B1: tạo route 
'''
home = Blueprint('home', __name__)
login = Blueprint("log", __name__)

@home.route('/')  #đối_tượng.route()    home = Blueprint('home', __name__)
def index():
    return render_template('index.html')

@login.route('/login')
def login_page():
    return render_template('login.html')

@login.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']
    
    if username == '1' and password == '1':  
        return redirect(url_for('home.open_welcome', username=username))   #tên_đối_tượng_blue_print.tên_function  home = Blueprint('home', __name__)
    else:
        flash('Login failed. Please check your credentials.', 'danger')
        return redirect(url_for('login.login_page'))

@home.route('/welcome/<username>')   
def open_welcome(username):
    return render_template('welcome.html', username= username)
    

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
