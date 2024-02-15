from flask import Blueprint, redirect, render_template
from flask_login import login_required
from SIMS.models import Student, School, Class

bp = Blueprint('student_list', __name__)

# 生徒一覧画面
@bp.route('/<school>/student_list')
@login_required
def student_list(school):
    # 生徒一覧を取得
    schools = School.get_all()
    students_by_class = Student.get_divide_by_class(school)
    # 学校名が不正な場合はトップページにリダイレクト
    if school not in [school['name'] for school in schools]:
        return redirect('/')
    return render_template('student_list.html', students_by_class=students_by_class, schools=schools, school=school)
