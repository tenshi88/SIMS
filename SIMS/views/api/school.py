from flask import Blueprint, jsonify, request
from flask_login import login_required
from SIMS import db, app
from SIMS.models import School

bp = Blueprint('api_school', __name__)

with app.app_context():
    db.create_all()

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
                school = School.query.filter(School.id == id).first()
                db.session.delete(school)
                db.session.commit()
                db.session.close()
                return jsonify({ 'error': '', 'result': 'Success' })
            # 学校更新
            case 'update':
                id = request.form.get('id')
                school = School.query.filter(School.id == id).first()
                school.name = request.form.get('name')
                db.session.commit()
                db.session.close()
                return jsonify({ 'error': '', 'result': 'Success' })
            # 学校登録
            case 'register':
                school = School(
                    name=request.form.get('name')
                )
                db.session.add(school)
                db.session.commit()
                db.session.close()
                return jsonify({ 'error': '', 'result': 'Success' })
            # 学校全取得
            case 'get':
                schools = School.query.all()
                schools = [school.getData() for school in schools]
                return jsonify({ 'error': '', 'result': 'Success', 'data': schools })
            case _:
                return jsonify({ 'error': 'Invalid action', 'result': 'Failure' })
    except Exception as e:
        return jsonify({ 'error': str(e), 'result': 'Failure' })