from src.Authentication.authentication_handler import AuthenticationHandler
from quickbooks import QuickBooks


class QuickBooksFactory:
    def __init__(self, auth_handler: AuthenticationHandler):
        self.auth_handler = auth_handler

    def init_client(self):
        auth_client = self.auth_handler.auth_client
        quickbooks_client = QuickBooks(auth_client=auth_client, refresh_token=auth_client.refresh_token,
                                       company_id=auth_client.realm_id)
        return quickbooks_client
