from flask import Blueprint, redirect
from flask_login import login_required

bp = Blueprint('index', __name__)

@bp.route('/')
@login_required
def index():
    return redirect('/school_list')