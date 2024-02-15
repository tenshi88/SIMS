from flask import Blueprint, redirect, request, render_template
from flask_login import login_required
from SIMS.models import School, Class, User

bp = Blueprint('admin_panel', __name__)

# 管理設定画面
@bp.route('/admin_panel', methods=['GET', 'POST'])
@login_required
def admin_panel():
    if request.method == 'GET':
        schools = School.get_all()
        classes = Class.get_all()
        users = User.get_all()
        return render_template('admin_panel.html', schools=schools, classes=classes, users=users)
    elif request.method == 'POST':
        type = request.form.get('type')
        pass