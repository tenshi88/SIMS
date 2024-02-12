from flask import Blueprint, redirect, request, render_template
from flask_login import login_required
from SIMS import db, app
from SIMS.models import School, Class, User

bp = Blueprint('admin_panel', __name__)

with app.app_context():
    db.create_all()

# 管理設定画面
@bp.route('/admin_panel', methods=['GET', 'POST'])
@login_required
def admin_panel():
    if request.method == 'GET':
        schools = School.query.all()
        schools = [school.getData() for school in schools]
        classes = Class.query.all()
        classes = [class_.getData() for class_ in classes]
        users = User.query.all()
        users = [user.getData() for user in users]
        return render_template('admin_panel.html', schools=schools, classes=classes, users=users)
    elif request.method == 'POST':
        type = request.form.get('type')
        pass