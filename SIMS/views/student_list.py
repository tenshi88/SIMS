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
    categorized_students = Student.get_categorized_list(school)
    # 学校名が不正な場合はトップページにリダイレクト
    if school not in [school['name'] for school in schools]:
        return redirect('/')
    return render_template('student_list.html', categorized_students=categorized_students, schools=schools, school=school)
