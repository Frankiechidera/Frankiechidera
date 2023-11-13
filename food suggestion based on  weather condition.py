# Create a dictionary of food suggestions based on weather conditions
food_suggestions = {
    'cold': ['Hot Soup', 'Hot Chocolate', 'Grilled Cheese Sandwich'],
    'hot': ['Ice Cream', 'Salad', 'Pasta'],
    'rainy': ['Soup', 'Pasta'],
}

# Get user input for weather conditions
weather = input("Enter the current weather condition (e.g., sunny, rainy, cold, hot): ").lower()

# Check if the weather condition is in the dictionary
if weather in food_suggestions:
    suggested_food = food_suggestions[weather]
    print("Suggested food: ", suggested_food)
else:
    print("Weather condition not found in suggestions.")
