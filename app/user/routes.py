from flask import Flask, render_template, request, redirect, url_for, Blueprint

user_bp = Blueprint('user', __name__)

#eg:
users = {
    1 :{"name": "Vinh", "email": "Vinh@gmail.com"},
    2 :{"name" : "Hùng sv", "email": "Hung@gmail.com"},
}

@user_bp.route('/profile/<int:user_id>')
def profile(user_id):
    user = users.get(user_id)
    if user:
        return render_template('profile.html', user=user)
    else:
        return "User not found", 404
