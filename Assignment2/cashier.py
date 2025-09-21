class Cashier:

    def __init__(self):
        pass

    def process_coins(self):
        print("Please insert coins.")
        dollars = int(input("how many large dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))
        total = dollars * 1.0 + half_dollars * 0.5 + quarters * 0.25 + nickels * 0.05
        return total

    def transaction_result(self, payment, cost):
        if payment < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        change = round(payment - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        return True

