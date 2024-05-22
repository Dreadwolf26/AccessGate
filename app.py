'''
User Authentication API


Learning resources: 

FastAPI Documentation: FastAPI: https://fastapi.tiangolo.com/
OAuth2 with FastAPI: OAuth2 FastAPI: https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/
Python OAuthLib Documentation: OAuthLib: https://oauthlib.readthedocs.io/en/latest/
JWT (JSON Web Tokens): JWT.io: https://jwt.io/

'''

#import necessary libraries 
from flask import Flask, render_template, request,jsonify
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
@app.route("/register", method=["POST"])
def register_user(username, password):
    data = request.get_json()
    username = data.get('username')
    passord = data.get('password')
    #hashing password 
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    conn = sqlite3.connect('AuthDB.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
    except sqlite3.IntegrityError:
        return jsonify({"message": "User already exists"}), 400
    finally:
        conn.close()

    return jsonify({"message": "User registered successfully"}), 201

#user login route 
@app.route("login",method=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    conn = sqlite3.connect('AuthDB.db')
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    row = cursor.fetchone()
    conn.close()

    if row and bcrypt.check_password_hash(row[0], password):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401

#validate credentials and issue a json web token JWT






#password reset endpoit


#password reset link or reset code via email (see nutritrack for example)




#create ennd point to update password using link or code
if __name__ == '__main__':
    app.run(debug=True)






#User profile endpoint

#fetch and update user information from the db





#OAuth integration (Allow users to log in from third party google, facebook etc.)