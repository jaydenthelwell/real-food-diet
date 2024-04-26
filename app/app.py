import os
from flask import Flask, render_template, request, redirect, url_for
from diet_app import Meal, FoodItem, predefined_food_items, food_items_dict
app = Flask(__name__, static_url_path='/static')

app = Flask(__name__)

meal_list = []
ingredients = []

def food_list():
    return [food_item.name for food_item in predefined_food_items]

def calculate_calories():
    calorie_count = 0
    for meal in meal_list:
        # print("Meal: ", meal.name)
        # print("Ingredients: ", [ingredient.name for ingredient in meal.ingredients])
        # print("Calories: ", [ingredient.calories for ingredient in meal.ingredients])
        for ingredient in meal.ingredients:
            calorie_count += ingredient.calories
    return calorie_count

def calculate_protein():
    protein_count = 0
    for meal in meal_list:
        # print("Meal: ", meal.name)
        # print("Ingredients: ", [ingredient.name for ingredient in meal.ingredients])
        for ingredient in meal.ingredients:
            print("Protein: " + ingredient.name + ": ", ingredient.protein)
            protein_count += ingredient.protein
    return protein_count

def calculate_carbohydrates():
    carbohydrate_count = 0
    for meal in meal_list:
        # print("Meal: ", meal.name)
        # print("Ingredients: ", [ingredient.name for ingredient in meal.ingredients])
        for ingredient in meal.ingredients:
            print("Carbohydrates: " + ingredient.name + ": ", ingredient.carbohydrates)
            carbohydrate_count += ingredient.carbohydrates
    return carbohydrate_count

def calculate_fats():
    fat_count = 0
    for meal in meal_list:
        # print("Meal: ", meal.name)
        # print("Ingredients: ", [ingredient.name for ingredient in meal.ingredients])
        for ingredient in meal.ingredients:
            print("Fats: " + ingredient.name + ": ", ingredient.fats)
            fat_count += ingredient.fats
    return fat_count

def calculate_vitamin_a():
    vitamin_a_total = 0
    for meal in meal_list:
        for ingredient in meal.ingredients:
            vitamin_a_total += ingredient.vitamin_a
    return vitamin_a_total

def calculate_vitamin_c():
    vitamin_c_total = 0
    for meal in meal_list:
        for ingredient in meal.ingredients:
            vitamin_c_total += ingredient.vitamin_c
    return vitamin_c_total

def calculate_vitamin_d():
    vitamin_d_total = 0
    for meal in meal_list:
        for ingredient in meal.ingredients:
            vitamin_d_total += ingredient.vitamin_d
    return vitamin_d_total

def calculate_vitamin_e():
    vitamin_e_total = 0
    for meal in meal_list:
        for ingredient in meal.ingredients:
            vitamin_e_total += ingredient.vitamin_e
    return vitamin_e_total

def calculate_vitamin_k():
    vitamin_k_total = 0
    for meal in meal_list:
        for ingredient in meal.ingredients:
            vitamin_k_total += ingredient.vitamin_k
    return vitamin_k_total

def calculate_calcium():
    calcium_total = 0
    for meal in meal_list:
        for ingredient in meal.ingredients:
            calcium_total += ingredient.calcium
    return calcium_total

def calculate_iron():
    iron_total = 0
    for meal in meal_list:
        for ingredient in meal.ingredients:
            iron_total += ingredient.iron
    return iron_total

def calculate_magnesium():
    magnesium_total = 0
    for meal in meal_list:
        for ingredient in meal.ingredients:
            magnesium_total += ingredient.magnesium
    return magnesium_total

def calculate_phosphorus():
    phosphorus_total = 0
    for meal in meal_list:
        for ingredient in meal.ingredients:
            phosphorus_total += ingredient.phosphorus
    return phosphorus_total

def calculate_potassium():
    potassium_total = 0
    for meal in meal_list:
        for ingredient in meal.ingredients:
            potassium_total += ingredient.potassium
    return potassium_total

def calculate_sodium():
    sodium_total = 0
    for meal in meal_list:
        for ingredient in meal.ingredients:
            sodium_total += ingredient.sodium
    return sodium_total

def calculate_zinc():
    zinc_total = 0
    for meal in meal_list:
        for ingredient in meal.ingredients:
            zinc_total += ingredient.zinc
    return zinc_total

def recommended_calories(gender, age, activity_level, total_calories):
    age = int(age)  # Convert age to an integer
    if gender == "M":
        if age in range(19, 31):
            if activity_level == "sedentary":
                calorie_range = range(600, 800)
            if activity_level == "moderately active":
                calorie_range = range(700, 900)
            if activity_level == "active":
                calorie_range = range(800, 1000)
        elif age in range(31, 51):
            if activity_level == 'sedentary':
                calorie_range = range(500, 700)
            elif activity_level == 'moderately active':
                calorie_range = range(600, 800)
            elif activity_level == 'active':
                calorie_range = range(650, 850)
        elif age >= 51:
            if activity_level == 'sedentary':
                calorie_range = range(400, 500)
            elif activity_level == 'moderately active':
                calorie_range = range(500, 600)
            elif activity_level == 'active':
                calorie_range = range(600, 700)
    elif gender == 'F':
        if age in range(19, 31):
            if activity_level == 'sedentary':
                calorie_range = range(500, 700)
            elif activity_level == 'moderately active':
                calorie_range = range(600, 800)
            elif activity_level == 'active':
                calorie_range = range(700, 900)
        elif age in range(31, 51):
            if activity_level == 'sedentary':
                calorie_range = range(450, 600)
            elif activity_level == 'moderately active':
                calorie_range = range(525, 650)
            elif activity_level == 'active':
                calorie_range = range(600, 700)
        elif age >= 51:
            if activity_level == 'sedentary':
                calorie_range = range(400, 475)
            elif activity_level == 'moderately active':
                calorie_range = range(475, 550)
            elif activity_level == 'active':
                calorie_range = range(550, 650)
    return total_calories in calorie_range, calorie_range

def calculate_calorie_score(total_calories, gender, age, activity_level):
    recommended, calorie_range = recommended_calories(gender, age, activity_level, total_calories)
    max_score = 20
    if recommended:
        return max_score
    else:
        difference = min(calorie_range) - total_calories
        if difference < 0:
            score =  max_score - (difference / 10)
        else:
            score = max_score - ((difference / 10) * -1)
        return min(max_score, score)

def calculate_macro_balance_score(protein_percentage, carbohydrates_percentage, fats_percentage):
    macro_balance_score = 0

    if protein_percentage >= 35:
        macro_balance_score += 5
    elif 25 <= protein_percentage < 35:
        macro_balance_score += 3
    elif 20 <= protein_percentage < 25:
        macro_balance_score += 2.5
    elif 15 <= protein_percentage < 20:
        macro_balance_score += 2
    elif protein_percentage < 15:
        macro_balance_score += 0

    if carbohydrates_percentage > 55:
        macro_balance_score += 2
    elif 30 <= carbohydrates_percentage <= 55:
        macro_balance_score += 5
    elif 20 <= carbohydrates_percentage < 30:
        macro_balance_score += 3
    elif 15 <= carbohydrates_percentage < 20:
        macro_balance_score += 1
    elif carbohydrates_percentage < 15:
        macro_balance_score += 0

    if fats_percentage > 35:
        macro_balance_score += 2
    elif 28 <= fats_percentage <= 35:
        macro_balance_score += 4
    elif 20 <= fats_percentage < 28:
        macro_balance_score += 5
    elif 15 <= fats_percentage < 20:
        macro_balance_score += 3
    elif fats_percentage < 15:
        macro_balance_score += 0

    return macro_balance_score

def calculate_micro_nutrient_score():
    # Recommended daily intake of vitamins and minerals in milligrams (per meal)
    recommended_intake = {
        'Vitamin A': 900 / 3,
        'Vitamin C': 90 / 3,
        'Vitamin D': 15 / 3,
        'Vitamin E': 15 / 3,
        'Vitamin K': 120 / 3,
        'Calcium': 1000 / 3,
        'Iron': 8 / 3,
        'Magnesium': 420 / 3,
        'Phosphorus': 700 / 3,
        'Potassium': 4700 / 3,
        'Sodium': 2300 / 3,
        'Zinc': 11 / 3
    }

    total_score = 0
    for meal in meal_list:
        meal_score = 0
        for ingredient in meal.ingredients:
            ingredient_name = ingredient.name
            food_item = food_items_dict.get(ingredient_name.lower())
            if food_item:
                # Add up the amount of each nutrient in the meal
                meal_score += (food_item.vitamin_a + food_item.vitamin_c +
                                food_item.vitamin_d + food_item.vitamin_e +
                                food_item.vitamin_k + food_item.calcium +
                                food_item.iron + food_item.magnesium +
                                food_item.phosphorus + food_item.potassium +
                                food_item.sodium + food_item.zinc)

        # Calculate the nutrient score for the meal
        meal_score_percentage = meal_score / sum(recommended_intake.values())
        meal_score_out_of_15 = meal_score_percentage * 15
        total_score += meal_score_out_of_15

    print("Total Nutrient Score (out of 15):", total_score)

    if total_score >= 15:
        return 15
    else:
        return round(total_score)

def generate_feedback(calorie_score, macro_balance_score, micro_nutrient_score):
    feedback_message = (
        f"Your calorie score is {calorie_score}\n/20. "
        f"Your macro balance score is {macro_balance_score}\n/15. "
        f"Your micro nutrient score is {micro_nutrient_score}/15. "
    )
    return feedback_message

@app.route('/', methods=['GET', 'POST'])
def index():
    global ingredients
    if request.method == 'POST':
        user_selection = request.form['ingredient']
        ingredient_weight = float(request.form['weight'])

        selected_ingredient = food_items_dict.get(user_selection.lower())

        if selected_ingredient:
            multiplier = ingredient_weight / selected_ingredient.weight
            calories_adjusted = selected_ingredient.calories * multiplier
            protein_adjusted = selected_ingredient.protein * multiplier
            carbs_adjusted = selected_ingredient.carbohydrates * multiplier
            fats_adjusted = selected_ingredient.fats * multiplier
            vitamin_a_adjusted = selected_ingredient.vitamin_a * multiplier
            vitamin_c_adjusted = selected_ingredient.vitamin_c * multiplier
            vitamin_d_adjusted = selected_ingredient.vitamin_d * multiplier
            vitamin_e_adjusted = selected_ingredient.vitamin_e * multiplier
            vitamin_k_adjusted = selected_ingredient.vitamin_k * multiplier
            calcium_adjusted = selected_ingredient.calcium * multiplier
            iron_adjusted = selected_ingredient.iron * multiplier
            magnesium_adjusted = selected_ingredient.magnesium * multiplier
            phosphorus_adjusted = selected_ingredient.phosphorus * multiplier
            potassium_adjusted = selected_ingredient.potassium * multiplier
            sodium_adjusted = selected_ingredient.sodium * multiplier
            zinc_adjusted = selected_ingredient.zinc * multiplier

            adjusted_ingredient = FoodItem(selected_ingredient.name, ingredient_weight,
                                        calories_adjusted, protein_adjusted,
                                        carbs_adjusted, fats_adjusted,
                                        vitamin_a_adjusted, vitamin_c_adjusted,
                                        vitamin_d_adjusted, vitamin_e_adjusted,
                                        vitamin_k_adjusted, calcium_adjusted,
                                        iron_adjusted, magnesium_adjusted,
                                        phosphorus_adjusted, potassium_adjusted,
                                        sodium_adjusted, zinc_adjusted)
            ingredients.append(adjusted_ingredient)
        else:
            print("Ingredient not found")

    return render_template('index.html', food_items=food_list(), ingredients=ingredients)

@app.route('/create_meal', methods=['POST'])
def create_meal():
    global ingredients, meal_list
    meal_name = request.form['meal_name']

    meal = Meal(meal_name, ingredients)
    meal_list.append(meal)
    ingredients = []

    total_calories = calculate_calories()
    return render_template('score.html', total_calories=total_calories)

@app.route('/remove_ingredient/<int:index>')
def remove_ingredient(index):
    global ingredients
    index -= 1
    if index >= 0 and index < len(ingredients):
        ingredients.pop(index)
    return redirect(url_for('index'))

@app.route('/view_meals')
def view_meals():
    total_calories = calculate_calories()
    total_protein = calculate_protein()
    total_carbohydrates = calculate_carbohydrates()
    total_fats = calculate_fats()
    return render_template('view_meals.html', meal_list=meal_list,
                        total_calories=total_calories, total_protein=total_protein,
                        total_carbohydrates=total_carbohydrates, total_fats=total_fats)

@app.route('/get_user_info', methods=['POST'])
def get_user_info():
    gender = request.form['gender'].strip().upper()
    age = request.form['age']
    activity_level = request.form['activity_level'].strip().lower()
    total_calories = float(request.form['total_calories'])
    recommended, calorie_range = recommended_calories(gender, age, activity_level, total_calories)

    total_protein = calculate_protein()
    total_carbohydrates = calculate_carbohydrates()
    total_fats = calculate_fats()

    total_macros = total_protein + total_carbohydrates + total_fats
    protein_percentage = round((total_protein / total_macros) * 100, 1)
    carbohydrates_percentage = round((total_carbohydrates / total_macros) * 100, 1)
    fats_percentage = round((total_fats / total_macros) * 100, 1)

    message = ""

    if recommended:
        message = "Your meal is within the recommended calorie range."
    else:
        difference = min(calorie_range) - total_calories
        if difference < 0:
            message = f"Your meal is not within the recommended calorie range. You need to remove {difference * -1} calories."
        elif difference > 0:
            message = f"Your meal is not within the recommended calorie range. You need to add {difference} calories."

    if protein_percentage < 35:
        message += f"\nProtein Percentage: {protein_percentage}%\n{35 - protein_percentage} more grams of protein to hit the target for protein intake in this meal. "
    else:
        message += f"\nProtein Percentage: {protein_percentage}%\n. This is a healthy amount of protein. "

    if carbohydrates_percentage > 45:
        message += f"\nCarb Percentage: {carbohydrates_percentage}%\nYou have gone over you carbohydrate target, consider balancing your meal out with more protein. "
    else:
        message += f"\nCarb Percentage: {carbohydrates_percentage}%\n. This is a healthy amount of carbs. "

    if fats_percentage < 20:
        message += f"\nFats Percentage: {fats_percentage}%\n{20 - fats_percentage} more grams of fats to hit the target for fat intake in this meal. Consider adding some more healthy fats. "
    else:
        message += f"\nFats Percentage: {fats_percentage}%\n. This is a healthy amount of fats. "

    return render_template('get_user_info.html', message=message)

@app.route('/score', methods=['POST'])
def score():
    gender = request.form['gender'].strip().upper()
    age = request.form['age']
    activity_level = request.form['activity_level'].strip().lower()
    total_calories = calculate_calories()
    recommended, calorie_range = recommended_calories(gender, age, activity_level, total_calories)
    # Calculate total macro-nutrients
    total_protein = calculate_protein()
    total_carbohydrates = calculate_carbohydrates()
    total_fats = calculate_fats()

    # Calculate total macros percentage
    total_macros = total_protein + total_carbohydrates + total_fats
    protein_percentage = (total_protein / total_macros) * 100
    carbohydrates_percentage = (total_carbohydrates / total_macros) * 100
    fats_percentage = (total_fats / total_macros) * 100

    message = ""

    if recommended:
        message = "Your meal is within the recommended calorie range."
    else:
        difference = min(calorie_range) - total_calories
        if difference < 0:
            message = f"Your meal is not within the recommended calorie range. You need to remove {difference * -1} calories."
        elif difference > 0:
            message = f"Your meal is not within the recommended calorie range. You need to add {difference} calories."

    if protein_percentage < 35:
        message += f"\nProtein Percentage: {protein_percentage}%\n{35 - protein_percentage} more grams of protein to hit the target for protein intake in this meal. "
    else:
        message += f"\nProtein Percentage: {protein_percentage}%\n. This is a healthy amount of protein. "

    if carbohydrates_percentage > 45:
        message += f"\nCarb Percentage: {carbohydrates_percentage}%\nYou have gone over you carbohydrate target, consider balancing your meal out with more protein. "
    else:
        message += f"\nCarb Percentage: {carbohydrates_percentage}%\n. This is a healthy amount of carbs. "

    if fats_percentage < 20:
        message += f"\nFats Percentage: {fats_percentage}%\n{20 - fats_percentage} more grams of fats to hit the target for fat intake in this meal. Consider adding some more healthy fats. "
    else:
        message += f"\nFats Percentage: {fats_percentage}%\n. This is a healthy amount of fats. "

    # Calculate calorie score
    calorie_score = calculate_calorie_score(total_calories, gender, age, activity_level)
    # Calculate macro-nutrient balance score
    macro_balance_score = calculate_macro_balance_score(
        protein_percentage, carbohydrates_percentage, fats_percentage)

    # Calculate micro-nutrient score
    micro_nutrient_score = calculate_micro_nutrient_score()

    # Calculate total score
    total_score = calorie_score + macro_balance_score + micro_nutrient_score

    # Provide feedback
    feedback = generate_feedback(calorie_score, macro_balance_score,
                                micro_nutrient_score)

    # Construct the response
    return render_template('score.html', message=message, feedback=feedback, total_score=total_score)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
