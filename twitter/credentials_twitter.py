import os
from dotenv import load_dotenv

class CredentialsTwitter:

    def __init__(self):
        load_dotenv()
        self.API_KEY = os.getenv('API_KEY')
        self.API_SECRET_KEY = os.getenv('API_SECRET_KEY')
        self.BEARER = os.getenv('BEARER')