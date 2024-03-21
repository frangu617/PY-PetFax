from flask import (Blueprint, render_template, request, redirect, url_for, jsonify)
from . import models
import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('fact', __name__, url_prefix='/facts')

@bp.route('/', methods=['GET'])
def index():
    facts = models.Fact.query.all()
    return render_template('facts/index.html', facts=facts)

@bp.route('/new', methods = ['GET','POST'])
def new():
    if request.method == 'POST':
     # Process the form submission
        name = request.form.get('name')  # Assuming 'submitter' is a field in your form
        fact = request.form.get('fact')  # Assuming 'fact' is a field in your form

        # Create a new instance of the Fact model
        new_fact = models.Fact(name=name, fact=fact)

        # Add the new_fact to the Flask-SQLAlchemy database session
        models.db.session.add(new_fact)

        # Commit the database session to save the changes
        models.db.session.commit()

        return redirect('/facts')
        
    return render_template('facts/new.html')

@bp.route('/<int:fact_id>', methods=['DELETE'])
def delete(fact_id):
    fact = models.Fact.query.get_or_404(fact_id)
    models.db.session.delete(fact)
    models.db.session.commit()
    return jsonify({'success': True}), 200