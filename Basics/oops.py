# class Test:
#     def __init__(self):
#         pass
#     def __init__(self, name):
#         self.name = name;
        
# t1 = Test("Hello")
# print(t1.name)


# class Test:
#     def __init__(self,name=None,age=None):
#         self.name = name
#         self.age = age

# t1 = Test("Hello")
# print(t1.name,t1.age)

# t2 = Test("Hello1",22)
# print(t2.name,t2.age)

# class Test:
#     def m1(self,a,b):
#         print(a+b)
#     def m1(self,a,b,c):
#         print(a+b+c)
    
# t1 = Test()
# t1.m1(10,20,30)


# class Test:
#     def m1(self):
#         print("Hello")
#     def m1(self,x):
#         print("Welcome")

# t1 = Test()
# t1.m1()


# class Parent:
#     def m1(self):
#         print("Parent")

# class Child:
#     def m1(self):
#         print("Child")

# p1 = Parent()
# p1.m1()

# c1 = Child()
# c1.m1()



# class Test:
#     name = None
#     age = None

# t1 = Test()
# t1.__class__.name = "Test1"
# t1.age = 20

# t2 = Test()
# t2.__class__.name = "Wipro"
# t2.age = 22
# print(t1.age,t1.name,Test.name)
# print(t2.age,t2.name,Test.name)

# class Emps:
#     company = None

#     def __init__(self,name):
#         self.name = name

# e1 = Emps("Emp1")
# e1.__class__.company = "TCS"
# print(Emps.company, e1.name)




# class Emp:
#     company = None

# e1 = Emp()
# e1.__class__.company = "TCS"
# print(e1.company)
# print(Emp.company)


# Emp.company = "TCS"
# print(Emp.company)




# class Emp:
#     company = None
#     @classmethod
#     def set_company(cls,company):
#         cls.company = company

# Emp.set_company("TCS")
# print(Emp.company)



# class Parent:
#     def m1(self):
#         print("Hello")
# class Child(Parent):
#     def m1(self):
#         print("Welcome")

# c1 = Child()
# c1.m1()

# class Parent:
#     def m1(self):
#         print("Parent !!!")

# class Child(Parent):
#     def m2(self):
#         print("Child")

# c1 = Child()
# c1.m1()
# c1.m2()





# class Emps:
#     @classmethod
#     def test_msg(e1):
#         print("Hello")

# Emps.test_msg()

# e1 = Emps()
# e1.test_msg()




# class Emps:
#     company = "TCS"
#     def __init__(self,name):
#         self.name = name

# e1 = Emps("Emp1")
# e2 = Emps("Emp2")
# print(e1.name,"Working in :",Emps.company)
# print(e2.name,"Working in :",Emps.company)

# class Emplopyee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.salary = salary
    
#     def getName(self):
#         return self.name
    
#     def getSalary(self):
#         return self.salary
# e1 = Emplopyee("Emp1",100000)
# print(e1.getName())
# print(e1.getSalary())





# class Student:
#     def __init__(self,name,age,marks):
#         self.name = name
#         self.age = age
#         self.marks = marks

# s1 = Student("Std1",20,90)
# print(s1.name,s1.age,s1.marks)

# s2 = Student("Std2",22,92)
# print(s2.name,s2.age,s2.marks)



# class Student:
#     def __init__(self):
#         pass