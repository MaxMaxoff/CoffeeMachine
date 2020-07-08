class CoffeeMachine():
    # region CONST
    # can be moved to config file
    _ESPRESSO = {
        "water": -250, 
        "milk": 0, 
        "coffee": -16, 
        "disposable_cups": -1, 
        "money": 4
    }
    _LATTE = {
        "water": -350, 
        "milk": -75, 
        "coffee": -20, 
        "disposable_cups": -1, 
        "money": 7
    }
    _CAPPUCCINO = {
        "water": -200, 
        "milk": -100, 
        "coffee": -12, 
        "disposable_cups": -1, 
        "money": 6
    }
    # endregion
    
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.disposable_cups = 9
        self.money = 550
        # region SWITCHER
        # can be moved to config files
        self._SWITCHER_BUY = {
            "1": self._ESPRESSO,
            "2": self._LATTE,
            "3": self._CAPPUCCINO,
            "back": None
        }
        self._SWITCHER = {
            "buy": self.buy,
            "fill": self.fill,
            "take": self.take,
            "remaining": self.status,
            "exit": self.stop_going,
        }
        # endregion
        self.keep_going = True
        self.action()

    def stop_going(self):
        self.keep_going = False

    def status(self):
        print(f'The coffee machine has:')
        print(f'{self.water} of water')
        print(f'{self.milk} of milk')
        print(f'{self.coffee} of coffee beans')
        print(f'{self.disposable_cups} of disposable cups')
        print(f'{self.money} of money')

    def action(self):
        while self.keep_going:
            print('Write action (buy, fill, take, remaining, exit):')
            action = input()
            if action in self._SWITCHER.keys():
                self._SWITCHER.get(action)()
    
    def buy(self):
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        action = input()
        if action in self._SWITCHER_BUY.keys() and self.is_enough_resources(self._SWITCHER_BUY.get(action)):
            self.change_resources(self._SWITCHER_BUY.get(action))
    
    def is_enough_resources(self, resources):
        if self.water + resources["water"] < 0:
            print('Sorry, not enough water!')
            return False
        if self.milk + resources["milk"] < 0:
            print('Sorry, not enough milk!')
            return False
        if self.coffee + resources["coffee"] < 0:
            print('Sorry, not enough coffee!')
            return False
        if self.disposable_cups + resources["disposable_cups"] < 0:
            print('Sorry, not enough disposable_cups!')
            return False
        print('I have enough resources, making you a coffee!')
        return True

    def change_resources(self, resources):
        if resources.get("water"):
            self.water += resources["water"]
        if resources.get("milk"):
            self.milk += resources["milk"]
        if resources.get("coffee"):
            self.coffee += resources["coffee"]
        if resources.get("disposable_cups"):
            self.disposable_cups += resources["disposable_cups"]
        if resources.get("money"):
            self.money += resources["money"]

    def fill(self):
        print('Write how many ml of water do you want to add:')
        self.change_resources({"water": int(input())})
        print('Write how many ml of milk do you want to add:')
        self.change_resources({"milk": int(input())})
        print('Write how many grams of coffee beans do you want to add:')
        self.change_resources({"coffee": int(input())})
        print('Write how many disposable cups of coffee do you want to add:')
        self.change_resources({"disposable_cups": int(input())})


    def take(self):
        print('I gave you', self.money)
        self.change_resources({"money": -self.money})


coffee_machine = CoffeeMachine()
