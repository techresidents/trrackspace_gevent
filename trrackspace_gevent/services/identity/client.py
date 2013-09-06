from trhttp_gevent.rest.client import GRestClient
from trrackspace.services.identity.client import IdentityServiceClient

class GIdentityServiceClient(IdentityServiceClient):
    """Gevent Rackspace identity service client."""

    def __init__(self,
            username,
            api_key=None,
            password=None,
            endpoint=None,
            timeout=10,
            retries=2,
            keepalive=True,
            proxy=None,
            rest_client_class=GRestClient,
            debug_level=0):
        """IdentityServiceClient constructor

        Args:
            username: Username to use for authentication
            api_key: Api key to use for authentication.
                This argument is not required if a password is used.
            password: Password to use for authentication.
                This argument is not required if an api_key is used.
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
            rest_client_class: optional RestClient class. If not 
                specified sensible default will be used.
            debug_level: httplib debug level. Setting this to 1 will log
                http requests and responses which is very useful for 
                debugging.
        """

        super(GIdentityServiceClient, self).__init__(
                username=username,
                api_key=api_key,
                password=password,
                endpoint=endpoint,
                timeout=timeout,
                retries=retries,
                keepalive=keepalive,
                proxy=proxy,
                rest_client_class=rest_client_class,
                debug_level=debug_level)
