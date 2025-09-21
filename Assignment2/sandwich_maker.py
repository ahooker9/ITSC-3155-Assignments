
class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        #####
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry insufficient {item}.")
                return False
        return True
        #if it takes more ingredients to order than we have, it will return false
        #otherwise it returns true

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"{sandwich_size} sandwich is ready!")
