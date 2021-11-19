import pyotp
from django.urls import reverse


def test_login(user_factory, api_client):
    pw = "blah"
    user = user_factory(password=pw)

    url = reverse('token_obtain_pair')

    data = {'email': user.email, 'password': pw}

    response = api_client.post(url, data)

    content = response.json()

    assert response.status_code == 200
    assert content['id'] == user.id


def test_login_inactive_user(user_factory, api_client):
    pw = "blah"
    user = user_factory(password=pw, is_active=False)

    url = reverse('token_obtain_pair')

    data = {'email': user.email, 'password': pw}

    response = api_client.post(url, data)
    assert response.status_code == 401


def test_login_two_factor(user_factory, api_client):
    pw = "blah"
    user = user_factory(password=pw, two_factor_active=True, two_factor_secret='Forge')

    url = reverse('token_obtain_pair')

    data = {'email': user.email, 'password': pw}

    response = api_client.post(url, data)
    assert response.status_code == 204


def test_login_two_factor_with_token(user_factory, api_client):
    pw = "blah"
    two_factor_secret = 'Forge'
    user = user_factory(
        password=pw, two_factor_active=True, two_factor_secret=two_factor_secret
    )

    url = reverse('token_obtain_pair')

    data = {
        'email': user.email,
        'password': pw,
        'token': pyotp.TOTP(two_factor_secret).now(),
    }

    response = api_client.post(url, data)
    assert response.status_code == 200


def test_login_two_factor_with_invalid_token(user_factory, api_client):
    pw = "blah"
    two_factor_secret = 'Forge'
    user = user_factory(
        password=pw, two_factor_active=True, two_factor_secret=two_factor_secret
    )

    url = reverse('token_obtain_pair')

    data = {'email': user.email, 'password': pw, 'token': 'Some token'}

    response = api_client.post(url, data)
    assert response.status_code == 401
