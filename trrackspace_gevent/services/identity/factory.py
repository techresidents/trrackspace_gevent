from trhttp_gevent.rest.client import GRestClient
from trpycore.factory.base import Factory
from trrackspace_gevent.services.identity.client import GIdentityServiceClient

class GIdentityServiceClientFactory(Factory):
    """Factory for creating GIdentityServiceClient objects."""

    def __init__(self,
            username=None,
            api_key=None,
            password=None,
            endpoint=None,
            timeout=10,
            retries=2,
            keepalive=True,
            proxy=None,
            rest_client_class=GRestClient,
            debug_level=0):
        """GIdentityServiceClientFactory constructor

        Args:
            username: Username to use for authentication with the Rackspace
                Identity Service. This argument is not required if 
                an identity_client argument is used.
            api_key: Api key to use for authentication with the Rackspace
                Identity Service. This argument is not required if a
                password or identity_client argument is used.
            password: Password to use for authentication with the Rackspace
                Identity Service. This argument is not required if an
                api_key or identity_client argument is used.
            endpoint: optional api endpoint
            timeout: socket timeout in seconds
            retries: Number of times to try a request with an unexpected
                error before an exception is raised. Note that a value of 2
                means to try each api request twice (not 3 times) before
                raising an exception.
            keepalive: boolean indicating whether connections to the
                cloudfiles servers should be maintained between requests.
                If false, connections will be closed immediately following
                each api request.
            proxy: (host, port) tuple specifying proxy for connection
            rest_client_class: optional GRestClient class. If not 
                specified sensible default will be used.
            debug_level: httplib debug level. Setting this to 1 will log
                http requests and responses which is very useful for 
                debugging.
        """
        self.username = username
        self.api_key = api_key
        self.password = password
        self.endpoint = endpoint
        self.timeout = timeout
        self.retries = retries
        self.keepalive = keepalive
        self.proxy = proxy
        self.rest_client_class = rest_client_class
        self.debug_level = debug_level
        self.username = username

    def create(self):
        """Return instance of GIdentityServiceClient object."""
        return GIdentityServiceClient(
                username=self.username,
                api_key=self.api_key,
                password=self.password,
                endpoint=self.endpoint,
                timeout=self.timeout,
                retries=self.retries,
                keepalive=self.keepalive,
                proxy=self.proxy,
                rest_client_class=self.rest_client_class,
                debug_level=self.debug_level)
