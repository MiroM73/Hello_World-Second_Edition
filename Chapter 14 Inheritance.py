class GameObject:
    def __init__(self, name):
        self.name = name

    def pickUp(self, player):
        # add pass keyword, if you don't define method, you only put comments in
        # pass keyword is used as a placeholder when you want to make a code stub
        # In the last example, we didn't put any real code in the methods,
        # just some comments explaining what the methods would do.
        # It's a way of planning or thinking ahead for what you'll add later.
        # The actual code would depend on how the game worked. Programmers
        # often do this as a way to organize their thoughts when they're writing
        # more complex code. The "empty" functions or methods are called code stubs.
        pass
        # put code here to add the object
        # to the player's collection

# Coin is a subclass of GameObject, as a subclass can inherit properties or methods
class Coin(GameObject):
    def __init__(self, value):
        # In __init__(), inherit GameObject's init and add stuff to it
        GameObject.__init__(self, "coin")
        self.value = value

    # A new spend() method for the Coin class
    def spend(self, buyer, seller):
        pass
        # put code here to remove the coin
        # from the buyer's money and
        # add it to the seller's money

myCoin = Coin(10)
print myCoin.name
print myCoin.value