class Student:
    Participation = 0.10
    Homework = 0.30
    Quizzes = 0.20
    FinalProject = 0.40

    def __init__(self, ID, firstName, lastName, phone, gender, birthdate, participation, homework, quizzes, FProject):
        self.ID = ID
        self.fullName = firstName + " " + lastName
        self.email = firstName + "." + lastName + "@aua.am"
        self.phone = phone
        self.gender = gender
        self.birthdate = birthdate
        self.participation = participation
        self.homework = homework
        self.quizzes = quizzes
        self.FProject = FProject


    def getPersonalInfo(self):
        print(self.ID)
        print(self.fullName)
        print(self.email)
        print(self.phone)
        print(self.gender)
        print(self.birthdate)
        print("----------------------")


    def getCurrentGrade(self):
        finalParticipation = float(self.Participation * 2 *self.participation)
        finalHomework = float(self.Homework * 3 * self.homework)
        finalQuizzes = float(self.Quizzes * 4 * self.quizzes)
        finalProject = float(self.FProject * 2 * self.FProject)
        finalGrade = float(finalParticipation + finalHomework + finalQuizzes + finalProject)
        print(finalGrade)
        print("----------------------")



def main():
    st1 = Student("AUA123", "student1", "lastname1", "123456", "M", "2/2/2002", 80, 700, 60, 50)
    st2 = Student("AUA123", "student1", "lastname2", "543210", "F", "10/10/2010", 100, 100, 83, 80)


    st1.getPersonalInfo()
    st2.getPersonalInfo()


    st1.getCurrentGrade()
    st2.getCurrentGrade()




main()
