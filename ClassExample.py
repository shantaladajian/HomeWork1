def Length():
    print("Dear user, you're going to choose the length of a list, and then input the numbers\nyou want to include in it. After which the program will\ngive you the list with the numbers added with thei previous one.")
    while True:
        Length=input("\nPlease input the length of your list in an integer form: ")
        if Length.isnumeric():
           break
        else:
            print("\n please try again. Answer in the form of the integers mentioned above.")
    return int(Length)


def List(Length):
    n = 0
    list = []
    for i in range(Length):
        while True:
            number = input("Please input a number to your list in an integer form")
            if number.isnumeric():
                break
            else:
                print("\n please try again. Answer in the form of the integers mentioned above.")
        number=int(number)
        number=number+n
        n=number
        list.append(number)
    print("List:", list)

def main():
    L=Length()
    List(L)
main()