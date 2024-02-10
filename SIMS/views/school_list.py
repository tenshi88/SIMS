from flask import Blueprint, render_template
from flask_login import login_required
from SIMS import db, app
from SIMS.models import School

bp = Blueprint('school_list', __name__)

with app.app_context():
    db.create_all()

@bp.route('/school_list')
@login_required
def school_list():
    schools = School.query.all()
    schools = [school.getData() for school in schools]
    return render_template('school_list.html', schools=schools)