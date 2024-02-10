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
                class_ = Class.query.filter(Class.id == id).first()
                db.session.delete(class_)
                db.session.commit()
                db.session.close()
                return jsonify({ 'error': '', 'result': 'Success' })
            # クラス更新
            case 'update':
                id = request.form.get('id')
                class_ = Class.query.filter(Class.id == id).first()
                class_.name = request.form.get('name')
                db.session.commit()
                db.session.close()
                return jsonify({ 'error': '', 'result': 'Success' })
            # クラス登録
            case 'register':
                class_ = Class(
                    name=request.form.get('name')
                )
                db.session.add(class_)
                db.session.commit()
                db.session.close()
                return jsonify({ 'error': '', 'result': 'Success' })
            # クラス全取得
            case 'get':
                classes = Class.query.all()
                classes = [class_.getData() for class_ in classes]
                return jsonify({ 'error': '', 'result': 'Success', 'data': classes })   
            case _:
                return jsonify({ 'error': 'Invalid action', 'result': 'Failure' })
    except Exception as e:
        return jsonify({ 'error': str(e), 'result': 'Failure' })