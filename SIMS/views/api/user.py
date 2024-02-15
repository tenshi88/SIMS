from flask import Blueprint, jsonify, request
from flask_login import login_required
from SIMS.models import User

bp = Blueprint('api_user', __name__)

# ユーザ操作用API
@bp.route('/api/user', methods=['POST'])
@login_required
def api_user():
    try:
        action = request.form.get('action')
        match action:
            # ユーザ削除
            case 'delete':
                id = request.form.get('id')
                User.delete(id)
                return jsonify({ 'error': '', 'status': 'success' })
            # ユーザ更新
            case 'update':
                User.update(
                    id=request.form.get('id'),
                    user_id=request.form.get('user_id'),
                    password=request.form.get('password')
                )
                return jsonify({ 'error': '', 'status': 'success' })
            # ユーザ登録
            case 'register':
                User.add(
                    user_id=request.form.get('user_id'),
                    password=request.form.get('password')
                )
                return jsonify({ 'error': '', 'status': 'success' })
            # ユーザ全取得
            case 'get':
                users = User.get_all()
                return jsonify({ 'error': '', 'status': 'success', 'data': users })
            case _:
                return jsonify({ 'error': 'Invalid action', 'status': 'failure' })
    except Exception as e:
        return jsonify({ 'error': str(e), 'status': 'failure' })