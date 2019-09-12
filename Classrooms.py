class Classroom:
    classroomIDs = []
    
    def __init__(self, capacity, roomID):
        self.schedule = []
        self.roomID = roomID
        self.capacity = capacity
        Classroom.classroomIDs.append(roomID)
    
    def isFree(self, start, end):
        is_free = True
        for slot in self.schedule:
            if end < slot["start"] or start > slot["end"]:
                pass
            else:
                is_free = False
                break
        return is_free
    
    def reserve(self, start, end):
        if self.isFree(start,end)==True:
            timeslot={"start":start,"end":end}
            self.schedule.append(timeslot)
            return True
        else:
            return False

    @classmethod
        def getAvailableRooms(cls):
            return str.join(",", cls.classroomIDs)
    
    
    @staticmethod
    def isValidSlot(start, end):
        return start < end


def room_IDs(classroom1):
    while True:
        start = input("Please insert the starting time in the form of NNNN instead of NN:NN = ")
        end = input("Please insert the starting time in the form of NNNN instead of NN:NN = ")
        if Classroom.isValidSlot(start, end):
            if start[0] == 0 or end[0] == 0:
                start = int(start[1:])
                end = int(end[1:])
            else:
                start = int(start)
                end = int(end)
            if classroom1.isFree(start, end) == True:
                classroom1.reserve(start, end)
                print("You just reserved the classroom", classroom1.roomID, " from ", start, " to ", end)
                print(classroom1.schedule)
            if classroom1.isFree(start, end) == False:
                print("Not available for", classroom1.roomID)
        else:
            print("The slot is invalid.")
        continueornot = input("do you want to continue?answer in yes or no")
        if continueornot == "no":
            print("see you next time:)")
            break
def main():
    classroom1 = Classroom(60, "208E PAB")
    classroom2 = Classroom(30, "314W PAB")
    classroom3 = Classroom(40, "114 PAB")
    print("Hello, here you can reserve a classroom. Available IDs are:", Classroom.getAvailableRooms())
    while True:
        roomID = input("Please input the room ID you want to reserve: ")
        if roomID == classroom1.roomID:
            room_IDs(classroom1)
            break
        if roomID == classroom2.roomID:
            room_IDs(classroom2)
            break
        if roomID == classroom3.roomID:
            room_IDs(classroom2)
            break
        else:
            print("This ID isn't within our room IDs, please try again")

main()
