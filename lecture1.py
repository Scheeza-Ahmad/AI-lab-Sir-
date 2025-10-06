print("Hello world")
name = " Ali"
age = 20
GPA = 3.5
login = True


print(name)
print(age)
print(GPA)
print(login)

print(type(name))
print(type(age))
print(type(GPA))
print(type(login))

# value = input('Helo, Enter the Number :')
# print(type(value))

login = input('Helo, Enter the status :')
print(type(login))

name = "Ali"
age =20

print(f"name is {name}")

day = 5
if day==5:
  print("Friday")
elif day==4:
  print("Thursday")
else:
  print("Weekend")

print(5+5)
print(5-5)
print(5*5)
print(5/5)
print(5%2)

# for(int i=5;i<10;i++){

# }

# for i in range(10):
#   print(i, end =" ")

# for i in range(3,15):
#   print(i, end =" ")


for i in range(20,5,-2):
  print(i, end =" ")

i =10

while i>0:
  print(i, end = "-")
  i=i-1

arr =[1,2,3,4,5,'Hello',True, 5,5,4.6,78]

print(arr)
# for i in arr:
#   print(i,end=" ")

arr.append("UCP")
print(arr)
arr.insert(2,"Ali")
print(arr)
print(f" 5 occurs {arr.count(5)} times")
arr.remove(5)
print(arr)
arr.pop(5)
print(arr)
arr.extend([1,2,7,8,9])
print(arr)
copied= arr.copy()
print(copied)
arr.clear()
print(arr)
copied= arr.copy()
print(copied)
# print(f" Sorted Array {arr.sort()} ")
# print(f" Reversed Array {arr.reverse()} ")

# print(dir(arr))
# print(help(arr))

data  ="Hello, I'm in UCP and here i'm studying in BSCS"
print(data)
print(data[3:10])
print(data[:10])
print(data[3:])
print(data[1:20:3])
print(data[::-1])


print(dir(data))

def sum(a,b):
  return a+b
print(sum(5,9))
