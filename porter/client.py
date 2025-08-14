from .api import courier as courier_b2b
from .api import courier
import requests
from .constants import HTTP_STATUS_CODE, ERROR_CODE, URL

import json
from .errors import (BadRequestError, GatewayError,
                     ServerError)


class Client:
    """Porter client class"""

    DEFAULTS = {
        'base_url': URL.BASE_URL
    }

    def __init__(self, session=None, api_key=None, **options):
        """
        Initialize a Client object with session,
        optional token handler, and options
        """
        self.session = session or requests.Session()
        self.base_url = self._set_base_url(**options)
        self.app_details = []
        self.API_KEY = api_key
        self.courier = courier.Courier(client=self)
        

    def _set_base_url(self, **options):
        base_url = self.DEFAULTS['base_url']

        if 'base_url' in options:
            base_url = options['base_url']
            del (options['base_url'])

        return base_url

    def _update_user_agent_header(self, options):
        user_agent = "{}{} {}".format('Porter-Python/', self._get_version(),
                                      self._get_app_details_ua())
        if 'headers' in options:
            options['headers']['X-API-KEY'] = self.API_KEY
            options['headers']['User-Agent'] = user_agent
        else:
            options['headers'] = {'User-Agent': user_agent}
            options['headers']['X-API-KEY'] = self.API_KEY

        return options

    def _get_version(self):
        version = "1.0.0"        
        return version

    def _get_app_details_ua(self):
        app_details_ua = ""

        app_details = self.get_app_details()

        for app in app_details:
            if 'title' in app:
                app_ua = app['title']
                if 'version' in app:
                    app_ua += "/{}".format(app['version'])
                app_details_ua += "{} ".format(app_ua)

        return app_details_ua

    def set_app_details(self, app_details):
        self.app_details.append(app_details)

    def get_app_details(self):
        return self.app_details

    def request(self, method, path, **options):
        """
        Dispatches a request to the Porter HTTP API
        """
        options = self._update_user_agent_header(options)

        url = "{}{}".format(self.base_url, path)
        response = getattr(self.session, method)(
            url, **options)        
        if ((response.status_code >= HTTP_STATUS_CODE.OK) and
                (response.status_code < HTTP_STATUS_CODE.REDIRECT)):
            return json.dumps({}) if (response.status_code == 204) else response.json()
        elif (response.status_code == HTTP_STATUS_CODE.UN_AUTHORIZED):
            msg = ERROR_CODE.MISSING_AUTH_TOKEN
            raise BadRequestError(msg)
        elif (response.status_code == HTTP_STATUS_CODE.BAD_REQUEST):
            msg = "Bad Request"
            raise BadRequestError(msg)
        else:
            return response.json()

    def get(self, path, params, **options):
        """
        Parses GET request options and dispatches a request
        """
        data, options = self._update_request({}, options)
        return self.request('get', path, params=params, **options)

    def post(self, path, data, **options):
        """
        Parses POST request options and dispatches a request
        """
        data, options = self._update_request(data, options)
        return self.request('post', path, data=data, **options)

    def patch(self, path, data, **options):
        """
        Parses PATCH request options and dispatches a request
        """
        data, options = self._update_request(data, options)
        return self.request('patch', path, data=data, **options)

    def delete(self, path, data, **options):
        """
        Parses DELETE request options and dispatches a request
        """
        data, options = self._update_request(data, options)
        return self.request('delete', path, data=data, **options)

    def put(self, path, data, **options):
        """
        Parses PUT request options and dispatches a request
        """
        data, options = self._update_request(data, options)
        return self.request('put', path, data=data, **options)

    def _update_request(self, data, options):
        """
        Updates The resource data and header options
        """
        data = json.dumps(data)

        if 'headers' not in options:
            options['headers'] = {}

        options['headers'].update({'Content-type': 'application/json'})

        return data, options

