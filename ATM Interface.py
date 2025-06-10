class ATM:
    def __init__(self):
        self.balance = 10000  # Default balance
        self.pin = "1234"     # Default PIN
        self.attempts = 0

    def authenticate(self):
        while self.attempts < 3:
            entered_pin = input("Enter your 4-digit PIN: ")
            if entered_pin == self.pin:
                print("✅ Authentication successful.\n")
                return True
            else:
                self.attempts += 1
                print(f"❌ Incorrect PIN. Attempts left: {3 - self.attempts}")
        print("❌ Too many incorrect attempts. Card blocked.")
        return False

    def show_menu(self):
        print("\n==== ATM MENU ====")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Exit")

    def check_balance(self):
        print(f"💰 Current balance: ₹{self.balance}")

    def withdraw(self):
        try:
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= 0:
                print("❌ Invalid amount.")
            elif amount > self.balance:
                print("❌ Insufficient balance.")
            else:
                self.balance -= amount
                print(f"✅ ₹{amount} withdrawn successfully.")
                self.check_balance()
        except ValueError:
            print("❌ Please enter a valid number.")

    def deposit(self):
        try:
            amount = float(input("Enter amount to deposit: ₹"))
            if amount <= 0:
                print("❌ Invalid amount.")
            else:
                self.balance += amount
                print(f"✅ ₹{amount} deposited successfully.")
                self.check_balance()
        except ValueError:
            print("❌ Please enter a valid number.")

    def run(self):
        if self.authenticate():
            while True:
                self.show_menu()
                choice = input("Choose an option (1-4): ")

                if choice == "1":
                    self.check_balance()
                elif choice == "2":
                    self.withdraw()
                elif choice == "3":
                    self.deposit()
                elif choice == "4":
                    print("👋 Thank you for using the ATM. Goodbye!")
                    break
                else:
                    print("❌ Invalid choice. Please try again.")

# Run the ATM
atm_machine = ATM()
atm_machine.run()
