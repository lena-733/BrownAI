class student:
    def __init__(self, smartness, Class):
        self.smartness = smartness
        self.Class = Class
    def canHeDoIt(self):
        if self.smartness>=5 and self.Class<=5:
            print("they can pass the class")
        elif self.smartness>=5 and self.Class>=5:
            print("maybe they could pass")
        elif self.smartness<=5 and self.Class>=5:
            print("they can't pass the class")
        elif self.smartness<=5 and self.Class<=5:
            print("he can probably pass")

class course:
    def __init__(self, students, teacher):
        self.students = students
        self.teacher = teacher
    def courseinfo(self):
        print("This course is taught by "+ self.teacher + " and has " +str(self.students)+ " students")



if __name__ =="__main__":
    smartness = input("how smart are you?\n")
    Class = input("how hard is your class?\n")
    student1=student(int(smartness),int(Class))
    student1.canHeDoIt()
    #not sure how to work this 



#if __name__ =="__main__":
#use this if you don't want a piece of code to run
