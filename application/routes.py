from flask import render_template, send_from_directory, Flask
from application import app
from .weight import add_weight_point
#from .plot_weight import plot_weight
#from __main__ import application

#application = Flask(__name__)

@app.route('/')
@app.route('/testing')
def test():
    return render_template('index.html', title='Home')

@app.route('/images/<path:path>')
def send_image(path):
    return send_from_directory('images', path)

@app.route('/post_weight/<string:weight>')
def post_weight(weight):
    #add_weight_point(weight)
    #plot_weight()
    return "weight posted"
