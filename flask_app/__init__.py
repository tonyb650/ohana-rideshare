from flask import Flask
app = Flask(__name__)
app.secret_key = "The secretest of keys"