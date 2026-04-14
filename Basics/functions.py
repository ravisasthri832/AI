# particular business logic called as function
# functions are used to "reuse" the business logic
# "def" is the keyword used to define the function

# definition without parameters and without return type
# definition without parameters and with return type
# definition with parameters and without return type
# definition with parameters and with return type

def demo(a,*t, b=10,c=20,**d):
    print(a,b,c,d)
demo(1, 40, 50, name='hello', age='40')

# def demo(a,b=10,c=20,*t,**d):
#     print(a,b,c,t,d)

# demo(10,None,None,20,30,40,x=10,y=20)



# def test(**data):
#     print(data)
#     print(type(data))
# test(name="siva",age=40)


# def test(*num):
#     print(type(num))

# test(1,2,3)




# def total(*num):
#     return sum(num)
# print(total(10,20,30,40,50))


# def test(a,b):
#     print(a,b)
# test(20,10)
# test(10,b=10)
# test(a=10,20)


# def test(name,age):
#     print(name, age)
# test('Siva',40)
# test(age=40, name="Siva")



# def test(num1,num2=200):
#     print(num1+num2)

# test(100)
#test()
#test(1000,2000)
#test(100,200,300)

# def wish(param="Good Morning !!!"):
#     print("Hello :", param)

# wish()
# wish("Basics")



# def power_ex(num1,num2):
#     res = num1 ** num2
#     return res
# x = power_ex(2,2)
# print(x)


# def power_ex(num1,num2):
#     res = num1 ** num2
#     print(res)
# power_ex(2,2)




# def power_ex():
#     num1 = 2
#     num2 = 2
#     res = num1 ** num2
#     return res
# x = power_ex()
# print(x)



# def power_ex():
#     num1 = 2
#     num2 = 2
#     res = num1 ** num2
#     print(res)
# power_ex()



# def addition(num1,num2):
#     res = num1 + num2
#     return res

# x = addition(200,100)
# print(x)



# def addition(num1,num2):
#     res = num1 + num2
#     print(res)
# addition(200,100)



# def vector_db_func():
#     username = "admin"
#     password = "admin@123"
#     res = "Login Success" if username == "admin" and password == "admin@123" else "Login Fail"
#     return res
# status = vector_db_func()
# print(status)






# def db_func():
#     username = "admin"
#     password = "admin@123"
#     res = "Login Success" if username == "admin" and password == "admin@123" else "Login Fail"
#     print(res)

# db_func()