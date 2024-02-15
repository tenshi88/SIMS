from flask import Blueprint, jsonify, request
from flask_login import login_required
from SIMS.models import School

bp = Blueprint('api_school', __name__)

# 学校一覧操作用API
@bp.route('/api/school', methods=['POST'])
@login_required
def api_school():
    try:
        action = request.form.get('action')
        match action:
            # 学校削除
            case 'delete':
                id = request.form.get('id')
                School.delete(id)
                return jsonify({ 'error': '', 'status': 'success' })
            # 学校更新
            case 'update':
                School.update(
                    id=request.form.get('id'),
                    name=request.form.get('name')
                )
                return jsonify({ 'error': '', 'status': 'success' })
            # 学校登録
            case 'register':
                School.add(
                    name=request.form.get('name')
                )
                return jsonify({ 'error': '', 'status': 'success' })
            # 学校全取得
            case 'get':
                schools = School.get_all()
                return jsonify({ 'error': '', 'status': 'success', 'data': schools })
            case _:
                return jsonify({ 'error': 'Invalid action', 'status': 'failure' })
    except Exception as e:
        return jsonify({ 'error': str(e), 'status': 'failure' })