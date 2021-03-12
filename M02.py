class Student:
    def __init__(self, name, id): 
        self.studName=name
        self.studId=id


x = Student("神魔三國志","101010100")
print(x.studName, "\t",x.studId)