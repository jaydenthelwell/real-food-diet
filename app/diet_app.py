import sys
import difflib

class FoodItem():
    def __init__(self, name, weight, calories, protein, carbohydrates, fats, vitamin_a, vitamin_c, vitamin_d, vitamin_e, vitamin_k, calcium, iron, magnesium, phosphorus, potassium, sodium, zinc):
        self.name = name
        self.weight = weight
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fats = fats
        self.vitamin_a = vitamin_a
        self.vitamin_c = vitamin_c
        self.vitamin_d = vitamin_d
        self.vitamin_e = vitamin_e
        self.vitamin_k = vitamin_k
        self.calcium = calcium
        self.iron = iron
        self.magnesium = magnesium
        self.phosphorus = phosphorus
        self.potassium = potassium
        self.sodium = sodium
        self.zinc = zinc

class Meal():
    #initializes the meal class
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

# lists of predefined food items represented as food item objects with attributes initialized

fish_items = [
    FoodItem("Salmon", 100, 208, 23, 0, 13, 9, 0, 2.8, 0.2, 0.5, 13, 0.2, 20, 23, 3, 59, 59),
    FoodItem("Cod", 100, 82, 18, 0, 1, 0, 0, 0, 0, 0, 1, 0.1, 4, 0, 0, 38, 63),
    FoodItem("Tuna", 100, 120, 26, 0, 1, 2, 0, 0, 0.5, 0, 8, 1.3, 12, 0, 0, 45, 12),
    FoodItem("Sardines", 100, 190, 25, 0, 9, 486, 0, 0.3, 1.8, 0.1, 382, 2.9, 42, 490, 259, 397, 1.3),
    FoodItem("Trout", 100, 140, 20, 0, 7, 1789, 0, 0.5, 1.4, 0, 60, 2.2, 27, 303, 424, 74, 1.1)
]

meat_items = [
    FoodItem("Chicken Breast", 100, 165, 31, 0, 3.6, 19, 0, 0.3, 0.1, 0.5, 11, 0.7, 23, 216, 256, 70, 0.8),
    FoodItem("Turkey Breast", 100, 189, 29, 0, 8, 20, 0, 0, 0, 0.1, 12, 1.5, 25, 250, 271, 72, 1.4),
    FoodItem("Lean Beef (Grass-fed, Sirloin)", 100, 250, 26, 0, 15, 2, 0, 0.1, 0.3, 1.9, 9, 1.8, 20, 190, 260, 70, 5),
    FoodItem("Pork Tenderloin", 100, 143, 28, 0, 3, 0, 0, 0, 0.1, 0.1, 7, 0.6, 22, 250, 308, 65, 1.1),
    FoodItem("Venison", 100, 158, 30, 0, 3, 0, 0, 0, 0.1, 0.1, 5, 3.1, 27, 208, 290, 62, 2.3)
]

vegan_protein_items = [
    FoodItem("Lentils", 100, 116, 9, 20, 0.4, 3, 1, 0, 0.1, 0.8, 27, 3.3, 36, 180, 369, 2, 1.3),
    FoodItem("Chickpeas", 100, 164, 8.9, 27.4, 2.6, 7, 2.5, 0, 0.6, 1.3, 49, 4.3, 48, 168, 291, 24, 2.6),
    FoodItem("Black Beans", 100, 339, 21.6, 62.4, 0.8, 14, 1.3, 0, 0.1, 0.8, 160, 9.1, 128, 333, 611, 2, 3.3),
    FoodItem("Tofu", 100, 76, 8, 1.9, 4.8, 38, 0, 0, 0.4, 0.1, 683, 4.7, 145, 164, 121, 8, 1.8),
    FoodItem("Tempeh", 100, 193, 19, 9.4, 11.4, 4, 0, 0, 0.2, 0.3, 62, 2.7, 66, 194, 235, 29, 2.4),
    FoodItem("Edamame", 100, 122, 11.9, 9.9, 5.2, 529, 11, 0, 1.8, 41, 59, 2.1, 54, 185, 436, 12, 2.1),
    FoodItem("Quinoa", 100, 120, 4.4, 21.3, 1.9, 0, 0, 0, 0.9, 0.3, 17, 1.5, 64, 197, 319, 5, 2.8),
    FoodItem("Hemp Seeds", 100, 553, 31.6, 10.9, 49.3, 0, 0, 0, 0, 1.6, 483, 7.95, 700, 165, 1400, 20, 7.95),
    FoodItem("Chia Seeds", 100, 486, 16.5, 42.1, 30.7, 54, 0, 0, 0.5, 7.7, 631, 7.72, 335, 631, 407, 16, 7.72),
    FoodItem("Almonds", 100, 579, 21.2, 21.7, 49.9, 0, 0, 0, 25.6, 0, 269, 3.7, 268, 481, 733, 1, 3.7)
]

fruit_items = [
    FoodItem("Apples", 100, 52, 0.3, 14, 0.2, 3, 4.6, 0, 0.2, 2.2, 6, 0.12, 5, 11, 107, 1, 0),
    FoodItem("Bananas", 100, 105, 1.3, 27, 0.4, 64, 8.7, 0, 0.1, 0.5, 5, 0.26, 27, 22, 358, 1, 0),
    FoodItem("Oranges", 100, 47, 1, 12, 0.1, 225, 53.2, 0, 0.3, 0, 40, 0.2, 10, 40, 181, 0, 0),
    FoodItem("Blueberries", 100, 57, 0.7, 14.5, 0.3, 54, 9.7, 0, 0.9, 19.3, 6, 0.28, 6, 12, 77, 1, 0.2),
    FoodItem("Strawberries", 100, 32, 0.7, 7.7, 0.3, 12, 58.8, 0, 0.3, 2.2, 16, 0.41, 13, 24, 153, 1, 0.3),
    FoodItem("Avocado", 100, 160, 2, 8.5, 14.7, 7, 8.8, 0, 2.1, 21, 12, 0.55, 29, 485, 507, 7, 1),
    FoodItem("Grapes", 100, 69, 0.6, 18.1, 0.2, 66, 3.2, 0, 0.2, 0, 10, 0.36, 10, 8, 191, 0, 0.1),
    FoodItem("Kiwi", 100, 61, 1.1, 14.7, 0.5, 87, 92.7, 0, 1.1, 40.3, 34, 0.31, 17, 34, 268, 3, 0.3),
    FoodItem("Mangoes", 100, 60, 0.8, 15, 0.4, 54, 45.7, 0, 0.9, 16.5, 11, 0.16, 11, 11, 168, 1, 0),
    FoodItem("Pineapple", 100, 50, 0.5, 13.1, 0.1, 58, 47.8, 0, 0.1, 0.1, 13, 0.29, 13, 1, 109, 1, 0),
    FoodItem("Papaya", 100, 43, 0.5, 10.8, 0.3, 47, 60.9, 0, 0.3, 5.5, 20, 0.25, 10, 20, 182, 1, 0.1),
    FoodItem("Peaches", 100, 39, 0.9, 9.5, 0.3, 96, 6.6, 0, 0.2, 6.6, 9, 0.25, 11, 11, 190, 1, 0),
    FoodItem("Watermelon", 100, 30, 0.6, 7.6, 0.2, 28, 8.1, 0, 0.1, 0, 7, 0.24, 10, 11, 112, 1, 0),
    FoodItem("Cherries", 100, 50, 1.1, 12.2, 0.3, 64, 7, 0, 0.2, 0, 13, 0.36, 13, 17, 173, 0, 0),
    FoodItem("Pears", 100, 57, 0.4, 15.2, 0.1, 38, 4.2, 0, 0.1, 4.2, 9, 0.18, 8, 11, 119, 1, 0)
]

vegetable_items = [
    FoodItem("Spinach", 100, 23, 2.9, 3.6, 0.4, 469, 28.1, 0, 2, 483, 99, 2.7, 79, 49, 558, 79, 0.5),
    FoodItem("Broccoli", 100, 55, 3.7, 10, 0.6, 623, 89.2, 0, 0.8, 101, 47, 1.1, 21, 66, 316, 33, 0.6),
    FoodItem("Kale", 100, 35, 2.9, 6.7, 0.5, 681, 89.3, 0, 1.7, 1067, 62, 1.7, 47, 62, 447, 92, 1),
    FoodItem("Bell Peppers", 100, 31, 0.99, 6, 0.3, 569, 128.1, 0, 1.3, 0, 90, 0.3, 7, 9, 128, 60, 2.5),
    FoodItem("Carrots", 100, 41, 0.93, 9.58, 0.24, 16706, 33.5, 0, 0.3, 16.9, 8, 0.24, 8, 3, 33, 16, 0.6),
    FoodItem("Brussels Sprouts", 100, 43, 3.38, 8.95, 0.3, 859, 85, 0, 0.9, 219, 85, 1.3, 75, 86, 320, 64, 0.4),
    FoodItem("Cauliflower", 100, 25, 1.92, 4.97, 0.28, 177, 112, 0, 0.5, 44, 16, 0.4, 15, 61, 177, 22, 0.2),
    FoodItem("Asparagus", 100, 20, 2.2, 3.88, 0.12, 215, 38, 0, 0.5, 24, 38, 0.5, 52, 54, 24, 34, 0.2),
    FoodItem("Green Beans", 100, 31, 1.83, 6.97, 0.22, 37, 27, 0, 1, 37, 16, 0.4, 27, 37, 209, 16, 0.6),
    FoodItem("Sweet Potatoes", 100, 86, 1.57, 20.12, 0.05, 14187, 709, 0, 0.4, 337, 97, 2, 54, 29, 337, 21, 0.4),
    FoodItem("Zucchini", 100, 17, 1.21, 3.11, 0.32, 221, 16, 0, 0.2, 9, 33, 0.3, 16, 18, 221, 16, 0.1),
    FoodItem("Cabbage", 100, 25, 1.28, 5.8, 0.1, 93, 36, 0, 0.3, 42, 45, 0.2, 34, 23, 93, 49, 0.2),
    FoodItem("Eggplant", 100, 25, 0.98, 5.88, 0.18, 237, 14, 0, 0.1, 14, 14, 0.3, 23, 14, 237, 14, 0.2),
    FoodItem("Cucumbers", 100, 15, 0.65, 3.63, 0.11, 8, 3.2, 0, 0.1, 2.8, 7, 0.1, 2, 2, 8, 14, 0.2),
    FoodItem("Red Onion", 100, 40, 1.1, 9.3, 0.1, 7, 1.6, 0, 0.1, 0, 4, 0.1, 1, 7, 7, 21, 0.1),
    FoodItem("White Onion", 100, 42, 1.1, 9.3, 0.1, 6, 1.7, 0, 0.1, 0, 5, 0.1, 1, 6, 7, 18, 0.1)
]

other_items = [
    FoodItem("Rice", 100, 130, 2.7, 28.2, 0.3, 2, 0.6, 0, 0.1, 0, 2, 0.7, 1, 6, 30, 28, 0),
    FoodItem("Whole Wheat Bread", 100, 247, 9.4, 49.7, 2.7, 41, 7.8, 0, 1.9, 11, 18, 1.7, 51, 7, 0, 7, 0),
    FoodItem("Oats", 100, 389, 16.9, 66.3, 6.9, 51, 10, 4, 0, 0, 0, 0, 0, 6, 5, 0, 0),
    FoodItem("Greek Yogurt (Fat-Free)", 100, 59, 10, 3.6, 0.4, 3, 0.1, 0, 0, 1, 44, 0, 0, 1, 0, 2, 0),
    FoodItem("Eggs", 100, 155, 12.6, 1.1, 10.6, 140, 0.1, 28, 0, 1.5, 47, 0, 0, 0.5, 1, 0, 6),
    FoodItem("Sourdough Bread", 100, 235, 8.5, 48.2, 2.7, 38, 6.2, 0, 1.2, 6, 17, 1.3, 39, 5, 0, 6, 0),
    FoodItem("Pasta (Whole Wheat)", 100, 371, 13.4, 72.8, 1.5, 74, 11, 0, 2, 30, 7, 0, 3, 2, 2, 0, 0),
    FoodItem("Cheese (Cheddar)", 100, 402, 25, 1.3, 33.1, 72, 0.06, 26, 0, 0.03, 20, 0, 0, 0.2, 0, 0, 0)
]

# added all lists to one big list

predefined_food_items = fish_items + meat_items + fruit_items + vegan_protein_items + vegetable_items + other_items
food_items_dict = {food_item.name.lower(): food_item for food_item in predefined_food_items}

if __name__ == "__main__":
    def food_list():
        #iterates over all the food items in predefined_food_items and prints the name
        for food_item in predefined_food_items:
            print(food_item.name)
        return food_item.name

    def meal_name():
        #asks user for name of meal
        meal_name = input("What would you like to call this meal? ")
        return meal_name.capitalize()

    def add_ingredient(ingredients):
        # Loop to continuously prompt user for action until valid option selected
        while True:
            # Prompt the user to choose an action: add ('a'), remove ('r'), or create ('create')
            action = input("""Type a/r to add or remove an ingredient or type "create" if you have added all ingredients.""").strip().lower()
            if action.lower() == "a": # If user selects 'a', call add_a_meal function
                add_a_meal(ingredients)
            elif action.lower() == "r":
                remove_ingredients(ingredients)
                # return ingredients
            elif action.lower() == "create": # If user selects 'create', return the ingredients and exit the function
                #returns ingredients and exits this function
                return ingredients
            else:
                return add_ingredient(ingredients)

    # def weight_adjust(ingredients):

    def add_a_meal(ingredients):
        food_list()

        while True:
            user_selection = input("Select an ingredient from our list: ").strip().lower()
            matches = difflib.get_close_matches(user_selection, [item.name.lower() for item in predefined_food_items], n=5)
            #first 5 indices match user selection
            if matches:
                for i, match in enumerate(matches, 1):
                    print(f"{i}. {match}")
                user_choice = input("Did you mean one of these? Type the number or 'no' to retry: ").strip()
                if user_choice == "no":
                    continue
                try:
                    index = int(user_choice) - 1
                    closest_match = matches[index]
                    user_selection = closest_match
                except (ValueError, IndexError):
                    print("Invalid choice. Please try again.")
                    continue
                # closest_match = matches[0]
                # if closest_match != user_selection:
                #     print("Did you mean:", closest_match)
                #     user_confirm = input("Type 'yes' to confirm or 'no' to retry: ").strip().lower()
                #     if user_confirm == 'yes':
                #         user_selection = closest_match  # Update user selection with the closest match
                #     elif user_confirm == 'no':
                #         continue  # Retry if user doesn't confirm
            for food_item in predefined_food_items:
                if user_selection.lower() == food_item.name.lower():
                    # ingredient = food_items_dict[user_selection.lower()]
                    # ingredients.append(ingredient)

                    ingredient_weight = input("How many grams of this would you like to add?")
                    multiplier = int(ingredient_weight) / food_item.weight
                    calories_adjusted = food_item.calories * multiplier
                    protein_adjusted = food_item.protein * multiplier
                    carbs_adjusted = food_item.carbohydrates * multiplier
                    fats_adjusted = food_item.fats * multiplier


                    adjusted_ingredient = FoodItem(food_item.name, ingredient_weight, calories_adjusted, protein_adjusted, carbs_adjusted, fats_adjusted)
                    ingredients.append(adjusted_ingredient)

                    print("Calories: ", food_item.calories  * multiplier)
                    print("Protein: ", food_item.protein  * multiplier)
                    print("Carbohydrates: ", food_item.carbohydrates  * multiplier)
                    print("Fats: ", food_item.fats  * multiplier)
                    add_ingredient(ingredients)
                    return "Ingredient added successfully!"

            print("This ingredient is not in our list")

    def remove_ingredients(ingredients):
        if len(ingredients) > 0:
            print("Ingredients: ", [ingredient.name for ingredient in ingredients])
            ingredient_to_remove = input("Please type the ingredient you want to remove: ").strip().lower()
            for ingredient in ingredients:
                if ingredient_to_remove == ingredient.name.lower():
                    ingredients.remove(ingredient)
                    print("Ingredient removed:", ingredient_to_remove)
                    print("Ingredients remaining: ", [ingredient.name for ingredient in ingredients])
                    if len(ingredients) > 0:
                        add_ingredient(ingredients)
                        return remove_ingredients(ingredients)
                    else:
                        while True:
                            choice = input("You have no ingredients remaining. Would you like to add some(Yes/No)").strip().lower()
                            if choice == "yes":
                                add_a_meal(ingredients)
                                break
                            elif choice == "no":
                                print("Exiting app")
                                sys.exit()
                            else:
                                print("Invalid choice. Please enter 'Yes' or 'No'.")
                                continue
                        break
            else:
                print("This ingredient is not in your list.")
                return remove_ingredients(ingredients)  # Recursive call if ingredient not found

    # if __name__ == "__main__":
    def create_meal(meal_list):
        ingredients = []
        add_a_meal(ingredients)
        meal = meal_name()
        print("Created: ", meal + ", with ", [ingredient.name for ingredient in ingredients])

    # create meal object and add it to the meal list
        meal_list.append(Meal(meal, ingredients))
    meal_list = []

    create_meal(meal_list)

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

    total_calories = calculate_calories()
    total_protein = calculate_protein()
    total_carbohydrates = calculate_carbohydrates()
    total_fats = calculate_fats()
    # Print the total calories of the meal
    print("Total calories of the meal:", total_calories)
    print("Total protein of the meal:", total_protein)
    print("Total carbohydrates of the meal:", total_carbohydrates)
    print("Total fats of the meal:", total_fats)

    def get_user_info(total_calories):
        gender = input("Enter your gender (M/F): ").strip().upper()
        age = int(input("Enter your age: "))
        activity_level = input("Enter your activity level (Sedentary/Moderately Active/Active): ").strip().lower()
        recommended, calorie_range = recommended_calories(gender, age, activity_level, total_calories)
        if recommended:
            print("Your meal is within the recommended calorie range. 4 points added to your score.")
        else:
            print("Your meal is not within the recommended calorie range. 0 points added to your score.")
            difference =  min(calorie_range) -  total_calories
            print("You need to add", str(difference) + " calories" )
        # return gender, age, activity_level
    get_user_info(total_calories)

    def protein_percentage_calculator():
        if protein_percentage < 35:
            print("Protein Percentage: ", str(protein_percentage) + "%")
            protein_difference = 35 - protein_percentage
            print(str(protein_difference) + " more grams of protein to hit the target for protein intake in this meal")
        else:
            print("Protein Percentage: ", protein_percentage)
            print("This is a healthy amount of protein")

    def carb_percentage_calculator():
        if carbohydrates_percentage > 45:
            print("Carb Percentage: ", str(carbohydrates_percentage) + "%")
            print("You have gone over you carbohydrate target, consider balancing your meal out with more protein")
        else:
            print("Carb Percentage: ", str(carbohydrates_percentage))
            print("This is a healthy amount of carbs")

    def fats_percentage_calculator():
        if fats_percentage < 20:
            print("Fats Percentage: ", str(fats_percentage) + "%")
            fats_difference =  20 - fats_percentage
            print(str(fats_difference) + " more grams of fats to hit the target for fat intake in this meal. Consider adding some more healthy fats.")
        else:
            print("Fats Percentage: ", fats_percentage)
            print("This is a healthy amount of fats")

    total_macros = total_protein + total_carbohydrates + total_fats

    protein_percentage = (total_protein / total_macros) * 100
    carbohydrates_percentage = (total_carbohydrates / total_macros) * 100
    fats_percentage = (total_fats / total_macros) * 100

    protein_percentage_calculator()
    carb_percentage_calculator()
    fats_percentage_calculator()

    def meal_rating():
        pass


    def recommended_calories(gender, age, activity_level, total_calories):
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
