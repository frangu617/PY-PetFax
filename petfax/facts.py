from flask import (current_app, Blueprint, render_template, request, redirect, url_for)
import json
from petfax import mongo

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('fact', __name__, url_prefix='/facts')

@bp.get('/')
def index():
    facts = mongo.db.facts.find()
    return render_template('facts.html', facts=facts)

@bp.route('/new', methods=['POST'])
def new():
    fact_text = request.form['fact']
    mongo.db.facts.insert_one({'fact_text': fact_text})
    return render_template('facts.html')