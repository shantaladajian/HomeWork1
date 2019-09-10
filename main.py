class Classroom:
    priviousClass=0
    def __init__(self, startHour, endHour):
        self.schedule=[]
        self.startHour = startHour
        self.endHour = endHour
    
    def isFree(self, startHour, endHour):
        newStart=int(self.startHour)
        newEnd=int(self.endHour)
        for n in range(3):
            priviousClass=str(Classroom.priviousClass+1)
            oldClass= 'class'+'_'+priviousClass
            oldStart=int(oldClass.startHour)
            oldEnd=int(oldClass.endHour)
            if oldStart[0]==0 or oldEnd[0]==0:
                oldStart=int(oldStart[1:])
                oldEnd =int(oldEnd[1:])
                if (oldStart<newStart and oldEnd<newEnd) or (oldStart>newStart and oldEnd>newEnd):
                    return True
                else:
                    return False
            else:
                if (oldStart<newStart and oldEnd<newEnd) or (oldStart>newStart and oldEnd>newEnd):
                    return True
                else:
                    return False

def reserve(self, startHour, endHour):
    if self.isFree(startHour, endHour)==True:
        timeslot={'start' : startHour,'end':endHour }
            self.schedule.append(timeslot)
            return True
        else:
            return False

class_1 = Classroom(1010, 1120)
class_2 = Classroom(1400, 1500)
class_3 = Classroom(1200, 1320)

def main():
    while True:
        startHour=input("Please enter the start Time of your class in the form of NNNN instead of NN:NN")
        endHour=input("Please enter the end Time of your class in the form of NNNN instead of NN:NN")
        if startHour[0] == 0 or endHour[0] == 0:
            startHour = startHour[1:]
            endHour = endHour[1:]
        class_4 = Classroom(startHour,endHour)
        if startHour.isnumeric():
            break
        else:
            print("Please try again in the form mentioned above.")
    if class_4.reserve(startHour, endHour)==False:
        print("Sorry the class is occupied during that time :)")
    else:
        print(class_4.schedule)
        classroomSchedule = {'class_1': '1010-1120', 'class_2': '1400-1500', 'class_3': '1200-1320'}
        classroomSchedule['class_4'] = startHour+'-'+endHour
        print(classroomSchedule)

main()
