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

smartness = input("how smart are you?\n")
Class = input("how hard is your class?\n")
student1=student(int(smartness),int(Class))
student1.canHeDoIt()