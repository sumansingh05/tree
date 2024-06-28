class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        self.count = -1

    def buildTree(self,nodes):
        self.count += 1
        if nodes[self.count] == -1:
            return None
        newNode = Node(nodes[self.count])
        newNode.left = self.buildTree(nodes)
        newNode.right = self.buildTree(nodes)

        return newNode
    
    def preorder(self,root):
        if root is None:
            return
        print(root.data,end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    def inorder(self,root):
        if root is None:
            return
        self.inorder(root.left)
        print(root.data,end=" ")
        self.inorder(root.right)
        

    def postorder(self,root):
        if root is None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end=" ")

nodes = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
tree = BinaryTree()
root = tree.buildTree(nodes)
print("Root of Tree is ",root.data)

print("Preorder Traversal:", end=" ")
tree.preorder(root)
print()
print("Inorder Traversal:", end=" ")
tree.inorder(root)
print()

print("Postorder Traversal:", end=" ")
tree.postorder(root)
print()



