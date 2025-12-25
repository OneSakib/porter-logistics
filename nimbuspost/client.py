"""Main SDK client for NimbusPost"""

from nimbuspost.auth import EShopBoxAuth
from nimbuspost.api.orders import OrdersAPI
# Import other API modules...


class NimbusPost:
    """
    Main SDK class for NimbusPost API

    Example:
        >>> sdk = NimbusPost(
        ...     workspace="myshop",
        ...     client_id="client_id",
        ...     client_secret="secret",
        ...     refresh_token="token"
        ... )
        >>> orders = sdk.orders.get_all()
    """

    def __init__(
        self,
        workspace: str,
        client_id: str,
        client_secret: str,
        refresh_token: str
    ):
        """
        Initialize NimbusPost

        Args:
            workspace: Your NimbusPost workspace name
            client_id: Your API client ID
            client_secret: Your API client secret
            refresh_token: Your API refresh token
        """
        self.workspace = workspace
        self.auth = EShopBoxAuth(client_id, client_secret, refresh_token)

        # Initialize API modules
        self.orders = OrdersAPI(workspace, self.auth)
