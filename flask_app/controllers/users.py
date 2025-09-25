from flask import render_template, request, redirect, session, flash
from flask_app import app
from flask_app.models import user
from flask_app.controllers import rides
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

# all GET routes
@app.route('/')
@app.route('/login')
def login_page():
    print('trying to render login')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/login')

#all POST routes
@app.route('/user/register', methods=['post'])
def create_user():
    if user.User.user_reg_is_valid(request.form):
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data = {
            'first_name' : request.form['first_name'].strip(), #the strip() here removes and leading or training spaces
            'last_name' : request.form['last_name'].strip(), #the strip() here removes and leading or training spaces
            'email' : request.form['email'].lower(), # notice the .lower() function here
            'password' : pw_hash
        }
        user_id = user.User.save(data)
        session['user_id'] = user_id
        session['user_name'] = request.form['first_name']
        return redirect('/ride/dashboard')
    else:
        session['first_name'] = request.form['first_name']
        session['last_name'] = request.form['last_name']
        session['email'] = request.form['email']
        session['password'] = request.form['password']
        session['confirm_password'] = request.form['confirm_password']
        return redirect('/login')

@app.route('/user/login', methods=['post'])
def login_user():
    session['login_email'] = request.form['email'].lower() #always make email all lowercase
    user_obj = user.User.get_one_by_email(request.form['email'].lower()) #always make email all lowercase
    if not user_obj: #check if bad email
        flash("There is no account with that email.","login")
        return redirect ("/login")
    elif not bcrypt.check_password_hash(user_obj.password,request.form['password']): #check for bad password
        flash("Invalid password.","login")
        return redirect ("/login")
    else: #success
        session.clear()
        session['user_id']=user_obj.id
        session['user_name'] = user_obj.first_name
        return redirect('/ride/dashboard')