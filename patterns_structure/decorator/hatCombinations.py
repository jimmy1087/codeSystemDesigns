from abc import ABC
# Interface
class IHat(ABC):
    def getDescription(self):
        pass
    def getPrice(self):
        pass
#########################################################
# Specific class
class StandardHat(IHat):
    def getDescription(self):
        return "Standard hat"
    def getPrice(self):
        return 100
# Specific class
class PremiumHat(IHat):
    def getDescription(self):
        return "Premium hat"
    def getPrice(self):
        return 200
#########################################################
# Decorator base class
class DecoratorHat(IHat):
    def getDescription(self):
        return super().getDescription()
    def getPrice(self):
        return super().getPrice()
# Decorator class
class RibbonedHat(DecoratorHat):
    def __init__(self, hat):
        self.hat = hat
    def getDescription(self):
        return "Ribonned " + self.hat.getDescription()
    def getPrice(self):
        return self.hat.getPrice() + 10
# Decorator class
class GoldenHat(DecoratorHat):
    def __init__(self, hat):
        self.hat = hat
    def getDescription(self):
        return "Golden " + self.hat.getDescription()
    def getPrice(self):
        return self.hat.getPrice() + 20

#########################################################

h1 = RibbonedHat(PremiumHat())
print(h1.getDescription(), h1.getPrice())  # -> 210

h1 = GoldenHat(RibbonedHat(PremiumHat()))
print(h1.getDescription(), h1.getPrice())  # -> 230

h1 = RibbonedHat(GoldenHat(StandardHat()))
print(h1.getDescription(), h1.getPrice())  # -> 130

h1 = GoldenHat(StandardHat())
print(h1.getDescription(), h1.getPrice())  # -> 120

h1 = PremiumHat()
print(h1.getDescription(), h1.getPrice())  # -> 200