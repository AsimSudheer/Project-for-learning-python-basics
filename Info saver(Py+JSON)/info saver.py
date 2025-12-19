import json
people = []

def display(people):
    for i,person in enumerate(people):
        print(i+1,"-",person["Name"],"|",person["Age"],"|",person["Email"])


def add_person():
    name = input("Enter the name:")
    age = input("Enter the age:")
    email = input("Enter the email:")
    person = {"Name":name,"Age":age,"Email":email}
    return person

def del_person(people):
    display(people)
    while True:
        number = input("Enter the number you want to delete:")
        try:
            number = int(number)
            if number <=0 or number >len(people):
                print("Enter a valid number")
            else:
                break
        except:
            print("invalid entry type")
    people.pop(number - 1)
    print("----The user has been deleted---")

def search(people):
    results = []
    search_name = input("Enter the name of the user:").lower()
    for person in people:
        name = person["Name"]
        if search_name in name.lower():
            results.append(person)
    display(results)

with open("contacts.json","r") as f:
    people = json.loads(f)["contacts"]

while True:
    choice = input("Enter the task 'add','delete','search','display' or 'q':").lower()
    if choice == "add":
       person = add_person()
       people.append(person)
       print("---The person has been added---")
    elif choice == "delete":
        del_person(people)
    elif choice == "search":
        search(people)
    elif choice == "q":
        break
    elif choice == "display":
        display(people)
    else:
        print("invalid  entry")

with open("contacts.json", "w") as f:
    people = json.loads(f)["contacts.json"]
