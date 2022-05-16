from flask import Flask, render_template, request
from flask_pymongo import PyMongo
#from application import routes
# print a nice greeting.
def say_hello(username = "World"):
    return '<p>Hello %s!</p>\n' % username

# some bits of text for the page.
header_text = '''
    <html>\n<head> <title>EB Flask Test</title> </head>\n<body>'''
instructions = '''
    <p><em>Hint</em>: This is a RESTful web service! Append a username
    to the URL (for example: <code>/Thelonious</code>) to say hello to
    someone specific.</p>\n'''
home_link = '<p><a href="/">Back</a></p>\n'
footer_text = '</body>\n</html>'

def indexfx():
    return render_template('base.html', title='Homeee', current_weight=0, min_weight=0)


# EB looks for an 'application' callable by default.
application = Flask(__name__, template_folder='./application/templates')
application.config["MONGO_URI"] = 'mongodb+srv://adao:altron88@handshake.xpbcd.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
mongo = PyMongo(application)
db = mongo.db
from application import routes
# add a rule for the index page.

@application.route('/update_min', methods=["POST"])
def update_min():
    req = request.form 
    weight = req['min_weight']
    db.scale.update_one({"name": "scale"}, {"$set": {"min_weight":weight}})
    result = db.scale.find_one({"name":"scale"})
    cur_weight = result['weight']
    email = result['email']
    item = result['item']
    return render_template('base.html', title='IoT Scale', current_weight=cur_weight, min_weight=weight, email=email,item=item)

@application.route('/update_email', methods=["POST"])
def update_email():
    req = request.form 
    email = req['email']
    db.scale.update_one({"name": "scale"}, {"$set": {"email":email}})
    result = db.scale.find_one({"name":"scale"})
    cur_weight = result['weight']
    email = result['email']
    min_weight = result['min_weight']
    return render_template('base.html', title='IoT Scale', current_weight=cur_weight, min_weight=min_weight, email=email)


@application.route('/post_weight/<string:weight>', methods=["GET"])
def update_weight(weight):
    new_weight = int(weight)
    db.scale.update_one({"name": "scale"}, {"$set": {"weight":new_weight}})
    return weight

@application.route('/update_item', methods=["POST"])
def update_item():
    req = request.form 
    item = req['item']
    db.scale.update_one({"name": "scale"}, {"$set": {"item":item}})
    result = db.scale.find_one({"name":"scale"})
    cur_weight = result['weight']
    weight = result['weight']
    email = result['email']
    return render_template('base.html', title='IoT Scale', current_weight=cur_weight, min_weight=weight, item=item, email=email)

@application.route('/')
def index():
    result = db.scale.find_one({"name":"scale"})
    cur_weight = result['weight']
    min_weight = result['min_weight']
    item = result['item']
    email = result['email']
    return render_template('base.html', title='IoT Scale', current_weight=cur_weight, min_weight=min_weight, item=item, email=email)
   
@application.route('/registration', methods=["GET", "POST"])
def registration():
    if request.method == "GET":
        return render_template('registration.html')
    elif request.method == "POST":
        req = request.form
        result = req
        print(req)
        print (result['email'])
        return 'hello'
    

# add a rule when the page is accessed with a name appended to the site
# URL.
application.add_url_rule('/hello/<username>', 'hello', (lambda username:
    header_text + say_hello(username) + home_link + footer_text))

# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()