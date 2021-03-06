from flask import Flask
from config import Config

app = Flask(__name__)
app._static_folder = 'images'
app.config.from_object(Config)

import application.routes
#from application import routes

