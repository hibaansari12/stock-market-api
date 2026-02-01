#list operations
num = [1,2,3,4]
num.append(5)
print(type(num))
num.remove(1)
print(num,"after removing")
for n in num:
    print(n *n)

#tuple
c=(1,30)
print(c)

#set
a= {1,2,3,4}
print(a)

#dictionary

students ={
"Name": "hiba",
"age" : 24,
"roll_no" : 1
}
print(students)
print(students["Name"])

# conditonal statements

marks = int (input("Enter your marks: "))

if marks <35:
    print("fail")
elif marks >=35:
    print("pass")
else:
    print("first class")

#for loop
students = ["A", "B", "C", "D"]

for s in students:
    print("Present:", s)

#while loop
password = "hello"
attempts = 0
max_attempts = 3
while password != "python" and attempts < max_attempts:
    attempts += 1
    password = input("Enter password: ")
if password =="hello":
    print("Access granted")
else:
    print("Access denied")

#2 table

for i in range(1,11):
    print("2 x", i, "=", 2 * i)

# prime number

  
# break and continue
for i in range(1,11):
    if i == 5:
        continue
    print(i)

#Sum all even numbers from 1 to 100
total = 0
for i in range(1,101):
    if i % 2 ==0:
        total += i
print("Sum of even numbers from 1 to 100 is:", total)

#Find common elements between two lists.

list1 = [1,2,3,4,5]
list2 =[4,5,6,7,8]
common_elements = []
for element in list1:
    if element in list2:
        common_elements.append(element)
print("Common elements:", common_elements)
              
