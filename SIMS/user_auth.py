from flask_login import LoginManager, login_user, logout_user
from SIMS import app
from SIMS.models import User

login_manager = LoginManager()
login_manager.init_app(app)

class UserAuth:
    def is_valid_user(user_id, password):
        users = User.query.all()
        users = [user.getData() for user in users]
        for user in users:
            if user['user_id'] == user_id and user['password'] == password:
                return True
        return False

    def login_user(user_id):
        login_user(User.query.filter_by(user_id=user_id).first())
    
    def logout_user():
        logout_user()
        
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)
