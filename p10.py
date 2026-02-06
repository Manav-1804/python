from datetime import datetime

# In-memory storage for rentals
rentals = []

LATE_FEE_PER_DAY = 10  # fixed penalty


# ---------- Function to Rent a Book ----------
def rent_book():
    print("\n--- Book Rental ---")
    customer = input("Enter customer name: ")
    book = input("Enter book title: ")
    rental_date = input("Enter rental date (DD-MM-YYYY): ")
    return_date = input("Enter expected return date (DD-MM-YYYY): ")

    if customer == "" or book == "":
        print("Error: Customer name and book title cannot be empty")
        return

    rental = {
        "customer": customer,
        "book": book,
        "rental_date": rental_date,
        "return_date": return_date,
        "returned": False
    }

    rentals.append(rental)
    print("Book rented successfully!")


# ---------- Function to Return a Book ----------
def return_book():
    print("\n--- Book Return ---")
    book = input("Enter book title to return: ")
    actual_return = input("Enter actual return date (DD-MM-YYYY): ")

    for rental in rentals:
        if rental["book"] == book and not rental["returned"]:
            rental["returned"] = True

            due_date = datetime.strptime(rental["return_date"], "%d-%m-%Y")
            actual_date = datetime.strptime(actual_return, "%d-%m-%Y")

            late_days = (actual_date - due_date).days
            late_fee = late_days * LATE_FEE_PER_DAY if late_days > 0 else 0

            print("\n----- RENTAL RECEIPT -----")
            print("Customer Name :", rental["customer"])
            print("Book Title    :", rental["book"])
            print("Rental Date   :", rental["rental_date"])
            print("Due Date      :", rental["return_date"])
            print("Return Date   :", actual_return)
            print("Late Fee      : Rs.", late_fee)
            print("-------------------------")
            return

    print("Error: Rental record not found")


# ---------- Function to Show All Rentals ----------
def show_rentals():
    print("\n--- Current Rentals ---")
    if not rentals:
        print("No rentals found")
        return

    for r in rentals:
        status = "Returned" if r["returned"] else "Not Returned"
        print(r["customer"], "-", r["book"], "-", status)


# ---------- Main Menu ----------
def main():
    while True:
        print("\n===== RentTrack Menu =====")
        print("1. Rent a Book")
        print("2. Return a Book")
        print("3. View Rentals")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            rent_book()
        elif choice == "2":
            return_book()
        elif choice == "3":
            show_rentals()
        elif choice == "4":
            print("Exiting RentTrack. Thank you!")
            break
        else:
            print("Invalid choice. Try again.")


# ---------- Run Program ----------
main()
