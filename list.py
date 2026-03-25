# list=[]
# print(list)

# numbers=[10,20,30,40]
# print(numbers)
# mixed=["hello",100,True,None]
# print(mixed)

#numbers=[10,20,30,40,50]
#print(numbers[0],numbers[-5])

# print(numbers[1:4]) #1 will be included and 4 will be excluded
# print(numbers[:2])
# print(numbers[2:])
# numbers[1]=25
# print(numbers)
# numbers.insert(1,20)
# print(numbers)
# numbers.extend([60,70,80])
# print(numbers)
# numbers.append(90)

# numbers=[100,200,300,400,500]
# numbers.remove(300)
# print(numbers)
# numbers.pop()
# print(numbers)
# numbers.pop(-2)
# print(numbers)

#numbers=[100,200,300,400,500]
# for num in numbers:
#     print(num)

#search operation
# numbers=[100,200,300,400,500]
# if 200 in numbers:
#     print("Number available")
# else:
#     print("Number not found")


# numbers=[100,200,300,400,500]
# print(len(numbers)) #length
# print(max(numbers)) #find maximum number
# print(min(numbers)) #find minumum number
# numbers.sort()
# print(numbers)
# #numbers.reverse()
# #print(numbers.reverse())
# numbers=[100,200,300,400,500]
#numbers.reverse()
# r=numbers[::-1]
# print(r)

#compression
#print([x*x for x in range(5)])
#print([x for x in range(10) if x%2==0])

# marks=[]
# for subject in range(6):
#     marks.append(int(input(f"Enter student Marks:")))
# print(sum(marks))
# print(sum(marks)/len(marks))
# print(max(marks))
# print(min(marks))

# tasks=[]
# while True:
#     print("1. Add task")
#     print("2. Remove Task")
#     print("3. View Task")
#     print("4. Exit")

#     choice=input("Enter your choice")
#     if choice=="1":
#         task=input("Enter Task")
#         tasks.append(task)
#     elif choice=="2":
#         task=input("Enter Task")
#         tasks.remove(task)
#     elif choice=="3":
#         for task in tasks:
#             print(task)
#     elif choice =="4":
#         break

numbers=[10,20,10,10,20,50,60,90]
duplicates=[]
print(numbers.count(10))
print(numbers.count(20))

for num in numbers:
    if numbers.count(num)>1 and num not in duplicates:
        duplicates.append(num)
print(duplicates)





