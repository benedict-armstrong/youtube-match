import uuid, os

import httplib2
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow

CLIENT_SECRETS_FILE = "client_secrets.json"

# This OAuth 2.0 access scope allows for full read/write access to the
# authenticated user's account.
YOUTUBE_READ_WRITE_SCOPE = "https://www.googleapis.com/auth/youtube"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

MISSING_CLIENT_SECRETS_MESSAGE = """
WARNING: Please configure OAuth 2.0

To make this sample run you will need to populate the client_secrets.json file
found at:

with information from the Developers Console
https://console.developers.google.com/

For more information about the client_secrets.json file format, please visit:
https://developers.google.com/api-client-library/python/guide/aaa_client_secrets
""".format(os.path.abspath(os.path.join(os.path.dirname(__file__),
                                        CLIENT_SECRETS_FILE)))

def get_authenticated_service():
    # Create a Storage instance to store and retrieve a single
    # credential to and from a file. Used to store the
    # oauth2 credentials for the current python script.

    secret = uuid.uuid4()
    print(secret)

    storage = Storage("credentials-{}".format(secret)) #"{}-oauth2.json".format(sys.argv[0]))
    credentials = storage.get()

    # Validate the retrieved oauth2 credentials
    if credentials is None or credentials.invalid:
        # Create a Flow instance from a client secrets file
        flow = flow_from_clientsecrets(CLIENT_SECRETS_FILE,
                                       scope=YOUTUBE_READ_WRITE_SCOPE,
                                       message=MISSING_CLIENT_SECRETS_MESSAGE)
        # The run_flow method requires arguments.
        # Initial default arguments are setup in tools, and any
        # additional arguments can be added from the command-line
        # and passed into this method.
        args = argparser.parse_args()
        # Obtain valid credentials
        credentials = run_flow(flow, storage, args)

    # Build and return a Resource object for interacting with an YouTube API
    return build(YOUTUBE_API_SERVICE_NAME,
                 YOUTUBE_API_VERSION,
                 http=credentials.authorize(httplib2.Http()))

