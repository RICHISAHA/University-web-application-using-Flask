import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'<{G\xf6ep\xc2\x02|\xec\xd7\xad\xec\x9e\x84\r'

    MONGODB_SETTINGS={ 'db' : 'UTA_Enrollment' }