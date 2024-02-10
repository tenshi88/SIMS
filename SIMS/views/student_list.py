from flask import Blueprint, render_template

bp = Blueprint('student_list', __name__)

# 生徒一覧画面
@bp.route('/student_list')
def student_list():
    return render_template('student_list.html')
