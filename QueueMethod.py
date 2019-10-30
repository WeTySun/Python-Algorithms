class fruitservice:
    def __init__(self):
        self.shelf = list()

    def addfruit(self, fruit):
# Insert method to add element
        if fruit not in self.shelf:
            self.shelf.insert(0,fruit)
            return True
        return False

# Pop method to remove element
    def removefromshelf(self):
        if len(self.shelf) > 0:
            return self.shelf.pop()
        return ("No fruits in shelf!")

    def size(self):
        return len(self.shelf)


fruits = fruitservice()
fruits.addfruit("Mango")
fruits.addfruit("Apple")
fruits.addfruit("Orange")
print(fruits.size())
print(fruits.removefromshelf())
print(fruits.removefromshelf())
