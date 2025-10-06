# #Comment python main hash sa hota hai

# #SIMPLE PRINT STATEMENT
# print("Hello world")

# #DIFFERENT DATATYPES
# name = " Ali"
# age = 20
# GPA = 3.5
# login = True #true small nhi likh sakta

# print(name)
# print(age)
# print(GPA)
# print(login)

# print(type(name))
# print(type(age))
# print(type(GPA))
# print(type(login))

# #TAKING INPUT
# # aagar input ko type na dain to by default type hoti hai str 
# value = input('Helo, Enter the Number :')
# print(type(value))

# login = input('Helo, Enter the status :')
# print(type(login))

# #agar tum chahti ho ka input ki type int ho to :
# num=int(input('Enter the number : '))
# print(type(num))

# #F STRING IN PYTHON==>AGAR APNA KISI CHEZ KI STATEMENT KA SATH KOI VARIABLE BHI PRINT KARAAN HO
# name = "Ali"
# age =20

# print(f"name is {name}")

# # ALTERNATE TAREEKA 
# print('The name is : ',name)

# #IF ELSE STATEMENT

# day = 5
# if day==5:
#   print("Friday")
# elif day==4:
#   print("Thursday")
# else:
#   print("Weekend")

# #ARITHMATIC OPERATIONS 

# print(5+5)
# print(5-5)
# print(5*5)
# print(5/5)
# print(5%2)

# #LOOPS 
# #FOR LOOP
# #Agar sirf aik chez hai to starting condition would be 0 and only the ending is given in the brackets
# for i in range(10):
#   print(i, end =" ")

# #Starting and ending condition is given 
# for i in range(3,15):
#   print(i, end =" ")

# #pehli hai starting condition dosri hai ending condition aur tesri hai intervals
# for i in range(20,5,-2):
#   print(i, end =" ")

# # WHILE LOOP 
# i =10
# while i>0:
#   print(i, end = "-")
#   i=i-1

# #ARRAY 
# arr =[1,2,3,4,5,'Hello',True, 5,5,4.6,78]

# # print(arr) #yeh array ko arrray format main print karai ga 

# # #yeh array ka only har inex pa jo para hua hai usa print karai ga
# # for i in arr:
# #   print(i,end=" ")

# #APPEND END PA ADD KARTA HAI
# arr.append("UCP")
# print(arr)

# #INSERT SPECIFIC POSITION PA ADD KARTA HAI
# # arr.insert(2,"Ali")
# # print(arr)


# print(f" 5 occurs {arr.count(5)} times")

# #REMOVE FIRST OCCURANCE KO REMOVE KARTA HAI 
# arr.remove(5)
# print(arr)

# #POP USS INDEX PA JO CHEZ PARI HOTI HAI USA REMOVE KARTA HAI 
# arr.pop(5)
# print(arr)

# #EXTEND END PA ADD KARTA HAI 
# arr.extend([1,2,7,8,9])
# print(arr)

# copied= arr.copy()
# print(copied)

# arr.clear()
# print(arr)

# copied= arr.copy()
# print(copied)

# #SORT AUR REVERSE MAIN ARRAY KA DATATYPE SAME HONA CHAHIYA
# print(f" Sorted Array {arr.sort()} ")
# print(f" Reversed Array {arr.reverse()} ")


# print(dir(arr))
# print(help(arr))

# data  ="Hello, I'm in UCP and here i'm studying in BSCS"
# print(data)
# #starting aur ending point diya hua hai 
# print(data[3:10])
# #sirf ending index diya hua starting 0 hai
# print(data[:10])
# #sirf staring index diya hua hai ending nhi hai
# print(data[3:])
# #starting ending index ka sath sath intervals bhi diya hua hai
# print(data[1:20:3])
# #staring index 0 ending last aur intervals hai -1
# print(data[::-1])
# print(dir(data))

# #FUNCTION
# def sum(a,b):
#   return a+b
# print(sum(5,9))
