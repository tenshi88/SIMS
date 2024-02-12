from flask import Blueprint, redirect, render_template
from flask_login import login_required
from SIMS import db, app
from SIMS.models import School

bp = Blueprint('student_list', __name__)

with app.app_context():
    db.create_all()

# 生徒一覧画面
@bp.route('/<school>/student_list')
@login_required
def student_list(school):
    schools = School.query.all()
    schools = [school.getData() for school in schools]
    # 学校名が不正な場合はトップページにリダイレクト
    if school not in [school['name'] for school in schools]:
        return redirect('/')
    return render_template('student_list.html', schools=schools, school=school)