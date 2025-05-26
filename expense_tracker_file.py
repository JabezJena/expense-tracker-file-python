# Mini Project Expense Tracker ! 

def add_expenses():
    category = input("Enter the category of expense: ")
    amount = input("Enter the amount spent: ")

    try :
        amount = float(amount)
        with open("e.txt", "a") as f :
            f.write(f"{category} - {amount}\n")
        print("Expense Added successfully!")
    except ValueError :
        print("Please Enter a proper Number ! ")

def view_expenses():
    print("Your Expenses : ")
    try :
        with open("e.txt","r") as f:
            data = f.read()
            print(data if data else "No expense yet.")
    except FileNotFoundError:
        print("No expense added yet ! ")
    
while True :
    print("Expense Tracker ! \n1. Add Expense \n2. View Expenses \n3. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_expenses()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        break
    else :
        print("Invalid choice, please try again.")