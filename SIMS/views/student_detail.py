from os import name
from flask import Blueprint,app, render_template, request
from flask_login import login_required
from SIMS import app
from SIMS.models import School, Student

bp = Blueprint('student_detail', __name__)


# パスパラメータを使う(idの部分を変数に入れる)
@bp.route('/<str:school>/student_detail/<int:id>',methods=['GET', 'POST'])
@login_required
def student_detail(id,school):
    student = Student.get_one(id=id)
    school = School.get_one(school=school)
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
        note = student['note']
    )   


# # パスパラメータを使う(idの部分を変数に入れる)
# @bp.route('/天満橋校/student_detail',methods=['GET', 'POST'])
# # @login_required
# def student_detail2(id):

    
#     student = Student.get_one(id = id)
#     students = [student.getData() for student in students]
#     return render_template('student_detail.html',\
#         name = name
#     )   


# # パスパラメータを使う(idの部分を変数に入れる)
# @bp.route('/心斎橋校/student_detail',methods=['GET', 'POST'])
# # @login_required
# def student_detail3(id):

    
#     student = Student.get_one(id = id)
#     students = [student.getData() for student in students]
#     return render_template('student_detail.html',\
#         name = name
#     )   


# # パスパラメータを使う(idの部分を変数に入れる)
# @bp.route('/三宮校/student_detail',methods=['GET', 'POST'])
# # @login_required
# def student_detail4(id):

    
#     student = Student.get_one(id = id)
#     students = [student.getData() for student in students]
#     return render_template('student_detail.html',\
#         name = name
#     )   


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')