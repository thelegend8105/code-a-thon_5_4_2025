class Transaction:
    def __init__(self, amount, description):
        self.amount = amount
        self.description = description

    def __repr__(self):
        return f"Debit of ${self.amount}: {self.description}"


class User:
    
    def __init__(self, username):
        self.username = username
        self.transactions = []
        self.balance=20000

    def add_transaction(self, amount,  description):
        transaction = Transaction(amount, description)
        self.balance-=amount
        self.transactions.append(transaction)
        

    def show_transactions(self):
        print(f"Transactions for {self.username}:")
        for transaction in self.transactions:
            print(transaction)
        print("Balance :" ,self.balance)



if __name__ == "__main__":
    
    test_user = User("Kavya")

    # Add some transactions
    
    test_user.add_transaction(50, 'Purchase of goods')
    test_user.add_transaction(25, 'Purchase of services')

    # Show all transactions for the test user
    test_user.show_transactions()
