from intuitlib.client import AuthClient
from src.common.config import AuthenticationConfiguration as authConfig


class AuthenticationHandler:
    def __init__(self):
        self.auth_client = AuthClient(authConfig.client_id, authConfig.client_secret, authConfig.redirect_uri,
                                      authConfig.environment)
        self.auth_url = self.auth_client.get_authorization_url([authConfig.scope])

    def add_token(self, auth_code, realm_id):
        self.auth_client.get_bearer_token(auth_code, realm_id=realm_id)
