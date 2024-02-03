class Money:
    def __init__(self,current_money):
        self.current_money = current_money
    
    def get_money(self):
        return self.current_money
    
    def set_money(self,film,price):
        if self.current_money > int(price):
            self.current_money = self.current_money - int(price)
            return f"You bought the movie '{film}' and your balance is less than '{ self.current_money} AZN'. Enjoy the film"
        else:
            return "You don't have enough balance"  