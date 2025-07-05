class Recipe:
    def __init__(self, recipe_id, name, ingredients, description):
        self.id = recipe_id
        self.name = name
        self.ingredients = ingredients  # list of ingredients
        self.description = description

    def display(self):
        print(f"Recipe ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Ingredients: {', '.join(self.ingredients)}")
        print(f"Description: {self.description}")
        print("-" * 30)

class RecipeBook:
    def __init__(self):
        self.recipes = []  # list to store Recipe objects

    def add_recipe(self, recipe):
        self.recipes.append(recipe)
        print(f"Recipe '{recipe.name}' added successfully!")

    def display_all(self):
        if not self.recipes:
            print("No recipes in the book.")
            return
        print("\n--- Recipe Book ---")
        for recipe in self.recipes:
            recipe.display()

# Example usage:
if __name__ == "__main__":
    book = RecipeBook()

    # Create some recipes
    r1 = Recipe(1, "Pancakes", ["Flour", "Eggs", "Milk", "Sugar", "Baking Powder"], "Mix ingredients and cook on skillet.")
    r2 = Recipe(2, "Scrambled Eggs", ["Eggs", "Butter", "Salt"], "Beat eggs and cook with butter until fluffy.")

    # Add recipes to the book
    book.add_recipe(r1)
    book.add_recipe(r2)

    # Display all recipes
    book.display_all()
