from flask import Flask, redirect, request

from src.authentication.authentication_handler import AuthenticationHandler
from src.quickbooks_utils.quickbooks_provider import QuickBooksProvider
from src.quickbooks_utils.quikbooks_factory import QuickBooksFactory


class QuickBooksApp:
    def __init__(self, auth_handler_prm: AuthenticationHandler, quickbooks_factory_prm: QuickBooksFactory):
        self.app = Flask(__name__)
        self.auth_handler = auth_handler_prm
        self.quickbooks_factory = quickbooks_factory_prm
        self.app.route('/login')(self.login)
        self.app.route('/auth-callback')(self.auth_callback)
        self.app.route('/api/accounts')(self.get_accounts)
        self.quickbooks_provider = None

    def login(self):
        return redirect(self.auth_handler.auth_url)

    def auth_callback(self):
        auth_code = request.args.get('code')
        realm_id = request.args.get('realmId')
        self.auth_handler.add_bearer_token(auth_code, realm_id)
        quickbooks_client = self.quickbooks_factory.init_client()
        self.quickbooks_provider = QuickBooksProvider(quickbooks_client)
        return 'Login succeeded'

    def get_accounts(self):
        if self.quickbooks_provider is None:
            return "Please login", 401
        accounts = self.quickbooks_provider.get_accounts()
        return accounts

    def run(self):
        self.app.run()


if __name__ == '__main__':
    auth_handler = AuthenticationHandler()
    quickbooks_factory = QuickBooksFactory(auth_handler)
    app = QuickBooksApp(auth_handler, quickbooks_factory)
    app.run()
