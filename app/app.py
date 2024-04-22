from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

meal_list = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_meal', methods=['GET', 'POST'])
def create_meal():
    if request.method == 'POST':
        from diet_app import predefined_food_items, add_a_meal, Meal, meal_name
        ingredients = []
        add_a_meal(ingredients)
        meal = meal_name()
        meal_list.append(Meal(meal, ingredients))
        return redirect(url_for('meal_summary'))

    return render_template('create_meal.html', predefined_food_items=predefined_food_items)

@app.route('/meal_summary')
def meal_summary():
    from diet_app import calculate_calories, calculate_protein, calculate_carbohydrates, calculate_fats, get_user_info
    total_calories = calculate_calories()
    total_protein = calculate_protein()
    total_carbohydrates = calculate_carbohydrates()
    total_fats = calculate_fats()

    get_user_info(total_calories)

    total_macros = total_protein + total_carbohydrates + total_fats

    protein_percentage = (total_protein / total_macros) * 100
    carbohydrates_percentage = (total_carbohydrates / total_macros) * 100
    fats_percentage = (total_fats / total_macros) * 100

    return render_template('meal_summary.html',
                            meal_list=meal_list,
                            total_calories=total_calories,
                            total_protein=total_protein,
                            total_carbohydrates=total_carbohydrates,
                            total_fats=total_fats,
                            protein_percentage=protein_percentage,
                            carbohydrates_percentage=carbohydrates_percentage,
                            fats_percentage=fats_percentage)

if __name__ == '__main__':
    app.run(debug=True)
