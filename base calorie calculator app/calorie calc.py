foods_calorie = {
    "rice":200,
    "egg":250,
    "bacon":350
}

food = input("Enter the name of the food:")
grams = int(input("Enter the grams:"))
try:
    calorie = (foods_calorie[food]/100)*grams
    print("The calorie=",calorie)
except:
    print("The entered food does not contain in the database")