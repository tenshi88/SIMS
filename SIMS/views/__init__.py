from datetime import timedelta
from importlib import import_module
from flask import redirect, request, session
from SIMS import app
from SIMS.user_auth import login_manager
import os, glob

# 現在のファイルのディレクトリパスを取得します。
directory_path = os.path.dirname(os.path.abspath(__file__))

# 指定したディレクトリ内のすべての .py ファイルを再帰的に検索します。
py_files = glob.glob(directory_path + '/**/*.py', recursive=True)

for file in py_files:
    # __init__.pyは読み込まない
    if '__init__.py' in file:
        continue
    # ファイル名から拡張子を取り除いてモジュールをインポート
    module_name = os.path.splitext(os.path.relpath(file))[0].replace(os.sep, '.')
    module = import_module(module_name).bp
    app.register_blueprint(module)

# ログインが必要なページで未ログインの場合はログインページにリダイレクト
@login_manager.unauthorized_handler
def unauthorized():
    return redirect('/login')

@app.errorhandler(404) # 404エラーが発生した場合の処理
def error_404(_):
    if request.path != '/favicon.ico' or '/static/' in request.path:
        # favicon.icoや/static/配下のファイルはそのまま404エラーを返す
        return '404 Not Found', 404
    # それ以外の場合はトップページにリダイレクト
    return redirect('/')

# リクエストのたびにセッションの寿命を更新する
@app.before_request
def before_request():
    session.permanent = True
    #app.permanent_session_lifetime = timedelta(minutes=15) # セッションの寿命を15分に設定
    session.modified = True