from flask import Blueprint,app, render_template
from flask_login import login_required
from SIMS import db, app
from SIMS.models import Student

bp = Blueprint('student_detail', __name__)


# パスパラメータを使う(idの部分を変数に入れる)
@bp.route('/本町校/student_detail',methods=['GET', 'POST'])
# @login_required
def student_detail(id):

    
    student = Student.get_one(id = id)
    students = [student.getData() for student in students]
    return render_template('student_detail.html',\
        name = Student.one('id')
    )   


# パスパラメータを使う(idの部分を変数に入れる)
@bp.route('/天満橋校/student_detail',methods=['GET', 'POST'])
# @login_required
def student_detail(id):

    
    student = Student.get_one(id = id)
    students = [student.getData() for student in students]
    return render_template('student_detail.html',\
        name = Student.one('id')
    )   


# パスパラメータを使う(idの部分を変数に入れる)
@bp.route('/心斎橋校/student_detail',methods=['GET', 'POST'])
# @login_required
def student_detail(id):

    
    student = Student.get_one(id = id)
    students = [student.getData() for student in students]
    return render_template('student_detail.html',\
        name = Student.one('id')
    )   


# パスパラメータを使う(idの部分を変数に入れる)
@bp.route('/三宮校/student_detail',methods=['GET', 'POST'])
# @login_required
def student_detail(id):

    
    student = Student.get_one(id = id)
    students = [student.getData() for student in students]
    return render_template('student_detail.html',\
        student = student
    )   


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')