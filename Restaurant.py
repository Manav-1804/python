import menu

while True:
    print("\n===== Restaurant Menu =====")
    print("1. Punjabi")
    print("2. Chinese")
    print("3. Dessert")
    print("4. Gujarati")
    print("5. South Indian")
    print("6. Exit")

    print("-" * 40)

    choice = int(input("Enter your choice: "))
    if choice == 6:
        print("Thank you! Visit again.")
        break

    type_menu = input("Enter type (dinning / packed): ")

    if choice == 1:
        menu.punjabi_menu(type_menu)
    elif choice == 2:
        menu.chinese_menu(type_menu)
    elif choice == 3:
        menu.dessert_menu(type_menu)
    elif choice == 4:
        menu.gujarati_menu(type_menu)
    elif choice == 5:
        menu.south_indian_menu(type_menu)
    else:
        print("Invalid Choice")

   
