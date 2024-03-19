from flask import Flask as flask
from flask_pymongo import PyMongo

mongo = PyMongo()
def create_app():
    app = flask(__name__)
    
    app.config["MONGO_URI"] = "mongodb://localhost:27017/PY-PetFax"
    
    mongo.init_app(app)
    
    @app.route('/')
    def hello():
        return 'Hello this is PetFax!'
    
    #pets index route
    # @app.route('/pets')
    # def pets():
    #     return 'These are out pets available for adoption'
    
    #register pet blueprint
    from . import facts
    app.register_blueprint(facts.bp)
    from . import pet
    app.register_blueprint(pet.bp)
    
    return app