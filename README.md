[![GitHub tag](https://img.shields.io/github/tag/krishank-gupta/ib_com_sci.svg?label=version)](https://github.com/krishank-gupta/ib_com_sci/releases)
![License](https://img.shields.io/github/license/krishank-gupta/ib_com_sci)

# Computer Science IA

# Criteria A

## Problem Definition

My client has a small store in the middle of a huge and busy wholesale market where buyers are always in a rush and there is no space to have a peaceful chat. The client finds themselves in a predicament where connections with clients seem to slip through their fingers just because they don't have time to forge an online connection <sup>2</sup>. This also results in a massive decrease in brand visibility<sup>2,3</sup>.
Additionally, the client finds that the wide range of buyers use different social media platforms so it takes time to find a mutual social media. There are cases where there are no mutual social medias. <sup>1,4</sup> The client does not know how many people are interested in their business<sup>5</sup>. They struggle to find the platform that resonates most with their target customers and therefore are unable to improve their presence on the specific platform<sup>6</sup>. This has resulted in a resource drain in an attempt to maintain multiple platforms and thus severely affected the brand visibility. My client has tried to use QR codes for specific platforms like Instagram, however, some customers do not use this platform. The client has also tried using Link Tree but sharing link tree profiles has been a hassle. Other shopkeepers seem to be having the same issue.

* See appendix 1 for initial meeting
* See appendix 2 for requested changes after proposed solution

## Proposed Solution and Justification

My proposed solution is to create a website where my client can create a customized page with links to all of their social media profiles. The client will then be able to create QR codes for their page directly from the website. Additionally, the client will be able to track visits to their page and clicks on specific social media profiles. My suggestion is to use Flask with Jinja and Flask-SQL_alchemy to create this website.

I think Flask is a great choice as it is a lightweight and flexible Python web framework that is well-suited for developing simple web applications. Flask makes it easy to create applications tailored to specific needs and requirements, without the added overhead and complexity of larger frameworks like React. In contrast to WordPress, Flask offers more control and customization options for web development, including custom database models, flexible routing, and dynamic templating with Jinja. Overall, Flask's simplicity, flexibility, and customization options make it a great choice for creating a small crowdfunding website.

I propose to use Flask instead of other common tools like React or WordPress. I propose to use Flask-SQL_Alchemy for Data Management as it is the Flask implementation of SQL_alchemy and makes it very easy to create tables, add data to the tables, and get information from the tables. According to the documentation, flask-SQL_Alchemy "simplifies using SQLAlchemy with Flask by setting up common objects and patterns for using those objects, such as a session tied to each web request, models, and engines."

## Success Criteria

1. (There are cases where there are no mutual social medias) <strong>Messaging</strong>: the application allows buyers to send messages to the clients in case there are no mutual social media platforms.

2. (The client finds themselves in a predicament where connections with clients seem to slip through their fingers just because they don't have time to forge an online connection) and (This also results in a massive decrease in brand visibility) <strong>QR Code Generation and Customization</strong>: the application generates color-customizable QR codes for the client's pages.

3. (This also results in a massive decrease in brand visibility) <strong>Customization Options</strong>: the application allows clients to edit colors in their page to fit their brand identities. Customizable options include background color, text color, and background and hover colors of social media buttons.

4. (There are cases where there are no mutual social medias) <strong>Posts feature</strong>: the application allows clients to make posts that showcase updates about their business like recent products, sales, etc.

5. (The client does not know how many people are interested in their business) <strong>Audience Tracking</strong>: the application tracks the number of visits to a particular client's page.

6. (They struggle to find the platform that resonates most with their target customers and therefore are unable to improve their presence on the specific platform) <strong> Analytics </strong>: the application can analyze the most popular social media platform for a specific client.  

*see appendix 3 for client feedback on success criteria

# Criteria B

## System Diagram
![system-diagram](/static/readme_images/system-diagram.png)
Fig 1: System Diagram

## ER Diagram
![er-diagram](/static/readme_images/er-diagram.png)
Fig 2: Entity Relationship Diagram

Visualization of the above ER Diagram:
![visualization](/static/readme_images/visualization-data.png)
Fig 3: Visualization of users data

![visualization](/static/readme_images/posts-data-visualization.png)
Fig 4: Visualization of posts data

![visualization](/static/readme_images/profile-data-visualization.png)
Fig 5: Visualization of profile data

## Wireframe Diagram
![wireframe-diagram](/static/readme_images/wireframe.png)
Fig 6: WireFrame diagram

## Test Plan

| **Test Case** 	| **Purpose** 	| **Steps/Input** 	| **Expected Result** 	|
|:---:	|:---:	|:---:	|:---:	|
| Initial Database Creation 	| Ensure that the database is created  	| None 	| 5 tables created with no pre-filled data 	|
| User Registration 	| Verify that a new user can successfully register. 	| 1. Access the "/signup" page. 2. Fill in the registration form with valid details. - Email: user@example.com - Username: newUser123 - Password: StrongPassword123 3. Submit the form. 	| User should be redirected to the login page with a success message. 	|
| Login Required 	| Verify that a not logged-in user cannot access login-only routes 	| 1. Access the "/new_post", "/inbox", and "/create-profile" endpoints. Ensure that they redirect to the login screen 	| Redirected to login screen 	|
| User Login 	| Verify that a registered user can log in. 	| 1. Access the "/login" page. 2. Enter valid login credentials. - Username: newUser123 - Password: StrongPassword123 3. Submit the form. 	| User should be redirected to the home page with a success message. 	|
| Create New Post 	| Verify that a logged-in user can create a new post. 	| 1. Log in. 2. Access the "/new_post" page. 3. Fill in the post details. - Title: New Post Title - Content: This is a test post content. - Upload a valid image file 4. Submit the form. 	| Post should be created, and user should be redirected to the post creation confirmation page. 	|
| Create User Profile 	| Verify that a logged-in user can create or update their profile. 	| 1. Log in. 2. Access the "/create_profile" page. 3. Fill in the profile details. - Background Color: #FFFFFF - Hover Color: #CCCCCC - Text Color: #000000 - Button Color: #000000 - Select one or more platforms and enter corresponding links. 4. Submit the form. 	| Profile should be created/updated 	|
| Delete Social Media Account 	| Verify that a user can delete a social media account from their profile. 	| 1. Click the remove platform button on the profile 	| The social media account should be deleted from the database 	|
| View User Profile 	| Verify that a user profile page displays correctly. 	| 1. Access a user's profile page ("/<username>"). 	| User's profile details and posts should be displayed. 	|
| Increment Clicks on Social Media Link 	| Verify that clicks on social media links are correctly incremented. 	| 1. Click on a platform link on the user's page 	| Click count for the social media link should be incremented, and the updated count should be displayed in the edit profile page 	|
| Generate QR Code 	| Verify that a QR code is generated for a user's profile. 	| 1. Access the "/static/qrcodes/<username>" endpoint. 	| The QR code image for the user's profile should be displayed. 	|
| Send and Receive Messages 	| Verify that users can send and receive messages through the chat system. 	| 1. Log in as two different users. 2. Access the "/inbox" page. 3. Send a message from one user to another. 	| The message should be sent and received, and the chat history should be updated. 	|
| Realtime Messaging 	| Ensure that the messages are in real time and no reloads are required 	| 1. Log in as two different users. 2. Access the "/inbox" page. 3. Send a message from one user to another. 	| The message should be updated in real time on both screens 	|
| Logout 	| Verify that a logged-in user can successfully log out. 	| 1. Access the "/logout" page. 	| User should be logged out and redirected to the login page. 	|

## Record of Tasks

| Task No | Planned Action                                                               | Planned Outcome                                                                                                        | Time estimate | Target completion date | Criterion |
|:-------:|------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------|:-------------:|------------------------|:---------:|
|    1    | Start collecting context for the problem                                     | Summarise what problem the client is facing                                                                            |    30 mins    | 2023/07/15             |     A     |
|    2    | Propose a solution                                                           | Discuss what can solve the problem with the client                                                                     |      1 hr     | 2023/07/17             |     A     |
|    3    | Write success criteria                                                       | Have an idea of the features needed and when the planned outcome can be called successful                              |    30 mins    | 2023/07/17             |     A     |
|    4    | Finalize success criteria with the client                                    | Get clients approval to start developing the software                                                                  |    30 mins    | 2023/07/17             |     A     |
|    5    | Draw System Diagram                                                          | Identify the resources needed for the software development                                                             |    20 mins    | 2023/07/20             |     B     |
|    6    | Draw Wireframe Diagram                                                       | Have a clear idea of how the website would look like                                                                   |    30 mins    | 2023/07/20             |     B     |
|    7    | Design UML Diagram                                                           | Have an understanding of all classes in the system and their attributes and methods                                    |    20 mins    | 2023/07/20             |     B     |
|    8    | Present Wireframe diagram to client                                          | Have the client comment on how the software would work                                                                 |    20 mins    | 2023/07/20             |     A     |
|    9    | Designing the flowchart for the login system                                 | Have a clear undertsanding about how the login system will work                                                        |    30 mins    | 2023/08/01             |     B     |
|    10   | Create Database                                                              | Setup a database to store users, their profiles, and their messages                                                    |    15 mins    | 2023/08/01             |     C     |
|    11   | Finalize the CSS Library to use                                              | Finalize the CSS library that I can use for styling the software                                                       |    20 mins    | 2023/08/01             |     B     |
|    12   | Design the front-end of the login system                                     | Have a functioning login page                                                                                          |    20 mins    | 2023/08/05             |     C     |
|    13   | Connect login system with database                                           | The login system should use the database so that users can have their accounts saved                                   |    10 mins    | 2023/08/05             |     C     |
|    14   | Implement secure password hashing for passwords                              | The system should be able to securely hash the passwords so that it is end to end encrypted                            |    10 mins    | 2023/08/05             |     C     |
|    15   | Test the user login system with dummy data                                   | Ensure that the users can create their accounts and login                                                              |    15 mins    | 2023/08/05             |           |
|    16   | Write the base html template file                                            | Have a HTML template that all pages will use                                                                           |    10 mins    | 2023/08/05             |     C     |
|    17   | Draw flowchart for the system that enables users to create their own page    | Have a clear understanding of the system that lets users create their own profile and add their social media profiles  |    15 mins    | 2023/08/08             |     B     |
|    18   | Code the routes of the system that enables users to create their own profile | Have the routes of the system that lets users create their own profile and add their social media profiles setup       |    15 mins    | 2023/08/18             |     B     |
|    19   | Design front-end of the page that enables users to create their profile      | Have users be able to design their profiles                                                                            |    10 mins    | 2023/08/18             |     C     |
|    20   | Connect front end and back end using jinja                                   | Have users be able to view and edit their profile                                                                      |    10 mins    | 2023/08/18             |     C     |
|    21   | Connect profile feature to the database                                      | Have the profile data be strored in the database                                                                       |    10 mins    | 2023/08/18             |     C     |
|    22   | Add dummy post data for testing                                              | Ensure that the profiling system allows users to create and edit their profiles and ensure it is saved in the database |    15 mins    | 2023/08/22             |     C     |
|    23   | Code the update profile feature                                              | Have users be able to change items in their profile                                                                    |    20 mins    | 2023/08/22             |     C     |
|    24   | Design the landing page                                                      | Have a home page for landing users and logo redirects                                                                  |    10 mins    | 2023/08/23             |     C     |
|    25   | Research QR code libraries                                                   | Have a library that can produce customizable QR codes                                                                  |    10 mins    | 2023/08/23             |     B     |
|    26   | Code QR code functionality                                                   | Have a system that generates a QR code for a specified page                                                            |    10 mins    | 2023/08/23             |     C     |
|    27   | Add customize options to QR code                                             | Have customizable QR codes                                                                                             |    10 mins    | 2023/09/01             |     C     |
|    28   | Code routes for QR Code Access                                               | create a route from which the QR code can be accessed                                                                  |     5 mins    | 2023/09/01             |     C     |
|    29   | Test QR codes generated and whether they lead to a user's profile            | Ensure that the QR codes are being generated and that they led to the user's profile                                   |    20 mins    | 2023/09/01             |     C     |
|    30   | Test QR Code customization                                                   | Ensure that the colors of the QR code can be added and changed as per user's wishes                                    |    20 mins    | 2023/09/01             |     C     |
|    31   | Present QR Code functionality to Client as per their request                 | Get feedback on the QR code system                                                                                     |    20 mins    | 2023/09/16             |     A     |
|    32   | Create routes for adding posts                                               | Have a post route where posts can be made                                                                              |     5 mins    | 2023/09/18             |     C     |
|    33   | Create flowchart for the system handling images                              | Have an idea of how the image processing system will work                                                              |     5 mins    | 2023/09/18             |     B     |
|    34   | Design the system for handling images from the form                          | Have the backend system that processes the images uploaded in the posts                                                |    15 mins    | 2023/09/25             |     C     |
|    35   | Write code to save post data into the database                               | Uploaded posts must be saved in the database                                                                           |    10 mins    | 2023/09/25             |     C     |
|    36   | Find a way to store the image in the database                                | Have a way to store images in the database (path/title)                                                                |    10 mins    | 2023/09/25             |     C     |
|    37   | Make the front end of the create posts page                                  | Have the form where posts can be created                                                                               |    10 mins    |             2023/09/28 |     C     |
|    38   | Connect post system front end and back end using Jinja                       | Have a working post adding and viewing system                                                                          |    30 mins    |             2023/09/28 |     C     |
|    39   | Test whether the post data is saved in the database with dummy data          | Ensure that the posts created by the users are saved in the database                                                   |    20 mins    |             2023/09/28 |     C     |
|    40   | Create navigation system                                                     | Have a system where users can navigate through the different pages                                                     |    10 mins    |             2023/09/28 |     C     |
|    41   | Seperate navigation system between logged in users and non-logged in users   | Have a seperate navigation system for users who are not logged in                                                      |    10 mins    |             2023/10/05 |     C     |
|    42   | Design the system where the posts can be seen                                | Have a system that enables the posts with images be seen to the users                                                  |    20 mins    |             2023/10/05 |     C     |
|    43   | Create a 404 page                                                            | Have a 404 page that is presented in case a client visits a broken internal link                                       |    15 mins    |             2023/10/05 |     C     |
|    44   | Test 404 page                                                                | Ensure that the 404 page is displayed when a user attempts an invalid page                                             |    10 mins    |             2023/10/12 |     C     |
|    45   | Create the front end for the messaging page                                  | Have a page where users can send messages                                                                              |    15 mins    |             2023/10/12 |     C     |
|    46   | Create routes for messaging                                                  | Have routes for chat feature                                                                                           |    15 mins    |             2023/10/12 |     C     |
|    47   | Connect messaging page and backend using web sockets                         | Have a real-time chat system using web sockets                                                                         |     2 hrs     |             2023/10/15 |     C     |
|    48   | Write the code to save messages in the database                              | Have the system save the messages in the server                                                                        |    20 mins    |             2023/10/15 |     C     |
|    49   | Make socket connections private by implementing rooms                        | Have the chat system be private among users so that a third user can not view messages between first and second user   |     2 hrs     |             2023/10/16 |     C     |
|    50   | Ensure that the messages are private using dummy data                        | Ensure that messages are private and cannot be accessed by other users                                                 |    20 mins    |             2023/10/17 |     C     |
|    51   | Make a test plan                                                             | Have a draft of the testing plan                                                                                       |      1 hr     |             2023/10/17 |     B     |
|    52   | Finalize the test plan                                                       | Finish and finalize test plan                                                                                          |    30 mins    |             2023/10/26 |     B     |
|    53   | Code Comments                                                                | Ensure that the code is commented for extensibility                                                                    |    45 mins    |             2023/10/26 |     C     |
|    54   | Check success criteria                                                       | Ensure application succeeds all success criterias                                                                      |    30 mins    |             2023/10/26 |     E     |
|    55   | Alpha testing                                                                | Ensure that the test plan passed by using 2 alpha testers                                                              |    30 mins    |             2023/11/12 |     E     |
|    56   | Future improvements                                                          | Write ways in which the application can be improved                                                                    |    30 mins    |             2023/11/12 |     E     |
|    57   | Create a video demonstration                                                 | Have a video showcasing the application                                                                                |    45 mins    |             2023/11/16 |     D     |
|    58   | Update Record of Tasks                                                       | Ensure that the record of tasks records every task                                                                     |    45 mins    |             2023/11/16 |     B     |
|    59   | Complete citations                                                           | Cite all resources used                                                                                                |    45 mins    |             2023/11/16 |     -     |
|    60   | Implementation                                                               | Deliver application to client and receive feedback                                                                     |      1 hr     |             2023/11/28 |     E     |

# Criteria C

## Existing Technologies Used

| Library/Modules  |
|:----------------:|
| os               |
| flask            |
| flask-login      |
| flask_socketio   |
| flask-sqlalchemy |
| datetime         |
| io               |
| werkzeug.utils   |
| qrcode           |
| urllib.parse     |
| sqlalchemy       |
| passlib.context  |

## List of Techniques Used

### 1. Web Sockets and Document Object Model Manipulation (Chat Feature: Success Criteria #1)

For a live chat, having to refresh the browser is a huge inconvinience specially since a user doesn't know when a message is arriving and when they should refresh. To solve this, I used web sockets so that messages update in real time without the need for refreshing the browser.

Using web sockets, a server-client connection is made where they can communicate using events. When a client connects, they join a virtual 'room'. When the HTML form for new message is submitted, the function below runs. The function checks to see if all data values are present, and stores them as constants. The code then uses Document Object Model Manipulation to display data in the front end. Then, it emits the 'send_message' event to the server with the recipient and message data attached. 

```.js
    window.sendMessage = function() {
        const userSelect = document.getElementById('userSelect');
        const messageInput = document.getElementById('messageInput');
        const recipient = userSelect.value;
        const message = messageInput.value;
        
        const messagesContainer = document.getElementById('messages');

        const card = document.createElement('div');
        card.className = 'card'
        const cardTitle = document.createElement('h3');
        cardTitle.className = `card-title right`;
        cardTitle.innerText = `${current_user} on ${(formatDateTime())}`;

        const cardContent = document.createElement('p');
        cardContent.className = `card-content right`;
        cardContent.innerText = message;

        card.appendChild(cardTitle);
        card.appendChild(cardContent);

        messagesContainer.appendChild(card);

        if (recipient && message) {
            socket.emit('send_message', { recipient, message });
            messageInput.value = '';
        }
    };
```

The server is actively listening for events. The code above triggers the code below. The server then gets the data attached and saves it in variables. Then, the User object of the sender and receipient is searched for using methods provided by the class (This is abstraction as we don't need to know how it does the search). These objects are used to create an instance of the message class and it is saved in the database. Then a 'message' event is emitted to the recipient's room so that the they gets the message in real time. 

```.py
@socketio.on('send_message')
def send_message(data):
	recipient_username = data['recipient']
	message_content = data['message']
	sender_username = current_user.username

	sender = Users.get_user(sender_username)
	recipient = Users.get_user(recipient_username)

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
```

Several events like the above are used to communicate between a client and the server to ensure real time chat feature.

### 2. Dynamic HTML Templates (Customizable Options: Success Criteria #3)

I used Jinja to create dynamic HTML templates to display content on the website. Jinja checks to see if there is a data variable being recieved from the server. If there is, jinja loops through every element in the data variable and presents the data in a card. Initially, I was using indexes to show the data like `<h2 class="post-card">{{ message[0] }}</h3>`. However, this caused several errors when I changed the position of the data in the server or added a new data field.

```.py
    <h1>Posts:</h1>
    {% for post in posts %}
        <div class="post-card">
            <img src="{{ url_for('static', filename='post_images/' + post.image_name) }}" alt="Post Image">
            <h1>{{ post.title }}</h1>
            <p>Posted on: {{ post.timestamp }}</p>

            <h4>{{ post.content }}</h4>
        </div>
    {% endfor %}
```

### 4. File Management System (Posting System: Success Criteria #4)

The Posts let clients showcase pictures. The code below uses functions and nested conditions to look for a file in the new post form and then checks to see if the file is allowed and safe to store. Then it creates an instance of the Posts class with the file name and saves in the database.

```.py
    if 'file' in request.files:
        file = request.files['file']

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        else:
            return redirect(request.url)

    user = Users.get_user(username)
    p = Posts(title=title, author=user, content=content,image_name=filename)
    db.session.add(p)
    db.session.commit()
```

### 5. Object Oriented Programming (Tracking Systems: Success Criteria #5, #6)

The tracking system implements OOP for abstraction and encapsulation. OOP provides a structured, modular, and reusable approach, making it easier to manage and extend the codebase. It enhances code organization, readability, and maintainability. 

```.py
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
```


### 6. Routing System (QR Code Customization: Success Criteria #2)

URL Endpoints are created using Flask to organize different locations where different pages are handled. Dynamic endpoints are created to serve files that contain variables in their endpoints like below: The code then checks to see if the username is a valid user using abstraction again and then parses through their profile to fetch their custom colors and edits the qr code generated.

```.py
@app.route('/static/qrcodes/<string:username>')

@app.route("/inbox", methods=['GET','POST'])
```

A problem that arose was that non-logged in user could access messaging routes. This caused a ethical problem as non-logged in users could pretend to be someone else and send messages as someone else. To solve this, I implemented a protected routes sytem that is described below:

```.py
def login_required(f):
    def wrapper(*args, **kwargs):
        if not current_user.is_authenticated:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    wrapper.__name__ = f.__name__
    return wrapper  
```

The code above sets up a custom decorator `@login_required` and takes a nested function wrapper that checks if there is a user authenticated using flask-login. If there is not a user authenticated, the code redirects the user to the login page using the url_for function imported from Flask. The function builds a redirect link by looking at functions present in each route in the flask app. If there is a user who is authenticated, the original function is called so the logged in user can view the page.

## List of Coding/design Principles Used

The Paradigms below are used to make the code extensible in the future by other developers.  

#### TRUE

The code in the application adheres to the TRUE design principles. 
1. Transparent: All *consequences* of changing a certain part of the code are obvious.
2. Reasonable: The *cost* of changing code is proportional to the benefits of the change.
3. Usable: Existing code is reusable in new and *unexpected* contexts
4. Exemplary: Code encourages change

#### SOLID: 

All classes in the application: 
1. Have a Single responsibility
2. Are Open for extension but closed for modification
3. Have Objects of a superclass that are replaceable with objects of a subclass without affecting the correctness of the program. Subtypes are substitutable for their base types.
4. Do not force clients to depend on Interfaces they are unfamiliar with
5. Have dependency inversion meaning no lower level module depends on higher level. They both depend on abstractions.

# Criteria D

[![Watch the video](https://i9.ytimg.com/vi_webp/oQabM2wWjY8/mq2.webp?sqp=CJjyjK0G-oaymwEmCMACELQB8quKqQMa8AEB-AH-BIAC6AKKAgwIABABGEggZShMMA8=&rs=AOn4CLC95HzDqFHSlF4wNlgQUidLpjP9wQ)](https://youtu.be/oQabM2wWjY8)

# Criteria E

## Client Evaluation
My client is very satisfied with the product (please refer to Appendix 4) as it achieves all the success criteria. 


## Peer Evaluation
My peer suggested changing the colors and modifying the layout but is very satisfied with the functionality (please refer to Appendix 5)

## Extensibility

The client was very satisfied with the final result. After discussions, we concluded that the following extensions could be added in the future:

1. Automated Message Responses: allow the users to set up a custom message that is sent to all users attempting to contact the user. Further, this system can also be reused as a vacation responder.
2. Advanced Customization Features: allow the users to customize their profile page more: add images/logos, customize fonts, add custom icons 

# Citations

1. “Flask raises TemplateNotFound error even though template file exists.” Stack Overflow, 27 April 2014, https://stackoverflow.com/questions/23327293/flask-raises-templatenotfound-error-even-though-template-file-exists. Accessed 14 October 2023.

2. Hamano, Junio C., and Oswald Buddenhagen. “How do I "un-revert" a reverted Git commit?” Stack Overflow, 4 January 2012, https://stackoverflow.com/questions/8728093/how-do-i-un-revert-a-reverted-git-commit. Accessed 4 January 2024.

3. “How to undo json.stringify() from javascript in a python script?” Stack Overflow, 10 December 2019, https://stackoverflow.com/questions/59273393/how-to-undo-json-stringify-from-javascript-in-a-python-script. Accessed 23 November 2023.

4. “Socket.io event listening on a specific room.” Stack Overflow, 8 August 2014, https://stackoverflow.com/questions/25195195/socket-io-event-listening-on-a-specific-room. Accessed 14 October 2023.

# Appendix

1. Initial Meeting (15/08/2023 @ 13:23)

Purpose: To find out the problem definition
Outcome: Found out that the client needs a software to solve their problem of not being able to connect to their possible clients.

2. Proposed Solution Meeting (2/09/2023 @ 18:32)

Purpose: To present proposed solution and get client's thoughts.
Outcome: Changed product from mobile app to web app as per client's preferences

3. Success Criteria Feedback

Purpose: To present success criteria
Outcome: Approved Success Criteria

![Success_Criteria](/static/readme_images/success-crieria-email.png)
Fig 7: Success Criteria Email Feedback

4. Client Eval

Purpose: To present final product
Outcome: Client liked final product

![Final_Client](/static/readme_images/final-feedback.png)
Fig 8: Final Product Email Feedback

5. Peer Eval

Purpose: To get feedback on final product
Outcome: Change colors and layout

![Peer_eval](/static/readme_images/peer-eval.png)
Fig 9: Final Product Peer Feedback