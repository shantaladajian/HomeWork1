class Classroom:
    def __init__(self):
        self.schedule = []
    
    def isFree(self, start, end, roomID):
        is_free = True
        for slot in self.schedule:
            if end < slot[roomID]["start"] or start > slot[roomID]["end"]:
                pass
            else:
                is_free = False
                break
        return is_free
    
    def reserve(self, start, end, roomID):
        if self.isFree(start, end, roomID) == True:
            timeslot = {roomID: {"start": start, "end": end}}
            self.schedule.append(timeslot)
            return True
        else:
            return False
    @staticmethod
    def isValidSlot(start, end):
        return start < end


def main():
    classroom = Classroom()
    print("Hello, here you can reserve a classroom. Available IDs are: 114 PAB , 208E PAB, 314PAB")
    while True:
        roomID = input("Please input the room ID you want to reserve : ")
        start = input("Please insert the starting time in the form of NNNN instead of NN:NN = ")
        end = input("Please insert the starting time in the form of NNNN instead of NN:NN = ")
        if Classroom.isValidSlot(start, end):
            if start[0] == 0 or end[0] == 0:
                start = int(start[1:])
                end = int(end[1:])
            else:
                start = int(start)
                end = int(end)
            if classroom.isFree(start, end, roomID) == False:
                print("Not available for", roomID)
            else:
                print(classroom.schedule)
                classroom.reserve(start, end, roomID)
                print("You just reserved the classroom", roomID, " from ", start, " to ", end)
                print(classroom.schedule)
        else:
            print("The slot is invalid.")
        answer=input("do you want to continue?answer in yes or no")
        if answer=='no':
            break
main()
