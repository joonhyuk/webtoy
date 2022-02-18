from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x94\xae#\xa1\xcf \xd4\x9d}2\xbb\xc3,\xbb\x04\xd9'