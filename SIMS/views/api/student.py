from datetime import datetime
from flask import Blueprint, jsonify, request
from flask_login import login_required
from SIMS.models import Student

bp = Blueprint('api_student', __name__)

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
                Student.delete(id)
                return jsonify({ 'error': '', 'status': 'success' })
            # 生徒更新
            case 'update':
                Student.update(
                    id=request.form.get('id'),
                    name=request.form.get('name'),
                    name_kana=request.form.get('name_kana'),
                    school=request.form.get('school'),
                    class_name=request.form.get('class_name'),
                    gender=int(request.form.get('gender')),
                    birthday=datetime.strptime(request.form.get('birthday'), '%Y-%m-%d'), # 文字列を日付型に変換
                    address=request.form.get('address'),
                    phone=request.form.get('phone'),
                    email=request.form.get('email'),
                    gmail=request.form.get('gmail'),
                    note=request.form.get('note'),
                )
                return jsonify({ 'error': '', 'status': 'success' })
            # 生徒登録
            case 'register':
                Student.add(
                    name=request.form.get('name'),
                    name_kana=request.form.get('name_kana'),
                    school=request.form.get('school'),
                    class_name=request.form.get('class_name'),
                    gender=int(request.form.get('gender')),
                    birthday=datetime.strptime(request.form.get('birthday'), '%Y-%m-%d'), # 文字列を日付型に変換
                    address=request.form.get('address'),
                    phone=request.form.get('phone'),
                    email=request.form.get('email'),
                    gmail=request.form.get('gmail'),
                    note=request.form.get('note'),
                )
                return jsonify({ 'error': '', 'status': 'success' })
            # IDと学校名で取得
            case 'get':
                args = request.form.to_dict()
                del args['action']
                if 'id' in args:
                    data = Student.get_one(**args)
                else:
                    data = Student.get_all(**args)
                return jsonify({ 'error': '', 'status': 'success', 'data': data })
            case 'get_categorized':
                data = Student.get_categorized_list(request.form.get('school'))
                return jsonify({ 'error': '', 'status': 'success', 'data': data })
            # 不正なアクション
            case _:
                return jsonify({ 'error': 'Invalid action', 'status': 'failure' })
    except Exception as e:
        return jsonify({ 'error': str(e), 'status': 'failure' })