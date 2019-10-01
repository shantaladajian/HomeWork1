
class Task:
    def __init__(self, task, date, levelofimportance):
        self.task=task
        self.date=date
        self.levelofimportance=levelofimportance
        self.Importance = {}
    def returnTask(self):
        return self.task
    def importance(self):
        h={self.task : self.levelofimportance}
        self.Importance.update(h)

class TaskManager():
    def __init__(self):
        self.Tasks=[]

    def addTask(self,t):
        self.t=t
        task=self.t.returnTask()
        self.Tasks.append(task)

    def printAllTasks(self):
        print("All Tasks : ")
        print(*self.Tasks,sep = ", ")

    def printTheMostImportantTask(self):
        important=self.t.Importance
        itemMaxValue = max(important.items(), key=lambda x : x[1])
        print('Max value in Dict: ', itemMaxValue[1])
        print('Key With Max value in Dict: ', itemMaxValue[0])
def main():
    auaTasks=TaskManager()
    personalTask=TaskManager()

    t=Task("Calculus HW","10/10/19", 8)
    auaTasks.addTask(t)

    t=Task("Get Ready For Midterms", "26/10/19" , 5)
    auaTasks.addTask(t)

    t=Task("Pay Cellphone Bill" , "22/10/19" , 2)
    personalTask.addTask(t)

    t=Task("sister Birthday Gift", "22/10/19", 10)
    personalTask.addTask(t)

    auaTasks.printAllTasks()
    personalTask.printTheMostImportantTask()
main()