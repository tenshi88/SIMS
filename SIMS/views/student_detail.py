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
    schools = School.get_all()

    return render_template('student_detail.html',\
        student = student,\
        school = school,\
        schools = schools
    )  
 
    
if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')