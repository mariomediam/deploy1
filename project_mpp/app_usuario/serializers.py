from rest_framework_simplejwt.serializers import TokenObtainSerializer
from app_usuario.auth import MyBackend
from rest_framework import exceptions

class CustomTokenObtainSerializer(TokenObtainSerializer):
    def validate(self, attrs):
        authenticate_kwargs = {
            self.username_field: attrs[self.username_field],
            'password': attrs['password'],
        }
        try:
            authenticate_kwargs['request'] = self.context['request']
        except KeyError:
            pass

        print("*************************authenticate_kwargs***********************************")
        print(authenticate_kwargs)
        my_backend = MyBackend()
        self.user = my_backend.authenticate(**authenticate_kwargs)
        print(self.user) # --> None

        if self.user is None or not self.user.is_active:
            self.error_messages['no_active_account'] = _(
                'No active account found with the given credentials') # --> *
            raise exceptions.AuthenticationFailed(
                self.error_messages['no_active_account'],
                'no_active_account',
            )


        return {}

class CustomTokenObtainPairSerializer(CustomTokenObtainSerializer):
    pass
    # @classmethod
    # def get_token(cls, user):
    #     return RefreshToken.for_user(user)

    # def validate(self, attrs):
    #     data = super().validate(attrs)

    #     refresh = self.get_token(self.user)

    #     data['refresh'] = str(refresh)
    #     data['access'] = str(refresh.access_token)

    #     if api_settings.UPDATE_LAST_LOGIN:
    #         update_last_login(None, self.user)

    #     return data