class BH:

    def __init__(self, URL = None):
        self.URL = URL
        self.next = None

class Stack:
    def __init__(self):
        self.__head = None

    def isEmpty(self):
        if self.__head == None:
            return True
        else:
            return False

    def push(self, newURL):
        if self.__head == None:
            self.__head = BH(newURL)
        else:
            newData = BH(newURL)
            newData.next = self.__head
            self.__head = newData

    def back(self):
        if self.isEmpty():
            return None
        else:
            poppedData = self.__head
            self.__head = self.__head.next
            global frw
            frw = poppedData
            poppedData.next = None
            return poppedData.URL

    def open(self):
        if self.isEmpty():
            return None
        else:
            return self.__head.URL

    def display(self):
        printval = self.__head
        if self.isEmpty():
            print("Stack is empty")
        else:
            while printval is not None:
                print(printval.URL)
                printval = printval.next

    def forward(self):
        temp = self.__head
        if temp.next is not None:
            return frw.URL)
        else:
            print("No Data")

def main():
    BH = Stack()
    BH.push("im.aua.am")
    BH.push("menu.am")
    BH.push("youtube.com")
    print("\n The initial list is:")
    BH.display()
    print("\n Top element is:", BH.open())
    print("\n one step back")
    BH.back()
    print("\n Displaying the list:")
    BH.display()
    print("\n the Top element is:", BH.open())
    BH.forward()
    print("\n one step forward,the top element is: ", BH.open())
    BH.back()
    print("\n going one step back. Top element: ", BH.open())
    print("\n Displaying what we have in our list: " )
    BH.display()
    print("\n Top element is", BH.open())


main()