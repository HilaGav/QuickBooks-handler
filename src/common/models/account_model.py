class AccountModel:
    def __init__(self, name, classification, currency_ref, account_type, active,
                 current_balance):
        self.name = name
        self.classification = classification
        self.currency_ref = currency_ref.__dict__
        self.account_type = account_type
        self.active = active
        self.current_balance = current_balance
