from django.contrib.auth.backends import BaseBackend
from app_usuario.models import UsuarioModel
# BaseBackend ModelBackend
class MyBackend(BaseBackend):
    print("")
    print("*************************** MyBackend ********************")
    print("")
    def authenticate(self, request, username=None, password=None):
        print('')
        print("************************** authenticateaaa ********************")
        print(username)
        print(password)
        print('01')
        if username is None:
            return None

        miUsuario = UsuarioModel.objects.get(pk=username)
        print(miUsuario)
        # miUsuario.set_unusable_password()
        print('02')
        return miUsuario

    def get_user(self, username):
        try:
            return UsuarioModel.objects.get(pk=username)
        except Exception:
            print("Error")
            return None

