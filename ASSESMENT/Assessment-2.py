'''
Assessment
Module 13) Python – Fundamentals of Python language
Module 14) Python – Collections, Functions, and Modules in Python Case Overview Scenario :
You are a trainee Python developer at ReadEase Library, a popular local library known for its wide collection of books and eBooks.
Currently, the librarian manually maintains book rentals and returns, leading to duplicate rentals, late return confusion, and difficulty tracking inventory.
The management requests a Python-based console program named RentTrack, which allows staff to manage book rentals, returns, and generate rental summaries — using only core Python programming features.
Core functionality 1. Book Rental Booking
• Allows librarian to record a new book rental.
• Captures customer name, book title, rental date, and expected return date. 2. Book Return & Late Fee Calculation
• Allows return entry of a rented book.
• Calculates late fee if returned after due date (fixed per-day penalty).
• Displays a summary receipt with customer details and payment. Key Competencies Tested
• Python Concepts: Functions, Looping (for, while), Collections (lists, dictionaries), Input/output formatting Practical Considerations
• Temporary in-memory data handling
• Clean, function-based modular structure
• Basic input validation and user prompts
• Neat receipt generation with rental summary Reflective Thinking
• Can this be extended to support file handling for rental history?
• Could future versions add QR code scanning for book IDs?
• How might we integrate a real-time book inventory check before renting?
'''

from datetime import datetime


rentals = []

LATE_FEE_PER_DAY = 10  


def display_menu():
    print("\n====== RentTrack Library System ======")
    print("1. Book Rental Booking")
    print("2. Book Return & Late Fee Calculation")
    print("3. View All Rentals")
    print("4. Exit")


def book_rental():
    print("\n--- Book Rental Booking ---")

    customer_name = input("Enter customer name: ").strip()
    book_title = input("Enter book title: ").strip()

    rental_date = input("Enter rental date (DD-MM-YYYY): ")
    return_date = input("Enter expected return date (DD-MM-YYYY): ")

    rental = {
        "customer": customer_name,
        "book": book_title,
        "rental_date": rental_date,
        "expected_return": return_date,
        "returned": False
    }

    rentals.append(rental)
    print("\nBook rented successfully!")


def book_return():
    print("\n--- Book Return ---")

    book_title = input("Enter book title to return: ").strip()
    found = False

    for rental in rentals:
        if rental["book"].lower() == book_title.lower() and not rental["returned"]:
            found = True
            actual_return = input("Enter actual return date (YYYY-MM-DD): ")

            due_date = datetime.strptime(rental["expected_return"], "%Y-%m-%d")
            return_date = datetime.strptime(actual_return, "%Y-%m-%d")

            late_days = (return_date - due_date).days
            late_fee = 0

            if late_days > 0:
                late_fee = late_days * LATE_FEE_PER_DAY

            rental["returned"] = True

            print("\n======= Rental Receipt =======")
            print("Customer Name :", rental["customer"])
            print("Book Title   :", rental["book"])
            print("Due Date     :", rental["expected_return"])
            print("Return Date  :", actual_return)
            print("Late Days    :", late_days if late_days > 0 else 0)
            print("Late Fee     : ₹", late_fee)
            print("==============================")
            break

    if not found:
        print("No active rental found for this book.")


def view_rentals():
    print("\n--- All Rentals ---")

    if not rentals:
        print("No rentals recorded.")
        return

    for i, rental in enumerate(rentals, start=1):
        status = "Returned" if rental["returned"] else "Active"
        print(f"{i}. {rental['book']} | {rental['customer']} | {status}")


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            book_rental()
        elif choice == "2":
            book_return()
        elif choice == "3":
            view_rentals()
        elif choice == "4":
            print("Thank you for using RentTrack!")
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
main()
