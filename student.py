class Node:
    def __init__(self,name=None ):
        self.name=name
        self.right=None
        self.left = None

class student:
    def __init__(self):
        self.student=None

    def __str__(self):
        if self.student == None:
            print("Root is Empty")
        else:
            return str(self.student.name)

    def addName(self,sname):
        self.student=Node(sname)

    def addCourse(self,cname):
        if self.student.left==None:
            self.student.left=Node(cname)
            return cname
        if self.student.right == None:
            self.student.right = Node(cname)

    def addAssignment(self,course,aname):
        course1=self.student.left
        course2=self.student.right
        if course==course1.name and course1.left==None:
            course1.left=Node(aname)
            return aname
        if course==course1.name and course1.right==None:
            course1.right=Node(aname)
            return aname
        if course==course2.name and course2.left==None:
            course2.left=Node(aname)
            return aname
        if course==course1.name and course2.right==None:
            course2.right=Node(aname)
            return aname

    def addGrade(self,assignment,grade):
        course1 = self.student.left
        course2 = self.student.right
        assignment11=course1.left
        assignment12=course1.right
        assignment21 = course2.left
        assignment22 = course2.right
        if assignment==assignment11:
            assignment11.left=grade
        if assignment==assignment12:
            assignment12.left=grade
        if assignment==assignment21:
            assignment21.left=grade
        if assignment==assignment22:
            assignment22.left=grade

    def printStudentinfo(self,name):
        if name != None:
            print(name.name, end=" ")
            self.printStudentinfo(name.right)
            self.printStudentinfo(name.left)
def main():
    student1=student()
    student1.addName("Shantal")
    student1.addCourse("ENGS103")
    student1.addCourse("ENGS123")
    student1.addAssignment("ENGS103","Spanning Sets")
    student1.addAssignment("ENGS103","Transformation")
    student1.addAssignment("ENGS123", "Capacitors and Dielectrics")
    student1.addGrade("Spanning Sets",100)
    student1.addGrade("Transformation",90)
    student1.addGrade("Capacitors and Dielectrics",70)
    student1.printStudentinfo(student1.student)
main()