import os
from app import create_app

conf = os.getenv('FLASK_CONFIG') or 'default'
app = create_app(conf)

if __name__ == '__main__':
    app.run()