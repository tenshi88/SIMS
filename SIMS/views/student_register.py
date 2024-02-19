from flask import Blueprint, render_template

bp = Blueprint('student_register', __name__)

# 生徒登録画面
@bp.route('/<school>/student_register/')
def student_register(school):
    return render_template('student_register.html',school=school)
