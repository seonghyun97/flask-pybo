from logging.config import dictConfig
from config.default import *

dictConfig({
    'version' : 1,
    'formatters' : {
        'default' : {
            'format' : '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
        }
    },

    'handlers' : {
        'file' :{
            'level' : 'INFO',
            'class' : 'logging.handlers.RotatingFileHandler',
            'filename' : os.path.join(BASE_DIR, 'logs/myproject.log'),
            'maxBytes' : 1024*1024*5, #5 MB
            'backupCount': 5,
            'formatter' : 'default',
        },
    },

    'root' : {
        'level' : 'INFO',
        'handlers' : ['file']
    }
})


SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x10\xdc\xeez\xba\x88\x9bZIT\xe3\x00\xd7\xfe+0'