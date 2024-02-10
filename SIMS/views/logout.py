from flask import Blueprint, redirect
from flask_login import login_required
from SIMS.user_auth import UserAuth

bp = Blueprint('logout', __name__)

@bp.route('/logout')
@login_required
def logout():
    # ログアウト処理
    UserAuth.logout_user()
    return redirect('/')