from flask import Blueprint, render_template, request

bp = Blueprint('admin_panel', __name__)

# 生徒登録画面
@bp.route('/admin_panel', methods=['GET', 'POST'])
def admin_panel():
    if request.method == 'POST':
        type = request.form.get('type')
        
    else:
        return render_template('admin_panel.html')
