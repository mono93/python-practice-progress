class IngredientProcessor:
    @staticmethod
    def parse_recipe_items(raw_ingredient_text):
        """Splits a comma-separated string into a clean list of individual ingredients."""
        return [ingredient.strip() for ingredient in raw_ingredient_text.split(",")]


# Test dataset using a descriptive name
raw_beverage_ingredients = " water , milk , ginger , honey "

# Calling the static method directly from the class
cleaned_ingredients_list = IngredientProcessor.parse_recipe_items(raw_beverage_ingredients)

print(cleaned_ingredients_list)
# Output: ['water', 'milk', 'ginger', 'honey']
