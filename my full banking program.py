#Cash Send
#assingment and generating of ID
#acess by many people 
#user will be able to view there account info
#user will be able to change password

class BankAccount:
    def __init__(self, username, password):
        self.username = username
        self.password = password 
        self.balance = 0.0  # Defaundlt balance is 0       
    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}.Thanks {self.username} New balance is ${self.balance}.")
        else:
            print("Invalid deposit amount!")
 
    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}.Thanks {self.username} New balance is ${self.balance}.")
        elif amount > self.balance:
            print("Insufficient funds!")
        else:
            print("Invalid withdrawal amount!")

    def view_balance(self):
        """Display the current balance."""
        print(f"Your current balance is: ${self.balance}")
     
class BankSystem:   # A dictonary to gather group of info that talk about the same thing
    def __init__(self):
        self.users = {}  # A dictionary to store users

    def create_account(self):
        """Create a new bank account."""
        
        print("To create a account please follow the steps")
        
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        
        email = input("Enter your email: ")
        if username in self.users:
            print("Username already exists. Please choose a different username.")
        else:
            new_account = BankAccount(username, password)
            self.users[username] = new_account
            print(f"Account created for {username} successfully.")

    def login(self):
        """Login to an existing account."""
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if username in self.users and self.users[username].password == password:
            print(f"Welcome back, {username}!")
            return self.users[username]
        else:
            print("Invalid credentials. Try again.")
            return None

    def menu(self, account):  # A coplete format on my cash Send online Banking system..
        """Show the menu options after successful login."""
        while True:
            print("Cash Send Bank Menu:")
            print("1. Deposit Money")
            print("2. Withdraw Money")
            print("3. View Balance")
            print("4. Logout")
            choice = input("Choose an option (1-4): ")

            if choice == "1":
                amount = float(input("Enter amount to deposit: $"))
                account.deposit(amount)
            elif choice == "2":
                amount = float(input("Enter amount to withdraw: $"))
                account.withdraw(amount)
            elif choice == "3":
                account.view_balance()
            elif choice == "4":
                print("Logging out...")
                break
            else:
                print("Invalid choice, please select between 1-4.")

def main():         # The first platform that will be seen by the user when code has been exicuted...
    bank_system = BankSystem()

    while True:
        print("\nWelcome to the Cash Send Banking System")
        print("how may we assist you today?")
        print("1. Create a new account")
        print("2. Login to an existing account")
        print("3. Lone service")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            bank_system.create_account()
        elif choice == "2":
            account = bank_system.login()
            if account:
                bank_system.menu(account)
        elif choice =="3":
            print("This service is corrently under mentanance please chose any of the other obtion in the list!")
        elif choice == "4":
            print("Thank you for using Cash Send banking system!")
            print("A project by Samuel Alex Montgomery")
            break
        else:
            print("Invalid choice, please select between 1-3.")
            
if __name__ == "__main__":
    main()
