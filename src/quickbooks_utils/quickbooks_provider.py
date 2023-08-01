import json

import quickbooks.objects.account
from quickbooks import QuickBooks

from src.models.account_DTO import AccountDTO


class QuickBooksProvider:
    def __init__(self, quickbooks_client: QuickBooks):
        self.account = quickbooks.objects.account.Account
        self.quickbooks_client = quickbooks_client

    def get_accounts(self):
        accounts = self.account.all(qb=self.quickbooks_client)

        accounts_models = [AccountDTO(account).__dict__ for account in accounts]
        return json.dumps(accounts_models)
