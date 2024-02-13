from datetime import datetime
from flask import Blueprint, jsonify, request
from flask_login import login_required
from SIMS import db, app
from SIMS.models import Student

bp = Blueprint('api_student', __name__)

with app.app_context():
    db.create_all()

# 生徒操作用API
@bp.route('/api/student', methods=['POST'])
@login_required
def api_student():
    try:
        action = request.form.get('action')
        match action:
            # 生徒削除
            case 'delete':
                id = request.form.get('id')
                student = Student.query.filter(Student.id == id).first()
                db.session.delete(student)
                db.session.commit()
                db.session.close()
                return jsonify({ 'error': '', 'status': 'success' })
            # 生徒更新
            case 'update':
                id = request.form.get('id')
                student = Student.query.filter(Student.id == id).first()
                student.name = request.form.get('name')
                student.school = request.form.get('school')
                student.class_name = request.form.get('class_name')
                student.gender = request.form.get('gender')
                birthday = request.form.get('birthday')
                student.birthday = datetime.strptime(birthday, '%Y-%m-%d') # 文字列を日付型に変換
                student.address = request.form.get('address')
                student.phone = request.form.get('phone')
                student.email = request.form.get('email')
                student.gmail = request.form.get('gmail')
                student.note = request.form.get('note')
                db.session.add(student)
                db.session.commit()
                db.session.close()
                return jsonify({ 'error': '', 'status': 'success' })
            # 生徒登録
            case 'register':
                name = request.form.get('name')
                school = request.form.get('school')
                class_name = request.form.get('class_name')
                gender = request.form.get('gender')
                birthday = request.form.get('birthday')
                birthday = datetime.strptime(birthday, '%Y-%m-%d') # 文字列を日付型に変換
                address = request.form.get('address')
                phone = request.form.get('phone')
                email = request.form.get('email')
                gmail = request.form.get('gmail')
                note = request.form.get('note')
                student = Student(
                    name=name,
                    school=school,
                    class_name=class_name,
                    gender=gender,
                    birthday=birthday,
                    address=address,
                    phone=phone,
                    email=email,
                    gmail=gmail,
                    note=note,
                )
                db.session.add(student)
                db.session.commit()
                db.session.close()
                return jsonify({ 'error': '', 'status': 'success' })
            # IDと学校名で取得
            case 'get':
                school = request.form.get('school')
                id = request.form.get('id')
                if id and school:
                    students = Student.query.filter(Student.id == id, Student.school == school).all()
                elif school:
                    students = Student.query.filter(Student.id == id).all()
                students = [student.getData() for student in students]
                return jsonify({ 'error': '', 'status': 'success', 'data': students })
            # 不正なアクション
            case _:
                return jsonify({ 'error': 'Invalid action', 'status': 'failure' })
    except Exception as e:
        return jsonify({ 'error': str(e), 'status': 'failure' })