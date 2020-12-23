from flask import (
    Blueprint,
    request, 
    render_template,
    session, 
    redirect, 
    flash,
    url_for
    )
import bcrypt
import datetime
from bson import ObjectId
from flask_login import current_user, login_user, logout_user, login_required

from .models import mongo,login_manager, User
from .forms import Login, Signup, Reset

auth = Blueprint(
    'auth',
    __name__,
    url_prefix='/auth',
    template_folder='templates')


@login_manager.user_loader
def load_user(username):
    user_db = mongo.db.users.find_one({"username": username})
    if not user_db:
        return None
    return User(username=user_db['username'])



@auth.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('auth.protectedRoute'))
    form = Login()
    if form.validate_on_submit():
        user_db = mongo.db.users.find_one({'username': form.username.data})
        if user_db and User.check_password(user_db['password'], form.password.data.encode('utf-8')):
            user_obj = User(username=user_db['username']) 
            login_user(user_obj, remember=True, duration=datetime.timedelta(days=10))
            return redirect(url_for('auth.protectedRoute'))
        else:
            flash('Invalid Credentials...!','danger')
    # print('Datas Usn:{} Pass:{} '.format(form.username.data, form.password.data))
    # print(form.errors)
    return render_template('auth/login.html', form = form)



@auth.route('/signup', methods=['GET','POST'])
def signup():
    form = Signup()
    if request.method == 'POST':
        users_db = mongo.db.users
        
        userCheck = users_db.find_one({'username': form.username.data})
        if userCheck:
            flash('Username already Exists..!','danger')
            return redirect(url_for('auth.signup'))

        password = form.password.data.encode('utf-8')
        hashedPassword = bcrypt.hashpw(password, bcrypt.gensalt())

        users_db.insert_one({
            'name': form.name.data,
            'username': form.username.data,
            'password': hashedPassword,
            'admin': False
        })
        flash('Successfully Signed Up','success')
        return redirect(url_for('auth.login'))
    # print(form.errors)
    return render_template('auth/signup.html', form = form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Successfully Logged Out...', 'success')
    return redirect(url_for('auth.login'))


@auth.route('/user/delete/<user_id>')
@login_required
def delete_user(user_id):
    user_db = mongo.db.users
    userCheck = user_db.find_one({'_id': ObjectId(user_id)})
    if not userCheck:
        flash('Invalid User Id', 'info')
        return redirect(url_for('auth.signup'))
    user_db.delete_one({'_id': ObjectId(user_id)})
    flash('User Deleted Successfully', 'success')
    return redirect(url_for('auth.signup'))


@auth.route('/user/password_reset/<user_id>', methods= ['GET', 'POST'])
@login_required
def pwd_reset(user_id):
    form = Reset()
    if request.method == 'POST':
        user_db = mongo.db.users.find_one({'_id': ObjectId(user_id)})
        if user_db: 
            new_pasword = form.password.data.encode('utf-8')
            new_pasword_hashed = bcrypt.hashpw(new_pasword, bcrypt.gensalt())
            update = mongo.db.users.update_one({'_id': ObjectId(user_id)}, {'$set':{'password': new_pasword_hashed}})
            flash('Password Update Successful', 'success')
            return redirect(url_for('auth.adminPanel'))
        flash('User Id not Found', 'danger')
        return redirect(url_for('auth.adminPanel'))
        
    return render_template('auth/pwd_reset.html', form = form, user_id = user_id)


@auth.route('/admin-panel')
@login_required
def adminPanel():
    if current_user.is_admin() :
        all_users = mongo.db.users.find({})
        return render_template('auth/admin-panel.html', all_users = all_users)
    return render_template('errors/not_Admin.html')


@auth.route('/protected-route')
@login_required
def protectedRoute():
    return render_template('auth/protected-route.html')