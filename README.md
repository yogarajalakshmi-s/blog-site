This is a blog site running on Flask

**Tech Stack**   
Python, Flask, Jinja, SQLite, SQLAlchemy, Html, CSS, Bootstrap

**About this project:**  
Developed this blog site from scratch.
The functionalities of the site include, Registering new user, Login, Home page displaying all blogs, Contact, About, Logout.
Maintaining three tables - users, blog_posts, comments.

**Functionalities:**
**Register** - Stored the users in the DB using SQLAlchemy. Secured the password using PBKDF2 hashing.
Validations are performed. If the mail ID already exists, shows the flask flash message.  
**Login** - Logging in users by comparing the data from DB. If the mail ID is incorrect, redirects the users to register page. If the password is incorrect, show a flash message that it's incorrect.  
**Home** - After successful login, the home page shows all the blog posts. Only the admin user (first signup) will be able to create, edit, delete a post. These buttons will not be shown for other users.
If a user clicks on a post, they can view the detailed post and comment on it.
The routes are all protected, i.e., if a user tries to access the edit or delete post by directly hitting the route, they will be shown 'Unauthorized message'.
If a user tries to view a post without logging in, they will be shown 'Unauthorized'.  
**About** - Basic template showing About page  
**Contact** - A contact form is created to make users contact with the admin user.  
**Logout** - After logging out, the user is redirect to the login page.  

**References:**
https://flask-login.readthedocs.io/en/latest/
https://flask.palletsprojects.com/en/2.3.x/patterns/flashing/
https://flask.palletsprojects.com/en/2.3.x/patterns/templateinheritance/
https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
