from flask import Blueprint, render_template, request
from datetime import datetime
from SIMS.models import Student

bp = Blueprint('student_register', __name__)

# 生徒登録画面
@bp.route('/<school>/student_register/', methods=['GET', 'POST'])
def student_register(school):
    if request.method == 'POST':
        id= Student.add(
                    name=request.form.get('name'),
                    name_kana=request.form.get('name_kana'),
                    school=school,
                    class_name=request.form.get('class_name'),
                    gender=int(request.form.get('gender')),
                    birthday=datetime.strptime(request.form.get('birthday'), '%Y-%m-%d'), # 文字列を日付型に変換
                    address=request.form.get('address'),
                    phone=request.form.get('phone'),
                    email=request.form.get('email'),
                    gmail=request.form.get('gmail'),
                    note=request.form.get('note'),
                )
        student = Student.get_one(id=id)
        return render_template('student_detail.html',student=student ,school=school)
    else:
        return render_template('student_register.html',school=school)