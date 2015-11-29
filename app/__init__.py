from flask import Flask

app = Flask(__name__)
from app import views

app.config['SECRET_KEY']='jhwd12et-2[uhwd6e2e8wdhgc'