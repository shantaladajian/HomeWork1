import datetime
class BST():
    def __init__(self):
        self.root= None

    def add(self,title, deadline, percent):
        if self.root==None:
            self.root=Assignment(title, deadline, percent)
        else:
            self._addAssignment(title, deadline, percent,self.root)

    def _addAssignment(self,title, deadline, percent, assignment):
        if self.root.deadline > assignment.deadline:
            if assignment.left == None:
                assignment.left = Assignment(title, deadline, percent)
            else:
                self._addAssignment(title, deadline, percent, Assignment.left)
        elif self.root.deadline < assignment.deadline:
            if assignment.right == None:
                assignment.right = Assignment(title, deadline, percent)
            else:
                self._addAssignment(title, deadline, percent, Assignment.right)
        else:
            print("value already in tree")

    def traverse_inOrder(self, assignment,title):
        if assignment != None:
            if assignment.title!=title:
                self.traverse_inOrder(assignment.left)
                self.traverse_inOrder(assignment.right)
            else:
                return assignment

    def find(self, title):
        if self.root.title==title:
            return self.root
        else:
            self.traverse_inOrder(self.root)


class LinkedList:
    def __init__(self):
        self.__head=None

    def add(self,node):
        tmp= self.__head
        if tmp == None:
            self.__head=node
        else:
            while tmp.next!=None:
                tmp=tmp.next

            tmp.next=node

    def getHead(self):
        return self.__head

    def find(self,data):
        tmp= self.__head
        while (tmp!=None):
            if tmp.isEqual(data):
                return tmp
            tmp=tmp.next
        return None

class Assignment:
    def __init__(self, title, deadline, percent):
        self.title = title
        self.deadline =self.to_integer(deadline)
        self.percent = percent
        self.grade = 0
        self.left=None
        self.right=None

    def to_integer(self,dt_time):
        return 10000 * dt_time.year + 100 * dt_time.month + dt_time.day

    def __str__(self):
        return self.title + ": " + self.deadline + ": " + str(self.percent) + ": " + str(self.grade)

    def addGrade(self, grade):
        self.grade = grade

    def getActualGrade(self):
        return self.grade

    def getCalculatedGrade(self):
        return self.grade * self.percent/100

    def isEqual(self,title):
        return self.title==title

class Course:
    def __init__(self, ID):
        self.ID = ID
        self.assignments = BST()
        self.next=None

    def __str__(self):
        return self.ID

    def addAssignment(self, title, deadline, percent):
        assignment = Assignment(title, deadline, percent)
        self.assignments.add(assignment)

    def getAssignment(self,title):
        return self.assignments.find(title)

    def addGrade(self, title, grade):
        assignment = self.getAssignment(title)
        if (assignment != None):
            assignment.addGrade(grade)
        else:
            print("The Assignment", title, "doesn't exist for the student")

    def getGrade(self):
        grade = 0
        tmp=self.assignments.root()
        while tmp !=None:
            grade = grade + tmp.getCalculatedGrade()
            tmp=tmp.next
        return grade

    def isEqual(self,ID):
        return self.ID==ID

class Student:
    def __init__(self, fName, lName, ID):
        self.fName = fName
        self.lName = lName
        self.ID = ID
        self.courses = LinkedList()

    def __str__(self):
        return self.getFullName() + ": " + self.ID

    def getCourse(self, ID):
        return self.courses.find(ID)

    def getFullName(self):
        return self.fName + " " + self.lName

    def addCourse(self, ID):
        course = Course(ID)
        self.courses.add(course)

    def addAssignment(self, cID, title, deadline, percent):
        course = self.getCourse(cID)
        if (course != None):
            course.addAssignment(title, deadline, percent)
        else:
            print("The Course", cID, "doesn't exist for the student")

    def getAssignment(self, cID, title):
        course = self.getCourse(cID)
        return course.getAssignment(title)

    def addGrade(self, cID, title, grade):
        course = self.getCourse(cID)
        if (course != None):
            course.addGrade(title, grade)
        else:
            print("The Course", cID, "doesn't exist for the student")

    def getCourseGrade(self, cID):
        course = self.getCourse(cID)
        return course.getGrade()

    def getAssignmentGrade(self,cID,atitle):
        assignment=self.getAssignment(cID,atitle)
        return assignment.grade

    # def getAssignmentCalculatedGrade(self,cID,atitle):
    #     assignment = self.getAssignment(cID, atitle)
    #     calculatedgrade=assignment.grade*assignment.percent
    #     return calculatedgrade

    def getFinalGrade(self):
        grade=0
        tmp=self.courses.getHead()
        while tmp!=None:
            grade=grade+self.getCourseGrade(tmp.ID)
            tmp=tmp.next
        return grade

def main():
    my_student = Student("Arthur", "Sargsyan", "AUA234")
    print(my_student)

    #Adding Ccourses
    my_student.addCourse("ENGS115")
    my_student.addCourse("ENGS103")
    print(my_student.getCourse("ENGS115"))
    print(my_student.getCourse("ENGS103"))

    #Adding Assignments
    my_student.addAssignment("ENGS115", "Implement Browser History using Stack", "2019-10-31", 30)
    my_student.addAssignment("ENGS103", "Transformation", "2019-10-31", 70)
    print(my_student.getAssignment("ENGS115", "Implement Browser History using Stack"))

    #Adding Assignments
    my_student.addAssignment("ENGS115", "Implement Browser History using Queue", "2019-11-13", 40)
    print(my_student.getAssignment("ENGS115", "Implement Browser History using Queue"))

    #adding Grades
    my_student.addGrade("ENGS115", "Implement Browser History using Stack", 90)
    my_student.addGrade("ENGS115", "Implement Browser History using Queue", 50)
    my_student.addGrade("ENGS103", "Transformation", 90)
    print(my_student.getAssignment("ENGS115", "Implement Browser History using Stack"))
    print(my_student.getAssignment("ENGS115", "Implement Browser History using Queue"))

    print(my_student.getCourseGrade("ENGS115"))
    print(my_student.getAssignmentGrade("ENGS115", "Implement Browser History using Stack"))
    # print(my_student.getAssignmentCalculatedGrade("ENGS115", "Implement Browser History using Stack"))

    #FinalGrade
    print("Final Grade for ",my_student.getFullName(), "is : " ,my_student.getFinalGrade())
main()
