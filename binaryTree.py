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
        if data < node.data:
            if node.left==None:
                node.left=Node(data)
            else:
                self._addNode(data,node.left)
        elif data > node.data:
            if node.right==None:
                node.right=Node(data)
            else:
                self._addNode(data,node.right)
        else:
            print("value already in tree")

    def traverse_inOrder(self, node):
        if node != None:
            self.traverse_inOrder(node.left)
            print(node.data, end=" ")
            self.traverse_inOrder(node.right)

    def traverse_preOrder(self,node):
        if node!=None:
            print(node.data, end=" ")
            self.traverse_preOrder(node.left)
            self.traverse_preOrder(node.right)

    def traverse_postOrder(self,node):
        if node!=None:
            self.traverse_postOrder(node.left)
            self.traverse_postOrder(node.right)
            print(node.data, end=" ")

    def printTree(self):
        if self.root!=None:
            self._printTree(self.root)

    def _printTree(self,node):
        if node!=None:
            self._printTree(node.left)
            print (str(node.data))
            self._printTree(node.right)

    def numberOfNodes(self,node, count=0):
        count = 1
        if self.root==None:
            return -1
        if self.root != None:
            if node.left != None:
                count += self.numberOfNodes(node.left)
            if node.right != None:
                count += self.numberOfNodes(node.right)
        return count

    def height(self):
        if self.root !=None:
            return self._height(self.root,0)
        else:
            return 0

    def _height(self,node,cur_height):
        if node==None:
            return cur_height
        left_height=self._height(node.left ,cur_height + 1)
        right_height = self._height(node.right, cur_height + 1)
        return max(left_height,right_height)

def fillTree(tree,elem=10,maxint=1000):
    from random import randint
    for int in range(elem):
        currElem=randint(0,maxint)
        tree.addNode(currElem)

def main():
    tree=BST()
    fillTree(tree)
    #tree.printTree()
    tree.traverse_inOrder(tree.root)
    print("\n")
    tree.traverse_preOrder(tree.root)
    print("\n")
    tree.traverse_postOrder(tree.root)
    print("\n \ntree height: ", str(tree.height()))
    print("Number of Nodes in the tree is : ", tree.numberOfNodes(tree.root))
main()

