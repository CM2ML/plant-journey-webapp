import os

# Load environmental variables from .env in development stage
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
	DEBUG = False
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'sdfhuethu39efgj!jfjegjh59s'
	SQLALCHEMY_RECORD_QUERIES = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class StagingConfig(Config):
	DEVELOPMENT = True
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')


class DevelopmentConfig(Config):
	DEVELOPMENT = True
	DEBUG = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')


class TestingConfig(Config):
	TESTING = True


config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'staging': StagingConfig,
	'production': ProductionConfig,
	'default': DevelopmentConfig
}