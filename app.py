from flask import Flask, Blueprint, render_template
from flask_wtf import CSRFProtect

from views.models import mongo, login_manager

from views.auth import auth
from views.errors import errors

import views.errors as error

app = Flask(__name__)

# Enter your MongoDB URI here.
app.config['MONGO_URI'] = 'mongodb://localhost:27017/speedApp'

app.config['SECRET_KEY'] = 'jdn4mmyxaIkqjcuYrliR5ojf8Cfi6X'

mongo.init_app(app)

login_manager.login_view = 'auth.login'
login_manager.init_app(app)
CSRFProtect(app)


app.register_blueprint(auth)
app.register_blueprint(errors)
app.register_error_handler(404,error.page_not_found)

@app.route('/')
def index():
    return render_template('auth/index.html')

if __name__ == "__main__":
    app.run(debug = True)