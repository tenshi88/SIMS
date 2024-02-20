from os import name
from flask import Blueprint,app, render_template, request
from flask_login import login_required
from httpx import delete
from SIMS import app
from SIMS.models import School, Student

bp = Blueprint('student_edit', __name__)

# 生徒編集画面
@bp.route('/<school>/student_edit/<int:id>',methods=['GET', 'POST'])
@login_required

def student_edit(id,school):

    student = Student.get_one(id=id)
    schools = School.get_all()
    student_delete = Student.delete(id=id)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
    print(student_delete)

    return render_template('student_edit.html',\
        student = student,\
        school = school,\
        schools = schools,\
        student_delete = student_delete
    )  


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')