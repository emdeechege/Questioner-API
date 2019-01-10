from app import create_app
"""this is imported from the __init__.py file contained in the subdirectory called app"""
"""app initializer """
import os
"""you import this to get all that we had defined and exported in the .env"""

config_name = os.getenv("APP_SETTINGS")
"""Gets the app settings defined in the .env file"""
app = create_app()
"""defining the configuration to be used"""


@app.route('/')
def hello_world():
    return 'Hello Questioner!'


if __name__ == '__main__':
    app.run()
