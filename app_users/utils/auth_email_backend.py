from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from app_users.models import User

# Email backend for get email form reset password
class EmailBackend(ModelBackend):
    def authenticate(self, request, username, password, **kwargs):
        print("Custom auth ... " + username)
        user = None
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            is_wrong_password = not user.check_password(password)
            
            if is_wrong_password: 
                raise Exception("Wrong password")
        except:
            return None
        return user

    def get_user(self, user_id: int):
        user = None
        try:
            user = User.objects.get(id=user_id)
            
        except:
            return None
        return user
