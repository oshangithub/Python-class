def find_animal(food):
    animal_dict = {
        "meat": ["lion", "tiger", "bear"],
        "grass": ["elephant", "zebra"],
        "leaves": ["elephant", "giraffe"],
        "bamboo": ["panda"],
        "fruits": ["monkey"],
        "insects": ["monkey"],
    }

    herbivorous = []
    carnivorous = []
    omnivorous = []

    # Check each animal in the dictionary
    for animal, foods in animal_dict.items():
        if food in foods:
            if animal in herbivorous:
                return f"The herbivorous animal that eats {food} is {animal}"
            elif animal in carnivorous:
                return f"The carnivorous animal that eats {food} is {animal}"
            elif animal in omnivorous:
                return f"The omnivorous animal that eats {food} is {animal}"
            else:
                return "Unknown"

    return "Unknown"

# Define the classifications of animals
herbivorous = ["elephant", "giraffe", "zebra", "panda", "monkey"]
carnivorous = ["lion", "tiger", "bear"]
omnivorous = ["bear"]

# Test the function
food = input("Enter a food: ")

if food in herbivorous:
    print(f"The herbivorous animals that eat {food} are:", ", ".join(herbivorous))
elif food in carnivorous:
    print(f"The carnivorous animals that eat {food} are:", ", ".join(carnivorous))
elif food in omnivorous:
    print(f"The omnivorous animals that eat {food} are:", ", ".join(omnivorous))
else:
    print("Unknown food or no animal eats it.")
