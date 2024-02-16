from os import name
from flask import Blueprint,app, render_template
from flask_login import login_required
from SIMS import app
from SIMS.models import School, Student

bp = Blueprint('student_detail', __name__)


# パスパラメータを使う(idの部分を変数に入れる)
@bp.route('/<school>/student_detail/<int:id>',methods=['GET', 'POST'])
@login_required

def student_detail(id,school):

    student = Student.get_one(id=id)
    school = School.get_one(name=school)

    return render_template('student_detail.html',\
        id = student['id'],\
        name = student['name'],\
        name_kana = student['name_kana'],\
        class_name = student['class_name'],\
        gender = student['gender'],\
        birthday = student['birthday'],\
        address = student['address'],\
        phone = student['phone'],\
        email = student['email'],\
        gmail = student['gmail'],\
        note = student['note'],\
        school = school
    )  


    

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')