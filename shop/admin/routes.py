from flask import render_template , session, request , redirect , url_for , flash
from .forms import RegistrationForm , LoginForm
from .models import User
from shop import app , db , bcrypt
@app.route('/')
def home():
    return "HOME PAGE OF YOUR SHOP"



@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password =  bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data,username= form.username.data,email= form.email.data,
                password=hash_password)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering')
        return redirect(url_for('home'))
    return render_template('admin/register.html', form=form , title="Registration Page")



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method =="POST" and form.validate():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email']= form.email.data
            flash(f'Welcome (form.email.data) you are logged in now', 'success')
            return redirect(url_for('home'))
        else:
            flash('Wrong Password , Try again', 'danger')

    return render_template('admin/login.html' , form=form , title = "Login Page")
