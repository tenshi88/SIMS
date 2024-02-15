from flask import Blueprint,app, render_template
from flask_login import login_required
from SIMS import db, app
from SIMS.models import Student

bp = Blueprint('student_detail', __name__)

with app.app_context():
    db.create_all()


    
@bp.route('/student_detail',methods=['GET', 'POST'])
# @login_required
def student_detail():

    students = Student.query.all()
    students = [student.getData() for student in students]
    return render_template('student_detail.html',\
        name = Student.one('id')
    )   


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')