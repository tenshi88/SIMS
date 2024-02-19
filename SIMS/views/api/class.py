from datetime import datetime
from flask import Blueprint, jsonify, request
from flask_login import login_required
from SIMS.models import Class

bp = Blueprint('api_class', __name__)

# クラス一覧操作用API
@bp.route('/api/class', methods=['POST'])
@login_required
def api_class():
    try:
        action = request.form.get('action')
        match action:
            # クラス削除
            case 'delete':
                id = request.form.get('id')
                Class.delete(id)
                return jsonify({ 'error': '', 'status': 'success' })
            # クラス更新
            case 'update':
                Class.update(
                    id=request.form.get('id'),
                    name=request.form.get('name'),
                    class_number=int(request.form.get('class_number')),
                    open_date=datetime.strptime(request.form.get('open_date'), '%Y-%m-%d'), # 文字列を日付型に変換
                    close_date=datetime.strptime(request.form.get('close_date'), '%Y-%m-%d'), # 文字列を日付型に変換
                )
                return jsonify({ 'error': '', 'status': 'success' })
            # クラス登録
            case 'register':
                Class.add(
                    name=request.form.get('name'),
                    class_number=int(request.form.get('class_number')),
                    open_date=datetime.strptime(request.form.get('open_date'), '%Y-%m-%d'), # 文字列を日付型に変換
                    close_date=datetime.strptime(request.form.get('close_date'), '%Y-%m-%d'), # 文字列を日付型に変換
                )
                return jsonify({ 'error': '', 'status': 'success' })
            # クラス全取得
            case 'get':
                classes = Class.get_all()
                return jsonify({ 'error': '', 'status': 'success', 'data': classes })   
            case _:
                return jsonify({ 'error': 'Invalid action', 'status': 'failure' })
    except Exception as e:
        return jsonify({ 'error': str(e), 'status': 'failure' })