from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError

class CustomProcessAdapter(DefaultAccountAdapter):
    # def clean_username(self,username):
    #     if len(username)>12:
    #         raise ValidationError('Please enter a username values less than the current one')
    #     return DefaultAccountAdapter.clean_username(self, username)

    def clean_email(self, email):
        RestrictedList=['test@test.com']
        if email in RestrictedList:
            raise ValidationError('Estas prohibido de registrarte. Porfavor contacte con el administrador')
        return email
    
    def clean_password(self, password):
        if len(password)>20:
            raise ValidationError("Por favor ingrese una contraseña que pueda recordar")
        return password