favourite_foods = []

while True:
    print("Favourite Foods Manager")
    print("0. Exit")
    print("1. Add Foods")
    print("2. Remove Foods")
    print("3. View favourite all foods")

    choice = input("Choose an option: ")

    if choice == "0":
        print("Thanks for using favourite foods Manager")
        break
    elif choice == "1":
        food = input("Enter your favourite food name: ")
        favourite_foods.append(food)
        print(f"{food} added successfully")
    elif choice == "2":
        food = input("Enter a food name which you want to remove")
        favourite_foods.remove(food)
        print(f"{food} removed successfully")
    elif choice == "3":
        if favourite_foods:
            print("Your favourite foods: ")
            for index, food in enumerate(favourite_foods, start=1):
                print(f"{index}.{food}")
        else:
            print("Food List is empty or didn't added yet!")
    else:
        print("Invalid choice ")
