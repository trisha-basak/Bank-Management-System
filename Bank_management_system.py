import time
class Account:
    def __init__(self, name, email, address, balance, accountType) -> None:
        self.name = name
        self.email = email
        self.address = address
        self.accountType = accountType #Mainly Two Types: Savings & Cuurent
        self.account_create = int(time.time())
        self.transaction = []
        self.loan_cnt = 1
        self.loan_amount = 0
        self.balance = balance
        self.minwithdrow = 100
        self.maxwithdrow = 1000000

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction.append(f"Deposited {amount}")
        print(f"Deposited {amount} Taka. New balance is {self.balance} Taka")
    
    def withdrow(self, amount):
        if amount < self.minwithdrow:
            print(f'Wothdrow more then {self.minwithdrow}')
        elif amount > self.maxwithdrow:
            print('Not possible')
        elif amount > self.balance:
            print('Withdrawal amount exceeded')
        else:
            self.balance -= amount
            print(f'Here is your money {amount}')
            print(f'Corrent balance {self.balance}')

    def check_balance(self):
        total = self.balance + self.loan_amount
        print(f"Available balance: {total}")

    def transaction_history(self):
        print(f"Transaction History")
        for transaction in self.transaction:
            print(transaction)

    def loan(self, amount):#most two times
        if self.loan_cnt <= 2:
            self.loan_amount += amount
            self.loan_cnt += 1
        else:
            print(f'Your Loan limit exist')

    def transfer(self, amount, sender, receiver, bank):
        if amount > sender.balance:
            print("Amount exceeded then your account balance")
        else:
            sender.balance -= amount
            receiver.balance += amount
            sender.transaction.append(f"Transferred {amount} to {receiver.account_create}")
            receiver.transaction.append(f"received amount {amount} from {sender.account_create}")
            print(f"Transferred {amount} to account {receiver.account_create}. Your corrent balance is {sender.balance}")


class Bank:
    def __init__(self):
        self.accounts = []
        self.total_loan_amount = 0
        self.loan_feature_on = True

    def create_account(self, account):
        self.accounts.append(account)
        print(f"Account for {account.name} created successfully. Your account number {account.account_create}!")
    
    def delete_account(self, account_number):
        for account in self.accounts:
            if account.account_create == account_number:
                accountNO = account.account_create
            
                if accountNO:
                    self.accounts.remove(account)
                    print(f"Account {account_number} deleted successfully!")
                else:
                    print("Account not found!")
    
    def find_account(self, account_number):
        for account in self.accounts:
            if account.account_create == account_number:
                return account
        return None
    
    def list_accounts(self):
        print("All Accounts List:")
        for account in self.accounts:
            print(f"Name: {account.name}, Email: {account.email}, Account No: {account.account_create}, Balance: {account.balance + account.loan_amount}")

    def total_bank_balance(self):
        total_balance = sum(account.balance for account in self.accounts)
        print(f"Total available balance in the bank: {total_balance}")

    def loan_feature(self):
        if self.loan_feature_on == True:
            self.loan_feature_on = False
            print("Loan Feature OFF")
        else:
            self.loan_feature_on = True
            print("Loan Feature ON")

# object
brac_bank = Bank()

while True:
    print("Welcome to Banking Management System")
    print("1. User")
    print("2. Admin")
    print("3. Exit")

    choice = input("Enter your choice: ")
    if choice == '1':
        while True:
            print("User Menu")
            print("1. Create Account")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Check Balance")
            print("5. View Transaction History")
            print("6. Take Loan")
            print("7. Transfer Money")
            print("8. Exit")
            user_option = input("Enter your choice: ")

            if user_option == '1':
                name = input("Enter your name: ")
                email = input("Enter your email: ")
                address = input("Enter your address: ")
                balance = input("Enter your balance: ")
                account_type = input("Enter account type (Savings/Current): ")
                account = Account(name, email, address, int(balance), account_type)
                brac_bank.create_account(account)

            elif user_option == '2':
                account_number = int(input("Enter your account number: "))
                account = brac_bank.find_account(account_number)#find_account
                if account:
                    amount = int(input("Enter amount for deposit: "))
                    account.deposit(amount)
                else:
                    print("Account not found!")

            elif user_option == '3':
                account_number = int(input("Enter your account number: "))
                account = brac_bank.find_account(account_number)
                if account:
                    amount = int(input("Enter amount to withdraw: "))
                    account.withdrow(amount)
                else:
                    print("Account not found!")

            elif user_option == '4':
                account_number = int(input("Enter your account number: "))
                account = brac_bank.find_account(account_number)
                if account:
                    account.check_balance()
                else:
                    print("Account not found!")

            elif user_option == '5':
                account_number = int(input("Enter your account number: "))
                account = brac_bank.find_account(account_number)
                if account:
                    account.transaction_history()
                else:
                    print("Account not found!")

            elif user_option == '6':
                account_number = int(input("Enter your account number: "))
                account = brac_bank.find_account(account_number)
                if account:
                    amount = int(input("Enter loan amount: "))
                    if brac_bank.loan_feature_on:
                        account.loan(amount)
                        brac_bank.total_loan_amount += amount
                    else:
                        print("Loan feature is currently turned off")
                else:
                    print("Account not found!")

            elif user_option == '7':
                sender_account_number = int(input("Enter your account number: "))
                sender_account = brac_bank.find_account(sender_account_number)
                if sender_account:
                    recipient_account_number = int(input("Enter recipient's account number: "))
                    recipient_account = brac_bank.find_account(recipient_account_number)
                    if recipient_account:
                        amount = int(input("Enter amount to transfer: "))
                        sender_account.transfer(amount, sender_account, recipient_account, brac_bank)
                    else:
                        print("Recipient account not found!")
                else:
                    print("Account not found!")

            elif user_option == '8':
                break

            else:
                print("Invalid choice! Please try again.")

    elif choice == '2':
        while True:
            print("Admin Menu")
            print("1. Create Account")
            print("2. Delete Account")
            print("3. List Accounts")
            print("4. Check Total Bank Balance")
            print("5. Check Total Loan Amount")
            print("6. Loan Feature")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                name = input("Enter your name: ")
                email = input("Enter your email: ")
                address = input("Enter your address: ")
                balance = input("Enter your balance: ")
                account_type = input("Enter account type (Savings/Current): ")
                account = Account(name, email, address, int(balance), account_type)
                brac_bank.create_account(account)

            elif choice == '2':
                account_number = int(input("Enter account number to delete: "))
                brac_bank.delete_account(account_number)

            elif choice == '3':
                brac_bank.list_accounts()

            elif choice == '4':
                brac_bank.total_bank_balance()

            elif choice == '5':
                print(f"Total loan amount: {brac_bank.total_loan_amount}")

            elif choice == '6':
                brac_bank.loan_feature()

            elif choice == '7':
                break

            else:
                print("Invalid choice! Please try again.")

    elif choice == '3':
        print("Thank you for using the Banking Management System!")
        break

    else:
        print("Invalid Index! Please try again.")