from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for recipes (list of dictionaries)
recipes = []

@app.route('/')
def index():
    return render_template('index.html', recipes=recipes)

@app.route('/add', methods=['GET', 'POST'])
def add_recipe():
    if request.method == 'POST':
        # Get form data
        name = request.form['name']
        ingredients = request.form['ingredients']
        instructions = request.form['instructions']
        
        # Create a new recipe dictionary and add it to the list
        new_recipe = {
            'id': len(recipes) + 1,
            'name': name,
            'ingredients': ingredients,
            'instructions': instructions
        }
        recipes.append(new_recipe)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<int:recipe_id>')
def delete_recipe(recipe_id):
    global recipes
    # Filter out the recipe to delete
    recipes = [recipe for recipe in recipes if recipe['id'] != recipe_id]
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
