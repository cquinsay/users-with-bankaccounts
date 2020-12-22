class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance = 0
    def make_deposit(self):
        self.account.deposit(100)
        print(self.account.balance)
    def make_withdrawal(self):
        self.account.withdraw(100)
        print(self.account.balance)
    def display_user_balance(self):
        print(f'User:{self.name}, Balance: ${self.balance}')
    def transfer_money(self, other_user, amount):
        other_user.make_deposit(amount)
        self.make_withdrawal(amount)

tommy = User('Tommy', 'tommy@tommy.com')
chuckie = User('Chuckie', 'chuckie@chuckie.com')
angelica = User('Angelica', 'angelica@angelica.com')

tommy.make_deposit(100)
tommy.make_deposit(200)
tommy.make_deposit(300)
tommy.make_withdrawal(150)
tommy.display_user_balance()
    
chuckie.make_deposit(500)
chuckie.make_deposit(200)
chuckie.make_withdrawal(50)
chuckie.make_withdrawal(100)
chuckie.display_user_balance()

angelica.make_deposit(1000)
angelica.make_withdrawal(25)
angelica.make_withdrawal(25)
angelica.make_withdrawal(50)
angelica.display_user_balance()

tommy.transfer_money(chuckie, 100)
tommy.display_user_balance()
chuckie.display_user_balance()

