from flask import (Blueprint, render_template)
import json

pets = json.load(open('pets.json'))
print(pets)

bp = Blueprint('pet', __name__, url_prefix='/pets')

@bp.route('/' )
def index():
    return render_template('pets/listing.html', pets=pets)

# Route for showing details of a specific pet
@bp.route('/<int:pet_id>')
def show(pet_id):
    # Adjust for zero-indexed list if pet_id starts from 1
    # Ensure pet_id is within the range of the pets list
    if 1 <= pet_id <= len(pets):
        pet = pets[pet_id - 1]  # Adjusting for zero-index
        return render_template('pets/show_pet.html', pet=pet)  # Use a template for showing a single pet
    else:
        # Handle the case where pet_id is out of range
        # For example, you can return a 404 page or a custom error message
        return render_template('404.html'), 404