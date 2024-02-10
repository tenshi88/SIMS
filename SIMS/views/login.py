from flask import Blueprint, redirect, render_template, request
from flask_login import current_user
from SIMS.user_auth import UserAuth

bp = Blueprint('login', __name__)

@bp.route('/login', methods=['GET', 'POST'])
def login():
    # ログイン済みの場合はトップページにリダイレクト
    if current_user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        password = request.form.get('password')
        # IDとパスワードが一致したらトップページにリダイレクト
        if UserAuth.is_valid_user(user_id, password):
            UserAuth.login_user(user_id)
            return redirect('/')
        # 一致しなかったらログインページに戻る
        else:
            return render_template('login.html', error_msg='IDまたはパスワードが違います')
    else:
        return render_template('login.html', error_msg='')