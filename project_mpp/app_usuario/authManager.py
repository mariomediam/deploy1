from django.contrib.auth.models import BaseUserManager


class ManejoUsuarios(BaseUserManager):
    print('')
    print("************************** ManejoUsuarios2 ********************")
    print('')
    def test_user(self, username):        
        return username

    def is_password_usable(self, encoded_password):
        print("")
        print("**************************** is_password_usable2 **************")
        print("")
        return True