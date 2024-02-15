from flask import Blueprint, render_template
from flask_login import login_required
from SIMS.models import School

bp = Blueprint('school_list', __name__)

@bp.route('/school_list')
@login_required
def school_list():
    schools = School.get_all()
    return render_template('school_list.html', schools=schools)