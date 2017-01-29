from flask import Flask
from datetime import datetime

app = Flask(__name__)

from app import views

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
