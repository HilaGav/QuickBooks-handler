import unittest
from datetime import datetime
from unittest.mock import Mock
from quickbooks.objects import Account
from src.authentication.authentication_handler import AuthenticationHandler
from src.quickbooks.quikbooks_factory import QuickBooksFactory


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.account_number = datetime.now().strftime('%d%H%M')
        self.name = "Test Account {0}".format(self.account_number)

    def test_init_client(self):
        # Create a mock AuthClient and set the required properties
        mock_auth_client = Mock()
        mock_auth_client.refresh_token = "mock_refresh_token"
        mock_auth_client.realm_id = "mock_realm_id"

        # Create a mock AuthenticationHandler and set the auth_client property
        mock_auth_handler = Mock(spec=AuthenticationHandler)
        mock_auth_handler.auth_client = mock_auth_client

        # Instantiate the QuickBooksFactory with the mock AuthenticationHandler
        factory = QuickBooksFactory(auth_handler=mock_auth_handler)

        # Call init_client()
        client = factory.init_client()

        # Assertions
        self.assertEqual(client.auth_client, mock_auth_client)
        self.assertEqual(client.refresh_token, "mock_refresh_token")
        self.assertEqual(client.company_id, "mock_realm_id")


if __name__ == '__main__':
    unittest.main()
