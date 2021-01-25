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


SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='dbmasteruser',
    pw=' 12345678 ',
    url=' ls-60bd725f04b3f1f2544bb1b1cf438502ca63374a.cizmmhwwxovg.ap-northeast-2.rds.amazonaws.com',
    db='flask_pybo'
)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\x10\xdc\xeez\xba\x88\x9bZIT\xe3\x00\xd7\xfe+0'