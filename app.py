from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from models import db, User, URL
from utils import generate_short_code
import validators

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/signup', methods=['GET','POST'])
def signup():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        if len(username) < 5 or len(username) > 9:
            return "Username must be between 5 and 9 characters"

        user = User.query.filter_by(username=username).first()

        if user:
            return "This username already exists"

        new_user = User(username=username, password=password)

        db.session.add(new_user)
        db.session.commit()

        return redirect('/login')

    return render_template('signup.html')


@app.route('/login', methods=['GET','POST'])
def login():

    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username, password=password).first()

        if user:
            login_user(user)
            return redirect('/dashboard')

        return "Invalid Login"

    return render_template('login.html')


@app.route('/dashboard', methods=['GET','POST'])
@login_required
def dashboard():

    if request.method == 'POST':

        original_url = request.form['url']

        if not validators.url(original_url):
            return "Invalid URL"

        short_code = generate_short_code()

        new_url = URL(
            original_url=original_url,
            short_code=short_code,
            user_id=current_user.id
        )

        db.session.add(new_url)
        db.session.commit()

    urls = URL.query.filter_by(user_id=current_user.id).all()

    return render_template('dashboard.html', urls=urls)


@app.route('/<short_code>')
def redirect_url(short_code):

    url = URL.query.filter_by(short_code=short_code).first()

    if url:
        return redirect(url.original_url)

    return "URL not found"


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')


if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)