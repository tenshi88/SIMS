from datetime import datetime
from os import name
from flask import Blueprint,app, jsonify, redirect, render_template, request
from flask_login import login_required
from httpx import delete
from SIMS import app
from SIMS.models import School, Student, Class

bp = Blueprint('student_edit', __name__)

# 生徒編集画面
@bp.route('/<school>/student_edit/<int:id>',methods=['GET', 'POST'])
@login_required

def student_edit(id,school):
    student = Student.get_one(id=id)
    schools = School.get_all()
    class_member = Class.get_all()
    if request.method == 'POST':
        student_update = Student.update(
                        id=request.form.get('id'),
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
        return redirect("student_list.html",school=school)
    
    elif request.method == 'GET':
        return render_template('student_edit.html',\
            student = student,\
            school = school,\
            schools = schools,\
            class_member = class_member
    )  


@bp.route('/<school>/student_delete/<int:id>',methods=['GET', 'POST'])
@login_required

def student_delete(id,school):

    student = Student.get_one(id=id)
    schools = School.get_all()
    student_delete =Student.delete(id)

    return render_template('student_edit.html',\
        student = student,\
        school = school,\
        schools = schools,\
        student_delete = student_delete
    )  


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')