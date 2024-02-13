from flask import Blueprint, redirect, render_template
from flask_login import login_required
from SIMS import db, app
from SIMS.models import Student, School, Class, get_divide_students_by_class

bp = Blueprint('student_list', __name__)

with app.app_context():
    db.create_all()

# 生徒一覧画面
@bp.route('/<school>/student_list')
@login_required
def student_list(school):
    # students = Student.query.filter_by(school=school).all()
    # students = [student.getData() for student in students]
    schools = School.query.all()
    schools = [school.getData() for school in schools]
    # classes = Class.query.all()
    # classes = [cls.getData() for cls in classes]

    students_by_class = get_divide_students_by_class(school)

    # studentsをクラスごとに分ける
    # students_by_class = []
    # for cls in classes:
    #     students_by_class.append({
    #         'class_name': cls['name'],
    #         'students': [student for student in students if student['class_name'] == cls['name']]
    #     })

    # for cls in classes:
    #     cls['students'] = [student for student in students if student['class_name'] == cls['name']]


    # 学校名が不正な場合はトップページにリダイレクト
    if school not in [school['name'] for school in schools]:
        return redirect('/')
    return render_template('student_list.html', students_by_class=students_by_class, schools=schools, school=school)