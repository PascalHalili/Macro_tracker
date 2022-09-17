import numpy as np
import matplotlib.pyplot as plt

from calories_tracker.food import Food

CALORIE_GOAL_LIMIT = 1800
PROTEIN_GOAL = 140
FAT_GOAL = 50
CARBS_GOAL = 150

today = []


def add_food():
    print("Adding a new food!")
    name = input("Name: ")
    calories = int(input("Calories: "))
    proteins = int(input("Proteins: "))
    fat = int(input("Fat: "))
    carbs = int(input("Carbs: "))
    food = Food(name, calories, proteins, fat, carbs)
    today.append(food)
    print("Successfully added!")


def display_calories():
    calorie_sum = sum(food.calories for food in today)
    protein_sum = sum(food.protein for food in today)
    fat_sum = sum(food.fat for food in today)
    carb_sum = sum(food.carbs for food in today)

    fig, axis = plt.subplots(2, 2)
    axis[0, 0].pie([protein_sum, fat_sum, carb_sum], labels=["Protein", "Fat", "Carbs"], autopct="%1.1f%%")
    axis[0, 0].set_title("Macro Distribution")
    axis[0, 1].bar([0, 1, 2], [protein_sum, fat_sum, carb_sum], width=0.4)
    axis[0, 1].bar([0.5, 1.5, 2.5], [PROTEIN_GOAL, FAT_GOAL, CARBS_GOAL], width=0.4)
    axis[0, 1].set_title("Macro Progress")
    axis[1, 0].pie([calorie_sum, CALORIE_GOAL_LIMIT - calorie_sum], labels=["Calories", "Remaining"], autopct="%1.1f%%")
    axis[1, 0].set_title("Calories Goal Progress")
    axis[1, 1].plot(np.array(range(len(today))), np.cumsum([food.calories for food in today]), label="Calories Eaten")
    axis[1, 1].axhline(y=CALORIE_GOAL_LIMIT, color='r', linestyle='-', label="Calorie Goal")
    axis[1, 1].legend()
    axis[1, 1].set_title("Calories Goal Over Time")
    fig.tight_layout()
    plt.show()


def show_menu():
    print("""
          (1) Add new food
          (2) Visualize progress
          (q) Quit
          """)


def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_food()
        elif choice == "2":
            display_calories()
        elif choice == "q":
            break
        else:
            print("Invalid Choice!")


if __name__ == '__main__':
    main()
