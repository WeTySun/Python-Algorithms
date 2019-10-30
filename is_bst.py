class Node:
    rChild,lChild,data = None,None,None

    def __init__(self,key):
        self.rChild = None
        self.lChild = None
        self.data = key

class Tree:
    root,size = None,0
    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self,node,someNumber):
        if node is None:
            node = Node(someNumber)
        else:
            if node.data > someNumber:
                self.insert(node.rchild,someNumber)
            else:
                self.insert(node.rchild, someNumber)
        return

def main():
    t = Tree()
    t.root = Node(4)
    t.root.rchild = Node(5)
    print t.root.data #this works
    print t.root.rchild.data #this works too
    t = Tree()
    t.insert(t.root,4)
    t.insert(t.root,5)
    print t.root.data #this fails
    print t.root.rchild.data #this fails too

if __name__ == '__main__':
     main()
