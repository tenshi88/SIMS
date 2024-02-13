from flask import Blueprint, jsonify, request
from flask_login import login_required
from SIMS import db, app
from SIMS.models import Class

bp = Blueprint('api_class', __name__)

with app.app_context():
    db.create_all()

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
                cls = Class.query.filter(Class.id == id).first()
                db.session.delete(cls)
                db.session.commit()
                db.session.close()
                return jsonify({ 'error': '', 'status': 'success' })
            # クラス更新
            case 'update':
                id = request.form.get('id')
                cls = Class.query.filter(Class.id == id).first()
                cls.name = request.form.get('name')
                db.session.commit()
                db.session.close()
                return jsonify({ 'error': '', 'status': 'success' })
            # クラス登録
            case 'register':
                cls = Class(
                    name=request.form.get('name')
                )
                db.session.add(cls)
                db.session.commit()
                db.session.close()
                return jsonify({ 'error': '', 'status': 'success' })
            # クラス全取得
            case 'get':
                classes = Class.query.all()
                classes = [cls.getData() for cls in classes]
                return jsonify({ 'error': '', 'status': 'success', 'data': classes })   
            case _:
                return jsonify({ 'error': 'Invalid action', 'status': 'failure' })
    except Exception as e:
        return jsonify({ 'error': str(e), 'status': 'failure' })