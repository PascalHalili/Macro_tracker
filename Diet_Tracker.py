# import tkinter
class Diet:
    def __init__(self, breakfast_calories_1, lunch_calories_1, dinner_calories_1, exercise_1, bmr_1):
        self.breakfast_calories = breakfast_calories_1
        self.lunch_calories = lunch_calories_1
        self.dinner_calories = dinner_calories_1
        self.exercise = exercise_1
        self.bmr = bmr_1

    def calorie_deficit(self):
        deficit = self.bmr + self.exercise - (self.breakfast_calories + self.lunch_calories + self.dinner_calories)
        return deficit


breakfast_calories = int(input("Breakfast calories: "))
lunch_calories = int(input("Lunch calories: "))
dinner_calories = int(input("Dinner calories: "))
exercise = int(input("Calories burned through exercise: "))
bmr = int(input("Basic metabolic rate: "))

fitness = Diet(breakfast_calories, lunch_calories, dinner_calories, exercise, bmr)
weekly_deficit = 7 * fitness.calorie_deficit()

if weekly_deficit > 0:
    print(f"You will loose {round(weekly_deficit / 7000, 2)} kg per week.")
elif weekly_deficit == 0:
    print(f"Your weight will stay the same.")
else:
    print(f"You will gain {round(-1 * weekly_deficit / 7000, 2)} kg per week.")
