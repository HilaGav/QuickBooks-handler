import unittest
from datetime import datetime
from unittest.mock import Mock
from unittest.mock import patch

from quickbooks.objects import Account
from src.authentication.authentication_handler import AuthenticationHandler
from src.quickbooks_utils.quickbooks_provider import QuickBooksProvider
from src.quickbooks_utils.quikbooks_factory import QuickBooksFactory


class TestQuickBooksProvider(unittest.TestCase):
    def setUp(self):
        self.account_number = datetime.now().strftime('%d%H%M')
        self.name = f"Test Account {self.account_number}"
        self.mock_auth_client = self.create_mock_auth_client()

    @staticmethod
    def create_mock_account():
        account = Account()
        account.AccountType = 'test'
        account.Active = False
        account.Name = 'hila test'
        account.Description = 'should not appear'
        return account

    @staticmethod
    def create_mock_auth_client():
        mock_auth_client = Mock()
        mock_auth_client.refresh_token = "mock_refresh_token"
        mock_auth_client.realm_id = "mock_realm_id"
        return mock_auth_client

    @patch('quickbooks.objects.Account.all')
    def test_get_accounts(self, mock_all):
        account = self.create_mock_account()
        mock_auth_handler = Mock(spec=AuthenticationHandler)
        mock_auth_handler.auth_client = self.mock_auth_client

        mock_all.return_value = [account]

        factory = QuickBooksFactory(auth_handler=mock_auth_handler)
        client = factory.init_client()

        provider = QuickBooksProvider(client)
        results = provider.get_accounts()

        expected_result = '[{"name": "hila test", "classification": null, "currency_ref": null, "account_type": ' \
                          '"test", "active": false, "current_balance": null}]'
        self.assertEqual(results, expected_result)

    @patch('quickbooks.objects.Account.all')
    def test_get_accounts_when_account_empty_return_empty_array(self, mock_all):
        account = self.create_mock_account()
        mock_auth_handler = Mock(spec=AuthenticationHandler)
        mock_auth_handler.auth_client = self.mock_auth_client

        mock_all.return_value = []

        factory = QuickBooksFactory(auth_handler=mock_auth_handler)
        client = factory.init_client()

        provider = QuickBooksProvider(client)
        results = provider.get_accounts()

        assert results == '[]'


if __name__ == '__main__':
    unittest.main()
