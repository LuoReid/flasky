import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
  SECRET_KEY=os.environ.get('SECRE_KEY') or 'hard to guess string:)'
  SQLALCHEMY_COMMIT_ON_TEARDOWN = True
  FLASKY_MAIL_SUBJECT_PREFIX = '[Flasky]'
  FLASKY_MAIL_SENDER = 'Flasky Admin<42113805@qq.com>'
  FLASKY_ADMIN=os.environ.get('FLASKY_ADMIN') or 'test@dev.com'
  FLASKY_POSTS_PER_PAGE=10
  FLASKY_COMMENTS_PER_PAGE=10

  @staticmethod
  def init_app(app):
    pass

class DevelopmentConfig(Config):
  DEBUG = True
  MAIL_SERVER = 'smtp.qq.com'
  MAIL_PORT =587
  MAIL_USE_TLS=True
  MAIL_USERNAME=os.environ.get('MAIL_USERNAME') or '42113805@qq.com'
  MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
  SQLALCHEMY_DATABASE_URI=os.environ.get('DEV_DB_URL') or \
    'sqlite:///{}'.format(os.path.join(basedir,'data.sqlite'))
class TestingConfig(Config):
  TESTING = True
  SQLALCHEMY_DATABASE_URI=os.environ.get('TEST_DB_URL') or \
    'sqlite:///{}'.format(os.path.join(basedir,'data.sqlite'))

class ProductionConfig(Config):
  SQLALCHEMY_DATABASE_URI=os.environ.get('PRO_DB_URL') or \
    'sqlite:///{}'.format(os.path.join(basedir,'data.sqlite'))

config = {
  'development':DevelopmentConfig,
  'testing':TestingConfig,
  'production':ProductionConfig,
  'default':DevelopmentConfig
}