from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


class ForgeApiClient(APIClient):
    """
    Decides if token is persisted between requests
    :type bool
    """

    persist_auth = False

    def authorize(self, user=None, persist_auth=False):
        """Authorize next request with jwt

        This generates a jwt for the user and automatically applies it to
        the next request. We explicitly clear the credentials again after the
        request to avoid having authorized requests when we don't expect them
        unless you set persist_auth to True

        :param   user: The user to generate jwt for
        :type    user: User
        :param   persist_auth: Keep the auth token between requests
        :type    persist_auth: Boolean
        """
        self.persist_auth = persist_auth

        # generate refresh and access token for user
        refresh = RefreshToken.for_user(user)
        token = refresh.access_token

        # set credentials for api client for next request(s)
        self.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')

        return user, refresh, token

    def put(self, *args, **kwargs):
        """Default format to json if not provided otherwise"""
        if 'format' not in kwargs:
            kwargs['format'] = 'json'

        return super().put(*args, **kwargs)

    def patch(self, *args, **kwargs):
        """Default format to json if not provided otherwise"""
        if 'format' not in kwargs:
            kwargs['format'] = 'json'

        return super().patch(*args, **kwargs)

    def post(self, *args, **kwargs):
        """Default format to json if not provided otherwise"""
        if 'format' not in kwargs:
            kwargs['format'] = 'json'

        return super().post(*args, **kwargs)
