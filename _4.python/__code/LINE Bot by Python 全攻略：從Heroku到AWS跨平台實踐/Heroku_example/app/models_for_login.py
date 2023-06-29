from flask_login import UserMixin
from app import login_manager

class User(UserMixin):
    pass

@login_manager.user_loader
def user_loader(使用者):
    if 使用者 not in users_dict:
        return

    user = User()
    user.id = 使用者
    return user

@login_manager.request_loader
def request_loader(request):
    使用者 = request.form.get('user_id')
    if 使用者 not in users_dict:
        return

    user = User()
    user.id = 使用者

    user.is_authenticated = request.form['password'] == users_dict[使用者]['password']

    return user

users_dict = {'Me': {'password': 'myself'}}