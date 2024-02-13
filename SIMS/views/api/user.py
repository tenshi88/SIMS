from flask import Blueprint, jsonify, request
from flask_login import login_required
from SIMS import db, app
from SIMS.models import User

bp = Blueprint('api_user', __name__)

with app.app_context():
    db.create_all()

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
                user = User.query.filter(User.id == id).first()
                db.session.delete(user)
                db.session.commit()
                db.session.close()
                return jsonify({ 'error': '', 'status': 'success' })
            # ユーザ更新
            case 'update':
                id = request.form.get('id')
                user = User.query.filter(User.id == id).first()
                user.user_id = request.form.get('user_id')
                user.password = request.form.get('password')
                db.session.commit()
                db.session.close()
                return jsonify({ 'error': '', 'status': 'success' })
            # ユーザ登録
            case 'register':
                user = User(
                    user_id=request.form.get('user_id'),
                    password=request.form.get('password')
                )
                db.session.add(user)
                db.session.commit()
                db.session.close()
                return jsonify({ 'error': '', 'status': 'success' })
            # ユーザ全取得
            case 'get':
                users = User.query.all()
                users = [user.getData() for user in users]
                return jsonify({ 'error': '', 'status': 'success', 'data': users })
            case _:
                return jsonify({ 'error': 'Invalid action', 'status': 'failure' })
    except Exception as e:
        return jsonify({ 'error': str(e), 'status': 'failure' })