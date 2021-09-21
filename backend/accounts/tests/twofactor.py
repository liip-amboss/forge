import pyotp
from django.urls import reverse
from accounts.models import User
from app import settings


def test_2fa_url(user_factory, api_client):
    user = user_factory()

    api_client.authorize(user)

    url = reverse('2fa-url')

    response = api_client.get(url)

    content = response.json()

    url = pyotp.totp.TOTP(content['secret']).provisioning_uri(
        name=user.email, issuer_name=settings.TWOFACTOR_ISSUER
    )

    assert content['secret'] == User.objects.get(id=user.id).two_factor_secret
    assert content['url'] == url


def test_2fa_url_unauthorized(api_client):
    url = reverse('2fa-url')

    response = api_client.get(url)

    assert response.status_code == 401


def test_activate_2fa(user_factory, api_client):
    two_factor_secret = 'Forge'
    user = user_factory(two_factor_secret=two_factor_secret)

    api_client.authorize(user)

    url = reverse('activate-2fa')

    twofactor_code = pyotp.TOTP(user.two_factor_secret).now()

    data = {'code': twofactor_code}

    response = api_client.post(url, data)

    assert response.status_code == 204
    assert User.objects.get(id=user.id).two_factor_active is True


def test_activate_2fa_wrong_code(user_factory, api_client):
    two_factor_secret = 'Forge'
    user = user_factory(two_factor_secret=two_factor_secret)

    api_client.authorize(user)

    url = reverse('activate-2fa')

    twofactor_code = 'Wrong code'

    data = {'code': twofactor_code}

    response = api_client.post(url, data)

    assert response.status_code == 400
    assert User.objects.get(id=user.id).two_factor_active is False


def test_active_2fa_unauthorized(api_client):
    url = reverse('activate-2fa')

    response = api_client.post(url)

    assert response.status_code == 401


def test_deactivate_2fa(user_factory, api_client):
    two_factor_secret = 'Forge'
    user = user_factory(two_factor_secret=two_factor_secret, two_factor_active=True)

    api_client.authorize(user)

    url = reverse('deactivate-2fa')

    response = api_client.post(url)

    updated_user = User.objects.get(id=user.id)

    assert response.status_code == 204
    assert updated_user.two_factor_secret is None
    assert updated_user.two_factor_active is False


def test_deactive_2fa_unauthorized(api_client):
    url = reverse('deactivate-2fa')

    response = api_client.post(url)

    assert response.status_code == 401
