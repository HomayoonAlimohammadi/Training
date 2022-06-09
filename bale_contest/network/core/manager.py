from django.contrib.auth.base_user import BaseUserManager 


class CustomeUserManager(BaseUserManager):

    def create_user(self, username, **extra_fields):
        if not username:
            raise ValueError('username can not be empty.')

        user = self.model(username=username, **extra_fields)
        user.set_password('password')
        user.save()
        return user 

    def create_superuser(self, username, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(username, **extra_fields)