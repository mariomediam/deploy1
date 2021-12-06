from rest_framework_simplejwt.authentication import JWTAuthentication

class myAuthentication(JWTAuthentication):

    def authenticate(self, request):
        print("")
        print("*************************** auhtenticate ***************************")
        print("")
        super.authenticate(request)
        


