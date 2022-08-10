def get_logger_config():
    return {
        "version": 1,
        "formatters": {"default": {
            "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s"
        }},
        "handlers": {"wsgi": {
            "class": "logging.StreamHandler",
            "stream": "ext://flask.logging.wsgi_errors_stream",
            "formatter": "default"
        }},
        "root": {
            "level": "INFO",
            "handlers": ["wsgi"]
        }
    }


def get_db_config():
    return [
        {
            'TableName': 'users',
            'KeySchema': [dict(AttributeName='email', KeyType='HASH')],
            'AttributeDefinitions': [dict(AttributeName='email', AttributeType='S')],
            'ProvisionedThroughput': dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
        }, {
            'TableName': 'messages',
            'KeySchema': [dict(AttributeName='id', KeyType='HASH')],
            'AttributeDefinitions': [dict(AttributeName='id', AttributeType='S')],
            'ProvisionedThroughput': dict(ReadCapacityUnits=5, WriteCapacityUnits=5)
        }
    ]
