"""Tree traversal have three stages: inorderTraversal, PreorderTraversal, PostorderTraversal."""

class Tree: # tree class
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def add(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.add(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.add(data)
        else:
            self.data = data


    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

# inorder traversal work from left subtree then take root and last right subtree
# define inorderTraversal function
    def inorderTraversal(self,root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

# preorder traversal root first left subtree second and finally right subtree
# define PreorderTraversal function
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

# post-order traversal first left subtree, second right subtree and finally root
# define PostorderTraversal

    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

"""Simply inorder traversal is print order like from smallest to biggest. Preorder traversal takes root first
when starts from left subtree - 14,10,19 and finally right subtree - 35, 31, 42. Postorder traversal takes left
subtree first - 10,19,14, right subtree - 31,42,35 and finally root - 27"""
# root for class variable
root = Tree(27) # root
root.add(14) # left subtree
root.add(35) # right subtree
root.add(10) # left subtree
root.add(19) # left subtree
root.add(31) # right subtree
root.add(42) # right subtree
print(root.inorderTraversal(root)) # printing inorderTraversal
print(root.PreorderTraversal(root)) # printing preorderTraversal
print(root.PostorderTraversal(root)) # printing postorderTraversal
