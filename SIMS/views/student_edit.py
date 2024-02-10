from flask import Blueprint

bp = Blueprint('student_edit', __name__)

# 生徒編集画面
@bp.route('/student_edit')
def student_edit():
    return '生徒編集画面'