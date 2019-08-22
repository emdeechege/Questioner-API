import os
from app import create_app
from instance.config import app_config

app = create_app(app_config['development'])
"""defining the configuration to be used"""


if __name__ == '__main__':
    app.run()
