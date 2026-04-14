# import seaborn as sns
# from matplotlib import pyplot as plt
# df=sns.load_dataset("tips")
# print(df.head())



#tuples


student=("Ravi",True,20)
print(student[0])
#immutable
#student[1]=22 not allow

#allow duplicates
# numbers=(10,20,10,20)
# print(numbers.count(10))

# slicing
# numbers=(10,20,30,40,50)
# print(numbers[2:4])
# print(numbers[:2])
# print(numbers[1:])

#iteration
# subjects=("Python basics","ML","DL","NLP","Agentic AI")
# for sub in subjects:
#     print(f"Subject is: {sub}")

#packing - unpacking
# data=10,20,30 #packing
# print(data)
# t1,t2,t3=data #unpacking
# print(t1,t3)

#functions
# def test_func():
#     return ("Std1","121")
# df=test_func()
# print(df)
# (sname,age)=test_func()
# print(sname,age)

#nesting
# nested=(
#     ("emp1",1000),
#     ("emp2",2000),
#     ("emp3",3000)
# )
# for tuple in nested:
#     empName,salary=tuple
#     print(f"Emp Name is: {empName}, Salary is: {salary}")
    
# tuple=(10,)
# print(tuple)

# tuple= (10,20,30,40,50,60,70,80,90,10)
# print(tuple.index(50))
# print(tuple.count(10))
# print(tuple.index(10))

# list1=[("Emp1",1000),("Emp2",2000)]
# list1.append(("emp3",3000))
# print(list1)
# for l in list1:
#     for e in l:
#         ename,sal=e
#         print(f"Emp is: {ename}, Salary is: {sal}")


# tuple=(10,20,30)
# print(len(tuple))
# print(max(tuple))
# print(min(tuple))
# print(tuple[::-1])
# a=10
# b=20
# a,b=b,a
# print(a,b)

# t=(10,20,30)
# l=list(t)
# print(l)
# l.append(60)
# t=tuple(l)
# print(t)
# found=False
# for e in t:
#     if e==30:
#         found=True
# print(found)

# nums=(10,20,30,40,50)
# l=list(nums)
# l.remove(30)
# t=tuple(l)
# print(t)

#nested tuple to single tuple
# nested=((10,20),(30,40),(50,60))
# flat=()
# for pair in nested:
#     flat+=pair
# print(flat)

#second largest number and first largest number
# numbers=(10,20,30,40,50,90)
# first=second=float('-inf')
# print(first)
# for num in numbers:
#     if num>first:
#         second=first
#         first=num
#     elif num>second and num!=first:
#         second=num
# print(second)
# print(first)

# data=(10,20,30,30,40,40,50)
# data1=set(data)
# t=tuple(data1)
# print(t)

# numbers=(10,20,30,40,50,60)
# minimum=maximum=[0]
# for num in numbers:
#     if num < minimum:
#         minimum=num
#     elif num > maximum:
#         maximum=num
# print(minimum,maximum)


# numbers=(10,20,30,40,50)
# a,*b,c=numbers
# print(a,b,c)