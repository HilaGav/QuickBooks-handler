from flask import Flask, redirect, request
from src.Authentication.authentication_handler import AuthenticationHandler
from src.quickbooks.quickbooks_provider import QuickBooksProvider
from quickbooks.objects.account import Account
from src.quickbooks.quikbooks_factory import QuickBooksFactory


class QuickBooksApp:
    def __init__(self):
        self.app = Flask(__name__)
        self.auth_handler = AuthenticationHandler()
        self.quickbooks_factory = QuickBooksFactory(self.auth_handler)
        self.app.route('/login')(self.login)
        self.app.route('/auth-callback')(self.auth_callback)
        self.app.route('/get_accounts')(self.get_accounts)
        self.quickbooks_provider = None

    def login(self):
        return redirect(self.auth_handler.auth_url)

    def auth_callback(self):
        auth_code = request.args.get('code')
        realm_id = request.args.get('realmId')
        self.auth_handler.add_token(auth_code, realm_id)
        quickbooks_client = self.quickbooks_factory.init_client()
        self.quickbooks_provider = QuickBooksProvider(quickbooks_client, Account)
        return ''

    def get_accounts(self):
        accounts = self.quickbooks_provider.get_accounts()
        return accounts

    def run(self):
        self.app.run()


if __name__ == '__main__':
    app = QuickBooksApp()
    app.run()
