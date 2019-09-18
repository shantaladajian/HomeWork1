class Room:
    
    rooms = []
    
    def __init__(self, type, roomID, capacity):
        self.type = type
        self.roomID = roomID
        self.capacity = capacity
        Room.rooms.append(self)
        print(Room.rooms)
    
    @classmethod
    def getRooms(cls):
        for room in cls.rooms:
            room.print()

    @classmethod
        def getRoomsByType(cls, type):
            for room in cls.rooms:
                if room.type == type:
                    print(room)

    @classmethod
        def getRoomById(cls, ID):
            if ID in cls.rooms.keys():
                return cls.rooms[ID]
            print("the room cannot be found")
            return False

class ClassRoom(Room):
    type = "ClassRoom"
    def __init__(self, roomID, capacity):
        super().__init__(ClassRoom.type, roomID, capacity)
        self.schedule = []
    
    def isFree(self, start, end):
        is_free = True
        for slot in self.schedule:
            if end < slot["start"] or start > slot["end"]:
                pass
            else:
                is_free = False
                break
        return is_free
    
    def Reserve(self, start, end):
        if self.isFree(start, end):
            timeslot = {"start": start, "end": end}
            self.schedule.append(timeslot)
            return True
        else:
            return False

    @classmethod
    def getscheduleofAllClsRooms(cls):
        for key in cls.rooms:
            currRoom = cls.rooms[key]
            print(currRoom.roomID, ' :')
            print("capacity: ", currRoom.capacity)
            print("schedule: ", currRoom.schedule)


@staticmethod
    def isValidSlot(start, end):
        return start < end
class Office(Room):
    type = "Office"
    def __init__(self, roomID, capacity):
        super().__init__(Office.type, roomID, capacity)
        self.faculty = []
    
    def facultyMembers(self):
        while True:
            name = input("please input faculty member name in the selected class:")
            if name not in Room.getRoomsByType("Office"):
                self.faculty.append(name)
            else:
                print("The member is already in the list")

def main():
    ClassRoom("208MB", 50)
    ClassRoom("300W PAB", 100)
    
    Office("114E PAB", 3)
    Office("110E PAB", 4)
    Office("001E PAB", 1)
    
    print("dear user, here you can reserve an office or a classroom. Available IDs are:\n",
          "IDs for classrooms:",
          Room.getRoomsByType("ClassRoom"), "IDs for Offices: ", Room.getRoomsByType("Office"))
    while True:
        IDchoice = input("Dear user please choose an ID from above.")
        currRoom = Room.getRoomById(IDchoice)
          
        if IDchoice == Room.getRoomsByType("Classroom"):
            start = int(input("input the start time: "))
            end = int(input("input the end time: "))
              
        if (Room.isValidSlot(start, end)):
            if currRoom.isFree(start, end) == False:
                print("Not available for ", IDchoice.roomID)
            else:
                currRoom.Reserve(start, end)
                print("You just reserved the classroom", IDchoice.roomID, " from ", start, " to ", end)
                print(IDchoice.schedule)
        elif IDchoice == Room.getRoomsByType("Office"):
            print(Office.facultyMembers())
        else:
            print("error. please try again.")
                                          
    else:
      print("The slot is invalid")

main()
