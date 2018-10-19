## Broker settings.
broker_url = 'amqp://localhost//'

# List of modules to import when the Celery worker starts.
imports = ('suziScraper.tasks')

## Using the database to store task state and results.
result_backend = 'redis://localhost'

task_annotations = {'tasks.add': {'rate_limit': '10/s'}}

# List of modules to import when celery starts.
CELERY_IMPORTS = ("suziScraper.tasks", )

CELERY_RESULT_BACKEND = "redis"
REDIS_HOST = "localhost"
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_CONNECT_RETRY = True

## Result store settings.
CELERY_RESULT_DBURI = "sqlite:///mydatabase.db"

## Broker settings.
BROKER_HOST = "localhost"
BROKER_PORT = 5672
BROKER_VHOST = "/"
BROKER_USER = "guest"
BROKER_PASSWORD = "guest"

## Worker settings
CELERYD_CONCURRENCY = 8
# CELERYD_LOG_FILE = "celeryd.log"
# CELERYD_LOG_LEVEL = "INFO"

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
enable_utc = True
