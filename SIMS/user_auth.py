from flask_login import LoginManager, login_user, logout_user
from werkzeug.security import check_password_hash
from SIMS import app
from SIMS.models import User

login_manager = LoginManager()
login_manager.init_app(app)

class UserAuth:
    def is_valid_user(user_id, password):
        user = User.query.filter_by(user_id=user_id).first()
        if user and check_password_hash(user.password, password):
            return True
        return False

    def login_user(user_id):
        login_user(User.query.filter_by(user_id=user_id).first())
    
    def logout_user():
        logout_user()
        
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
