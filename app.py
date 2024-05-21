'''
User Authentication API


Learning resources: 

FastAPI Documentation: FastAPI: https://fastapi.tiangolo.com/
OAuth2 with FastAPI: OAuth2 FastAPI: https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/
Python OAuthLib Documentation: OAuthLib: https://oauthlib.readthedocs.io/en/latest/
JWT (JSON Web Tokens): JWT.io: https://jwt.io/

'''

#import necessary libraries 
from flask import Flask, render_template
import sqlite3
import bcrypt

#Instantiate Flask
app = Flask("__main__")


#Establish database
conn = sqlite3.connect("AuthDB.db")

#create cursor object
cursor = conn.cursor()

#Creating table to store user information
cursor.execute('''CREATE TABLE IF NOT EXISTS users 
                  (id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT)''')

#commit table creation
conn.commit()

#closing DB connection
conn.close()


#create index page for API usage
@app.route("/")
def index():
    print("Replace this with return render_template when index html is created")


#create endpoint for user registration
@app.route("/user_registration")
def register_user(username, password):

#get user data (Username/Password)

#using hashing algo to salt and hash passwords with bcrypt 

#commit to database




#user login route 

#validate credentials and issue a json web token JWT






#password reset endpoit


#password reset link or reset code via email (see nutritrack for example)




#create ennd point to update password using link or code







#User profile endpoint

#fetch and update user information from the db





#OAuth integration (Allow users to log in from third party google, facebook etc.)