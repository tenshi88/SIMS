from os import name
from flask import Blueprint,app, render_template
from flask_login import login_required
from SIMS import app
from SIMS.models import School, Student

bp = Blueprint('student_edit', __name__)

# 生徒編集画面
@bp.route('/<school>/student_edit/<int:id>',methods=['GET', 'POST'])
@login_required

def student_edit(id,school):

    student = Student.get_one(id=id)
    schools = School.get_all()

    return render_template('student_edit.html',\
        student = student,\
        school = school,\
        schools = schools
    )  

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')