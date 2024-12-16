# Binary Tree Impl
class binary_Tree():
    def __init__(self,key):
        self.left=None
        self.right=None
        self.val = key
    def preorder(self):
        print(self.val,end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()
    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.val,end=" ")
        if self.right:
            self.right.inorder()
    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.val,end=" ")
        
root=binary_Tree(1)
root.left=binary_Tree(2)
root.right=binary_Tree(3)
root.left.left=binary_Tree(4)
root.left.right=binary_Tree(5)
root.right.left=binary_Tree(6)
root.right.right=binary_Tree(7)

root.preorder()
print()
root.inorder()
print()
root.postorder()