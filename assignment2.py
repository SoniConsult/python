# question 1
def classify_number(num):
    if num <= 0:
        return "Neither prime nor composite"
    elif num == 1:
        return "Neither prime nor composite"
    elif num == 2:
        return "Prime"
    for i in range(2, num):
        if num % i == 0:
            return "Composite"
    return "Prime"

try:
    num = int(input("Enter a number: "))
    print(classify_number(num))
except ValueError:
    print("Invalid input")
  
# classify_number(7)

# question 2

# creating list of library
library = []

def menu():
    print("\nLibrary Menu:")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. List all books")
    print("5. Exit")

def add_book():
    book = input("Enter the book name: ")
    library.append(book)
    print(f"'{book}' added to library.")

def remove_book():
    book = input("Enter the book name to remove: ")
    if book in library:
        library.remove(book)
        print(f"'{book}' removed from library.")
    else:
        print(f"'{book}' not found in library.")

def list_books():
    if library:
        print("\nBooks in the library:")
        for book in library:
            print(book)
    else:
        print("No books in the library.")

while True:
    menu()
    choice = input("Choose an option: ")
    if choice == '1':
        add_book()
    elif choice == '2':
        remove_book()
    elif choice == '3':
        search = input("Enter the book name to search: ")
        if search in library:
            print(f"'{search}' is in the library.")
        else:
            print(f"'{search}' is not in the library.")
    elif choice == '4':
        list_books()
    elif choice == '5':
        print("Exiting the system.")
        break
    else:
        print("Invalid option, try again.")

# menu()

# question 3

balance = 1000

def atm_menu():
    print("\nATM Menu:")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

def check_balance():
    print(f"Your balance is: ${balance}")

def deposit():
    global balance
    try:
        amount = float(input("Enter amount to deposit: "))
        balance += amount
        print(f"Deposited ${amount}. New balance: ${balance}")
    except ValueError:
        print("Invalid amount.")

def withdraw():
    global balance
    try:
        amount = float(input("Enter amount to withdraw: "))
        if amount > balance:
            print("Insufficient funds.")
        else:
            balance -= amount
            print(f"Withdrew ${amount}. New balance: ${balance}")
    except ValueError:
        print("Invalid amount.")

while True:
    atm_menu()
    choice = input("Choose an option: ")
    if choice == '1':
        check_balance()
    elif choice == '2':
        deposit()
    elif choice == '3':
        withdraw()
    elif choice == '4':
        print("Exiting the ATM system.")
        break
    else:
        print("Invalid option, try again.")
# atm_menu()



