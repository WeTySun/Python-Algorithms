class Shelf:
    def __init__(self):
        self.shelf = []

    def add(self, book):
        if book not in self.shelf:
            self.shelf.append(book)
            return True
        else:
            False

    def peek(self):
        return self.shelf[-1]

    def remove(self):
        if len(self.shelf) <= 0:
            return ("No book in shelf!")
        else:
            return self.shelf.pop()

shelf = Shelf()
shelf.add("The call of the wild")
shelf.add("A midsummer night's dream")
shelf.add("Civil disobedience")
shelf.add("Songs for the open road")
print(shelf.remove())
print(shelf.remove())
