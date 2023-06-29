from ClassActivity import student
#from ClassActivity import course
#have to put this inpi
smartness = input("tell us how smart you are on a scale of 1 to 10!\n")
Class = input("how hard is your class?\n")
student1=student(int(smartness),int(Class))
student1.canHeDoIt()


