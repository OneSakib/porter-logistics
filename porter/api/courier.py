from .base import Resource
from ..constants.url import URL


class Courier(Resource):
    def __init__(self, client=None):
        super(Courier, self).__init__(client)

    def get_quote(self, data={}, **kwargs):
        url = URL.GET_QUOTE
        return self.post_url(url, data, **kwargs)

    def create_order(self, data={}, **kwargs):
        url = f"{URL.ORDER}/create"
        return self.post_url(url, data, **kwargs)

    def track_order(self, order_id, data={}, **kwargs):
        url = f"{URL.ORDER}/{order_id}"
        return self.get_url(url, data, **kwargs)

    def cancel_order(self, order_id, data={}, **kwargs):
        url = f"{URL.ORDER}/{order_id}/cancel"
        return self.get_url(url, data, **kwargs)

