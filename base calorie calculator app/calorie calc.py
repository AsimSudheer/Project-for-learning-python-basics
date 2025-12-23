from datetime import datetime
food_loq =[]

food_calories = {
    "rice": 130,
    "egg": 155,
    "apple": 52,
    "banana": 89,
    "bread": 265
}

def save_to_file():
    now = datetime.now()
    time = now.strftime("%y - %m - %d %H:%M" )
    with open("food info.txt","a") as file:
        file.write(f"------{time}------\n\n")
        file.write("-----Next Day-----\n")
        for item in food_loq:
            file.write(item+"\n")
        file.write(f"Total calories is {sum(calories):.2f} kcal\n\n")
calories = []

def add_food(food_name,grams):
    calorie = (food_name/100)*grams
    return calorie

def total_food():
    print("Total calories in a day:",sum(calories))


while True:
    print("--------------------------------------------------")
    print("1.Add food\n2.View Total calorie\n3.Exit")
    try:
        choice = int(input("Enter your choice:"))
    except ValueError:
        print("Enter a valid number")
    if choice == 1:
        print("-----ADD FOOD-----")
        food = input("Enter the name of the food:").lower()
        try:
            grams = int(input("Enter the amount of food:"))
        except ValueError:
            print("Enter the valid number")
        food_name = food_calories[food]
        if food_name is None:
            print("The entered food details is not available")
            continue
        calorie = add_food(food_name,grams)
        calories.append(calorie)
        food_loq.append(f"{food} - {calorie:.2f} kcal")
        print("The food has been added")
    elif choice == 2:
        print("----TOTAL----")
        total_food()
    elif choice == 3:
        save_to_file()
        print("The details has been added to the file")
        break   