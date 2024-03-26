import os
from dotenv import load_dotenv
from flask import Flask as flask
from flask_migrate import Migrate
def create_app():
    app = flask(__name__)
    
    load_dotenv()
    postgres_user = os.getenv('PG_USERNAME')
    posgres_password = os.getenv('PG_PASSWORD')
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{postgres_user}:{posgres_password}@localhost:5432/petfax'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    from . import models
    models.db.init_app(app)
    migrate = Migrate(app, models.db)
    @app.route('/')
    def hello():
        return 'Hello this is PetFax!'
    
    #register pet blueprint
    from . import facts
    app.register_blueprint(facts.bp)
    from . import pet
    app.register_blueprint(pet.bp)
    
    return app