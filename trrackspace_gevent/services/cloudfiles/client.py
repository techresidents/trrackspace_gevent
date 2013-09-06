from trhttp_gevent.rest.client import GRestClient
from trrackspace.services.cloudfiles.client import CloudfilesClient
from trrackspace_gevent.services.identity.client import GIdentityServiceClient

class GCloudfilesClient(CloudfilesClient):
    """GEvent Rackspace Cloudfiles API Client

    CloudfilesClient must be used in conjunction with an IdentityServiceClient.
    The identity_client is required for authentication and api endpoint
    lookups. If an identity_client is not explicitly passed to the construtor
    one will be created for you using the username and password/api_key.

    Example usage:
        client = GCloudfilesClient(username="user", password="...")
        or
        client = GCloudfilesClient(username="user", api_key="...")
        or
        identity_client = GIdentityServiceClient(username="user", password="...")
        client = GCloudfilesClient(identity_client=identity_client)
    """

    def __init__(self,
            username=None,
            api_key=None,
            password=None,
            region=None,
            servicenet=True,
            identity_client=None,
            identity_client_class=GIdentityServiceClient,
            timeout=10,
            retries=2,
            keepalive=True,
            proxy=None,
            rest_client_class=GRestClient,
            debug_level=0):
        """GCloudfilesClient constructor

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
            region: optional datacenter region to connect to, i.e. DFW.
                If region is not passed, the default region for the
                authenticated user will be used.
            servicenet: boolean indicating the Rackspace internal network,
                servicenet, should be used for requests. If running
                on Rackspace servers this is recommended since latency
                will be lowered and charges will not be incurred.
            identity_client: optional IdentityServiceClient to use for
                authentication and api endpoint lookup. If identity_client
                is not passed, one will be created for you using the
                username and password/api_key pair.
            identity_client_class: optional IdentityServiceClient class
                to use to construct identity_client if it's not given.
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
        
        super(GCloudfilesClient, self).__init__(
                username=username,
                api_key=api_key,
                password=password,
                region=region,
                servicenet=servicenet,
                identity_client=identity_client,
                identity_client_class=identity_client_class,
                timeout=timeout,
                retries=retries,
                keepalive=keepalive,
                proxy=proxy,
                rest_client_class=rest_client_class,
                debug_level=debug_level)
