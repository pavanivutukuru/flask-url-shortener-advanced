# flask-url-shortener-advanced
Flask URL Shortener Web Application with Login System
# Flask URL Shortener Web Application (Advanced)

This project is a URL Shortener built using Flask.  
Users can sign up, log in, and shorten long URLs into short links.

## Features
- User Signup
- User Login
- URL Shortening
- URL Validation
- User-specific URL history
- Redirect to original URL

## Technologies Used
- Python
- Flask
- SQLite
- SQLAlchemy
- Flask-Login
- HTML
- CSS
- Validators Library

## Project Structure
app.py
models.py
utils.py
requirements.txt
templates/
static/

How the Application Works:

The user opens the web application.

The user signs up with a username and password.

After signup, the user logs into the system.

The dashboard page appears where the user can enter a long URL.

The application validates the URL format.

A unique short code is generated.

The short URL is displayed to the user.

The shortened URL redirects to the original website when clicked.

The user's previously shortened URLs are displayed in the dashboard


Example

Input URL:

https://www.google.com

Generated Short URL:

http://127.0.0.1:5000/3h0pC8

Clicking the short URL redirects to the original website.
