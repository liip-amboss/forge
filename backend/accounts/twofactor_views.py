import pyotp as pyotp
from django.conf import settings
from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework.views import APIView


@method_decorator(
    name='post',
    decorator=swagger_auto_schema(operation_summary='Activate 2FA for the current user with a verify token',
                                  responses={
                                      '204': '2FA activated',
                                      '400': 'Wrong verify token',
                                      '401': 'Not authenticated',
                                  },
                                  tags={'2FA'})
)
class Activate2FA(APIView):
    """
    This view activates the two factor authentication for the authenticated user if the verify code is valid
    """

    def post(self, request, *args, **kwargs):
        if not request.user:
            return Response(status=401)

        code = request.data['code']

        verified = pyotp.totp.TOTP(request.user.two_factor_secret).verify(code)

        if not verified:
            return Response(status=400)

        request.user.two_factor_active = True
        request.user.save()

        return Response(status=204)


@method_decorator(
    name='post',
    decorator=swagger_auto_schema(operation_summary='Deactivate 2FA for the current user',
                                  responses={
                                      '204': '2FA deactivated',
                                      '401': 'Not authenticated',
                                  },
                                  tags={'2FA'})
)
class Deactivate2FA(APIView):
    """
    This view deactivates the two factor authentication for the authenticated user
    """

    def post(self, request, *args, **kwargs):
        if not request.user:
            return Response(status=401)

        request.user.two_factor_active = False
        request.user.two_factor_secret = None
        request.user.save()

        return Response(status=204)


@method_decorator(
    name='get',
    decorator=swagger_auto_schema(operation_summary='Get information for showing the 2FA qr code',
                                  responses={
                                      '200': 'Information for showing the 2FA qr code',
                                      '401': 'Not authenticated',
                                  },
                                  tags={'2FA'})
)
class Get2FAUrl(APIView):
    """
    This view returns the qr code url and the generated secret for the two factor authentication
    """

    def get(self, request, *args, **kwargs):
        if not request.user:
            return Response(status=401)

        secret = pyotp.random_base32()

        request.user.two_factor_secret = secret
        request.user.save()

        url = pyotp.totp.TOTP(secret).provisioning_uri(name=request.user.email, issuer_name=settings.TWOFACTOR_ISSUER)

        return Response(status=200, data={'url': url, 'secret': secret})
