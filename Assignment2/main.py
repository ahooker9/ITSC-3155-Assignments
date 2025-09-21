
import data
import cashier
import sandwich_maker

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
cashier_instance = cashier.Cashier




def main():
    status = True
    while status:
        request = input("What would you like? (small/ medium/ large/ off/ report): ")

        if request == "off":
            status = False

        elif request == "report":
            print(f"Bread: {resources['bread']} slice(s)")
            print(f"Ham: {resources['ham']} slice(s)")
            print(f"Cheese: {resources['cheese']} ounce(s)")

        elif request in recipes:
            sandwich = recipes[request]
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                payment = cashier_instance.process_coins

                if cashier_instance.transaction_result(payment, sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(request, sandwich["ingredients"])

        else:
            print("Invalid input. Please choose small, medium, large, report, or off.")

if __name__=="__main__":
    main()
