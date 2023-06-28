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

student1=student(3,1)
student1.canHeDoIt()