class Node:
    def __init__(self,data=None ):
        self.data=data
        self.right=None
        self.left = None

class BST:
    def __init__(self):
        self.root= None

    def __str__(self):
        if self.root == None:
            print("Root is Empty")
        else:
            return str(self.root.data)

    def addNode(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            self._addNode(data,self.root)

    def _addNode(self,data,node):
        if data<node.data:
            if node.left==None:
                node.left=Node(data)
            else:
                self._addNode(data,node.left)
        elif data>node.data:
            if node.right==None:
                node.right=Node(data)
            else:
                self._addNode(data,node.right)
        else:
            print("value already in tree")

    def printTree(self):
        if self.root!=None:
            self._printTree(self.root)

    def _printTree(self,node):
        if node!=None:
            self._printTree(node.left)
            print (str(node.data))
            self._printTree(node.right)

    def height(self):
        if self.root !=None:
            return self._height(self.root,0)
        else:
            return 0

    def _height(self,node,cur_height):
        if node==None: return cur_height
        left_height=self.height(node.left ,cur_height + 1)
        right_height = self.height(node.right, cur_height + 1)
        return max(left_height,right_height)

def fillTree(tree,elem=100,maxint=1000):
    from random import randint
    for int in range(elem):
        currElem=randint(0,maxint)
        tree.addNode(currElem)

tree=BST()
tree=fillTree(tree)
tree.printTree()
print("tree height: ", str(tree.height()))

