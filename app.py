from petfax import create_app

app = create_app()



# from flask import Flask as flask

# app = flask(__name__)

# #index route
# @app.route('/')
# def index():
#     return 'Hello this is PetFax'

# #pets index route
# @app.route('/pets')
# def pets():
#     return 'These are out pets available for adoption'