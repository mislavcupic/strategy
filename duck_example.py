class Fly:
    def fly(self):
        pass

class CanFly(Fly):
    def fly(self):
        return "This duck can fly"

class CannotFly(Fly):
    def fly(self):
        return "Cannot fly"

class OnlyWithWingsFly(Fly):
    def fly(self):
        return "Can fly only with handmade wings"

class Duck:
    def __init__(self, name, fly: Fly):
        self.name = name
        self.fly = fly

    def __str__(self):
        return f"name: {self.name}, status flying: {self.fly.fly()}"

    def perform_fly(self):
        return self.fly.fly()

class RubberDuck(Duck):
    def perform_fly(self):
        return self.fly.fly()

class FlyingDuck(Duck):
    def perform_fly(self):
        return self.fly.fly()

if __name__ == "__main__":
    # Pass an instance of the strategy class, not the class itself
    rubber = RubberDuck("Rubber", fly=CannotFly())
    flyingDuck = FlyingDuck("FlyingDuck",fly=CanFly())
    print(rubber.perform_fly())
    print(rubber)  # Calls __str__()
    print(flyingDuck.perform_fly())
    print(flyingDuck)
