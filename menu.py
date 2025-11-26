def punjabi_menu(option):
    dinning_menu = [
        ("Paneer Butter Masala", 250),
        ("Chole Bhature", 120),
        ("Dal Makhani", 180),
        ("Aloo Paratha", 90),
        ("Amritsari Kulcha", 150)
    ]

    packed_menu = [
        ("Paneer Tikka", 200),
        ("Veg Biryani", 160),
        ("Rajma Chawal", 150),
        ("Kadhi Chawal", 130),
        ("Stuffed Naan Combo", 180)
    ]

    
    if option.lower() == "dinning":
        print("Punjabi Dinning Menu")
        for item, price in dinning_menu:
            print(f"{item}")

    elif option.lower() == "packed":
        print("Punjabi Packed Menu")
        for item, price in packed_menu:
            print(f"{price} Rs")

    else:
        print("Invalid Option! Please choose 'dinning' or 'packed'.")


def chinese_menu(option):
    dinning_menu = [
        ("Veg Manchurian Gravy", 180),
        ("Hakka Noodles", 150),
        ("Veg Fried Rice", 140),
        ("Chilli Paneer", 220),
        ("Spring Rolls", 120)
    ]

    packed_menu = [
        ("Veg Momos (10 pcs)", 120),
        ("Schezwan Rice", 160),
        ("Garlic Noodles", 150),
        ("Crispy Veg", 180),
        ("Paneer Momos (8 pcs)", 150)
    ]

    
    if option.lower() == "dinning":
        print("Chinese Dinning Menu")
        for item, price in dinning_menu:
            print(f"{item}")

    elif option.lower() == "packed":
        print("Chinese Packed Menu")
        for item, price in packed_menu:
            print(f"{price} Rs")

    else:
        print("Invalid Option! Please choose 'dinning' or 'packed'.")

def dessert_menu(option):
    dinning_menu = [
        ("Gulab Jamun (2 pcs)", 60),
        ("Rasmalai (2 pcs)", 80),
        ("Chocolate Brownie", 120),
        ("Ice Cream Scoop", 50),
        ("Shahi Tukda", 90)
    ]

    packed_menu = [
        ("Gajar Halwa (200g)", 100),
        ("Kaju Katli (100g)", 140),
        ("Ladoo Box (4 pcs)", 80),
        ("Dry Fruit Barfi (150g)", 160),
        ("Rasgulla (2 pcs)", 50)
    ]

    if option.lower() == "dinning":
        print("Dessert Dinning Menu")
        for item, price in dinning_menu:
            print(f"{item}")

    elif option.lower() == "packed":
        print("Dessert Packed Menu")
        for item, price in packed_menu:
            print(f"{price} Rs")

    else:
        print("Invalid Option! Choose 'dinning' or 'packed'.")

def gujarati_menu(option):
    dinning_menu = [
        ("Gujarati Thali", 180),
        ("Undhiyu", 150),
        ("Khaman Dhokla", 40),
        ("Sev Tameta", 120),
        ("Bhakri & Shaak", 90)
    ]

    packed_menu = [
        ("Thepla Pack (6 pcs)", 60),
        ("Fafda Jalebi Pack", 100),
        ("Handvo Slice", 50),
        ("Patra Pack", 70),
        ("Muthiya Pack", 80)
    ]

    if option.lower() == "dinning":
        print("Gujarati Dinning Menu")
        for item, price in dinning_menu:
            print(f"{item}")

    elif option.lower() == "packed":
        print("Gujarati Packed Menu")
        for item, price in packed_menu:
            print(f"{price} Rs")

    else:
        print("Invalid Option")

def south_indian_menu(option):
    dinning_menu = [
        ("Masala Dosa", 90),
        ("Idli Sambar", 60),
        ("Medu Vada", 70),
        ("Onion Uttapam", 100),
        ("Rava Dosa", 110)
    ]

    packed_menu = [
        ("Mini Idli Pack", 50),
        ("Curd Rice", 80),
        ("Lemon Rice", 70),
        ("Upma Pack", 60),
        ("Pongal Pack", 85)
    ]

    if option.lower() == "dinning":
        print("South Indian Dinning Menu")
        for item, price in dinning_menu:
            print(f"{item}")

    elif option.lower() == "packed":
        print("South Indian Packed Menu")
        for item, price in packed_menu:
            print(f"{price} Rs")

    else:
        print("Invalid Option")
