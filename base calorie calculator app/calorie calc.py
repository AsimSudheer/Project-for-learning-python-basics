
calories = []

def add_food(food,grams):
    calorie = (food/100)*grams
    return calorie

def total_food():
    print("Total calories in a day:",sum(calories))


while True:
    print("--------------------------------------------------")
    print("1.Add food\n2.View Total calorie\n3.Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print("-----ADD FOOD-----")
        food = input("Enter the name of the food:")
        grams = int(input("Enter the amount of food:"))
        calorie = add_food(food,grams)
        calories.append(calorie)
        print("The food has been added")
    elif choice == 2:
        print("----TOTAL----")
        total_food()
    elif choice == 3:
        break