from flask import (current_app, Blueprint, render_template, request, redirect, url_for)
import json
from petfax import mongo

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('fact', __name__, url_prefix='/facts')

@bp.get('/')
def index():
    facts = mongo.db.facts.find()
    return render_template('facts_index.html')

@bp.route('/new', methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        fact_text = request.form['fact']
        mongo.db.facts.insert_one({'fact_text': fact_text})
        # Redirect to prevent form resubmission on refresh
        return redirect(url_for('fact.index'))

    # For a GET request, just render the template with the form
    return render_template('facts.html')
