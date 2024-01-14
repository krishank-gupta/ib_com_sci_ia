import os 
from flask import Flask, render_template, request, redirect, url_for, send_file,jsonify
from flask_login import LoginManager, login_user, current_user, login_required, logout_user, UserMixin
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_sqlalchemy import SQLAlchemy
from static.library import hash_password, check_password, validation
from datetime import datetime
from io import BytesIO
from werkzeug.utils import secure_filename
import qrcode
from urllib.parse import unquote
from sqlalchemy import DateTime, func, or_

db = SQLAlchemy()

class Users(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String, unique=True, nullable=False)
	username = db.Column(db.String, unique=True, nullable=False)
	password = db.Column(db.String, unique=False, nullable=False)
	posts = db.relationship('Posts', backref='author', lazy='dynamic')
	profile = db.relationship('Profile', backref='author', uselist=False)

	def get_user(self, username):
		return Users.query.filter_by(username=username).first()

class Posts(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	title = db.Column(db.String(1000), nullable=False) # Added this line
	content = db.Column(db.String(1000), nullable=False)
	image_name = db.Column(db.String(255))  # Store the path to the uploaded image
	timestamp = db.Column(DateTime(timezone=True), default=func.now())
	
class Profile(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), unique=True)
	background_color = db.Column(db.String(1000), default="#FFFFFF") 
	text_color = db.Column(db.String(1000), default="#000000")
	hover_color = db.Column(db.String(1000), default="#cccccc")
	button_color = db.Column(db.String(1000), default="#000000")
	social_media_accounts = db.relationship('SocialMediaAccount', backref='user', lazy='dynamic')
	view_count = db.Column(db.Integer, default=0)  # New column for view count

	def increase_count(self):
		self.view_count += 1
		db.session.commit()


class SocialMediaAccount(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	profile_id = db.Column(db.Integer, db.ForeignKey('profile.id'))
	platform = db.Column(db.String, nullable=False)
	link = db.Column(db.String, nullable=False)
	clicks = db.Column(db.Integer, default=0)

class Message(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	sender_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	content = db.Column(db.String(1000), nullable=False)
	timestamp = db.Column(DateTime(timezone=True), default=func.now())

app = Flask(__name__)
adminUsername = "sys_admin"
login_manager = LoginManager(app)

socketio = SocketIO(app)

UPLOAD_FOLDER = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static', 'post_images')
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(
    app.root_path, 'database', 'database.db')
app.secret_key = os.urandom(12)
db.init_app(app)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(12)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def login_required(f):
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper  

def admin_privilege_required(f):
	def wrapper(*args, **kwargs):
		if current_user.username != 'Krishank':
			return redirect(url_for('index'))
		return f(*args, **kwargs)
	wrapper.__name__ = f.__name__
	return wrapper

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id))

@app.route("/", methods=['GET','POST'])
def index():
	return render_template("landing.html")

@app.route("/signup", methods=['GET', 'POST'])
def signup():
	message = ''
	if request.method == 'POST':
		signup_email = request.form['signup_email']
		signup_username = request.form['signup_username']
		signup_password = hash_password(request.form['signup_password'])
		# print(signup_email, signup_username, signup_password)
		u = Users(email=signup_email, username=signup_username, password=signup_password)
		db.session.add(u)
		db.session.commit()
		message = f"Registration Success. Proceed to Login."
		return render_template("signup.html", message=message)
	else:
		return render_template("signup.html", message=message)
	
@app.route("/login", methods=['GET', 'POST'])
def login():
	message = ''
	error = ''
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		users = Users.query.all()
		for user in users:
			if user.username == username and check_password(password, user.password):
				message = "success"
				login_user(user)
				return redirect(url_for('index'))
			else:
				message = "error"
				error = True
		print(message,error)
		return render_template("login.html", message=message, error=error)
	else:
		print(message,error)
		return render_template("login.html", message=message, error=error)

@app.route('/new_post', methods=['GET', 'POST'])
@login_required
def new_post():
	if request.method == 'POST':
		username = current_user.username
		title = request.form['title']
		content = request.form['content']
		
		if 'file' in request.files:
			file = request.files['file']

			if file and allowed_file(file.filename):
				filename = secure_filename(file.filename)
				file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			else:
				return redirect(request.url)

		user = Users.query.filter_by(username=username).first()
		p = Posts(title=title, author=user, content=content,image_name=filename)
		db.session.add(p)
		db.session.commit()
		return render_template('add_post.html')
	else:
		return render_template('add_post.html')

@app.route('/create_profile', methods=['GET', 'POST'])
@login_required
def create_profile():
	if request.method == 'POST':
		username = current_user.username
		bg_col = request.form['background_color']
		hover_color = request.form['hover_color']
		text_color = request.form['text_color']
		button_color = request.form['button_color']
		platforms = request.form.getlist('platform[]')
		links = request.form.getlist('link[]')

		print(username, bg_col, hover_color,text_color,button_color)
		print("Platforms:", platforms)
		print("Links:", links)

		user = Users.query.filter_by(username=username).first()

		existing_profile = Profile.query.filter_by(user_id=user.id).first()
		prof = None

		if existing_profile:
			existing_profile.background_color = bg_col
			existing_profile.hover_color = hover_color
			existing_profile.text_color = text_color
			existing_profile.button_color = button_color
			print('updated')
		else:
			prof = Profile(background_color=bg_col, author=user, text_color=text_color, button_color=button_color, hover_color=hover_color)
			db.session.add(prof)
		
		db.session.commit()
		profile_id = prof.id if prof else existing_profile.id

        # Assuming that the number of platforms and links are the same
		for platform, link in zip(platforms, links):
			social_media = SocialMediaAccount(profile_id=profile_id, platform=platform, link=link)
			db.session.add(social_media)
			db.session.commit()

		return render_template('create_profile.html', user=user, existing_profile=existing_profile)
	else:
		username = current_user.username
		user = Users.query.filter_by(username=username).first()

		# Retrieve the user's profile data
		existing_profile = Profile.query.filter_by(user_id=user.id).first()

		return render_template('create_profile.html', user=user, existing_profile=existing_profile)

@app.route('/delete_social_media', methods=['DELETE'])
def delete_social_media():
	# Implement your logic to delete the social media account here
	# For example:
	data = request.get_json()
	social_media_link = data.get('link')
	social_media = SocialMediaAccount.query.filter_by(link=social_media_link).first()
	if social_media:
		db.session.delete(social_media)
		db.session.commit()
		result = f"Social media account with link {social_media_link} deleted successfully!"
	else:
		result = f"Social media account with link {social_media_link} not found!"

	print(result)
	return result


@app.route('/<string:user_username>')
def show_user(user_username):
	user = Users.query.filter_by(username=user_username).first()
	if user:
		profile = Profile.query.filter_by(user_id=user.id).first()
		profile.increase_count()

		db.session.commit()
		posts = user.posts.all()

		return render_template('user_profile.html', username=user.username, posts=posts, profile=profile)
	else:
		return render_template('404.html'), 404
		
@app.route('/click', methods=['POST'])
def increment_clicks():
	data = request.get_json()
	link = data.get('link')

	if link:

		decoded_link = unquote(link)
		print(decoded_link)

		social_media = SocialMediaAccount.query.filter_by(link=decoded_link).first()
		print(social_media)
		if social_media:
			# Increment the clicks count
			social_media.clicks += 1
			print(social_media.clicks)
			db.session.commit()

			return jsonify(clicks=social_media.clicks, social_media_id=social_media.id)
		else:
			return jsonify(error='Social media account not found'), 404
	else:
		return jsonify(error='Link not provided in the request body'), 400

@app.route('/static/qrcodes/<string:username>')
def serve_qr_code(username):
	user = Users.query.filter_by(username=username).first()
	if user:
		profile = Profile.query.filter_by(user_id=user.id).first()

		qr = qrcode.QRCode(
			version=1,
			error_correction=qrcode.constants.ERROR_CORRECT_L,
			box_size=20,
			border=4,
		)
		qr.add_data(f"http://127.0.0.1:5000/{username}")  # Replace with your actual domain
		qr.make(fit=True)

		# Create BytesIO object to store the image in memory
		img_stream = BytesIO()
		img = qr.make_image(fill_color=profile.background_color,back_color=profile.text_color)
		img.save(img_stream)
		img_stream.seek(0)

		# Return the image directly without saving to the server
		return send_file(img_stream, mimetype='image/png')
	else:
		return render_template('404.html'), 404

@app.route("/inbox", methods=['GET','POST'])
@login_required
def inbox():
	users = Users.query.all()
	c = Users.query.filter_by(username=current_user.username).first()

	messages = Message.query.filter(or_(Message.sender_id == c.id, Message.receiver_id == c.id)).all()
	data = []

	for message in messages:
		sender = Users.query.filter_by(id=message.sender_id).first()
		data.append((message, sender.username))


	# for i in messages:
	# 	message = Message.query.filter_by(id=i.id).first()
	# 	sender = message.sender_id
	# 	S = Users.query.filter_by(id=sender).first()
	# 	print(message,S.username)
	# 	data.append((message,S.username))
	return render_template("inbox.html", data=data[::-1],current_user=c)

@socketio.on('get_users')
def get_users():
	u = Users.query.all()
	users = []
	for user in u:
		users.append(user.username)
	emit('user_list', users)

@socketio.on('connect')
def handle_connect():
    if current_user.username:
        join_room(current_user.username)

@socketio.on('disconnect')
def handle_disconnect():
    if current_user.username:
        leave_room(current_user.username)

@socketio.on('join_room')
def join():
    join_room(current_user.username)

@socketio.on('send_message')
def send_message(data):
	recipient_username = data['recipient']
	message_content = data['message']
	sender_username = current_user.username

	sender = Users.query.filter_by(username=sender_username).first()
	recipient = Users.query.filter_by(username=recipient_username).first()

	new_message = Message(
		sender_id=sender.id, 
		receiver_id=recipient.id, 
		content=message_content, 
		timestamp=datetime.now()
	)

	db.session.add(new_message)
	db.session.commit()
	
	emit(
		'message', {
			'sender': sender_username,  
			'message': message_content,
			'timestamp': datetime.now().strftime('%b %d, %Y %I:%M %p')
		},
		to=recipient.username
	)


@app.route('/logout')
def logout():
	logout_user()		
	return redirect(url_for('login'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/admin')
def admin():
	users = Users.query.all()
	posts = Posts.query.all()
	return render_template('admin.html', users=users, posts=posts)

with app.app_context():
	db.create_all()