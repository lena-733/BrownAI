from classfile import student
from classfile import course
#from ClassActivity import course
#have to put this in
smartness = input("tell us how smart you are on a scale of 1 to 10!\n")
Class = input("how hard is your class?\n")
student1=student(int(smartness),int(Class))
student1.canHeDoIt()

students = input("how many students in this course?\n")
teacher = input("what is the teachers name?\n")
course1 = course(int(students), teacher)
course1.courseinfo()
