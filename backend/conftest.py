import pytest
from tests.api_client import ForgeApiClient
from pytest_factoryboy import register
from accounts import factories as account_factories


@pytest.fixture(autouse=True)
def enable_db(db):
    pass


@pytest.fixture
def api_client():
    return ForgeApiClient()


register(account_factories.UserFactory)
