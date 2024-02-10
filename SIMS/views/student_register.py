from flask import Blueprint

bp = Blueprint('student_register', __name__)

# 生徒登録画面
@bp.route('/student_register')
def student_register():
    return '生徒登録画面'
