# -------------------- STRING CONCATENATION --------------------

"""one = "apna"
two = "college"
final = one + two

print(final)          # apnacollege
print(len(one))       # length of "apna"

luu = two
print(len(luu))       # length of "college"


# -------------------- STRING FUNCTIONS EXAMPLES --------------------

name = "adarsh"

print(name.startswith("a"))
print(name.capitalize())
print(name.replace("a", "s"))
print(name.find("a"))
print(name.count("a"))
print(name.upper())


# -------------------- TRAFFIC LIGHT PROGRAM --------------------

light = input("Light color: ")

if light == "red":
    print("Stop")
elif light == "yellow":
    print("Ready")
elif light == "green":
    print("Go")
else:
    print("Wrong colour")


# -------------------- GRADE CALCULATOR --------------------

marks = int(input("Enter marks: "))

if marks > 90:
    print("A Grade")
elif 80 <= marks <= 90:
    print("B Grade")
elif 70 <= marks < 80:
    print("C Grade")
else:
    print("Fail")


# -------------------- LIST BASICS --------------------

marks_list = [44, 55, 6, 76, 55]
print(marks_list[3])   # 76

# List manipulation
student = ["sahil", 44, "adarsh"]
student[1] = "sss"
print(student)

# List slicing #

std = [33,44,55,66,77,64,88]
print(std[3:4])                                                                            

# (33,44)#
#append#"""

"""strr = [33,44,33,22,11]
strr.append(999)
print(strr.sort())
print(strr)

#reverse and append #
liist = [3,2,4,3]
print(liist.count(3))"""


# tuples #


"""li = [1,2,3,4,5,6,7,8,9,10]

print(list[0])
print(li[-1])
print(len(li)  //2)"""

#distonary

"""dict = {
    "name":"adarsh",
    "marks":77,
    "age":23,
"topics":("java","python"),
"students": {
    "maths":55,
    "hindi":59
}

}"""



 
#sets

"""set1 = {"python","java","cpp","python","javascript","java","python","java","cpp,","c"}
set2 = {"python","java","cpp","python","javascript","java","python","java","cpp,",}

print(set1.union(set2) )"""

# dictonary homework

"""dict = {"cat" : "a small animal ",
        
        "table"  :  ["hhh","ggg"]
        }

print(dict)


set = ("python", "java", "javascript","c++")


newdict = (input("enter marks 1"))
ddd = (input("enter marks 2"))
ccc = (input("enter marks 3"))

print(newdict)
print(ddd)
print(ccc)"""



"""name  = {"namee" : "manish",
         "age" : 33,
         "course": "bca"}

print(name.get("course"))  # but yaha pe "" quotes me q likha wo to string ban jayega na
name.update({"age" : 222})
print(name)
name.update({"city" : "mumbai"})
print(name)"""

"""product = {"apple": 40, "banana": 20, "mango": 60}

print(product.get("banana")) # 1st answer
product.update({"banana": 99}) # 2nd answer
print(product)                                                              # perfect

product.pop("apple") # third answer
print(product)


new_dict = {
    "name" : "adarsh",
    "age" : 33,
    "city" : "mumbai",
    "course" : "bca",
    "address" : "home"
}

print(len(new_dict))
print(new_dict.items())


d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

d1.update({"c": 3, "d": 4})
print(d1) """


# important loops concept 

"""i = 1
while i <=100 : # first peactice question done 
    print(i)
    i +=1"""

"""i =100
while i >=1 :
    print(i)
    i-="""



"""tupple = (3,4,5,6,7,8,9,0,5)



i = 1
while i <= 20:
    print("hello")
    if i == 15:
     break                            # executed properly just make sure sure it has to be assign inside loop
    i +=1"""


# muscle memory 

"""i = 1 
while i <=20 :
    print(i)
    i +=1                           # why it doesnt print 9 only 8 
    if i == 9:
        break"""


"""i = 1
while i <=10:
    if(i ==4):
        print(i)
        i +=1
        continue
    if( i == 8):
        break
    print(i)
    i+=1"""

"""listtt = [1,2,3,4,5,6]
x = int(input("enter number "))

for adarsh in listtt:
    if x == adarsh:
        print("found")
        break
else:
    print("not found")"""

"""x = int(input("enter a number "))

for i in range ( 0 ,11):
    print (x *i)"""

"""l = 0

for i in range( 0 , 51 ,1):
     l +=i
     print(i)

 

i = 1
while i < 3:
    print(i)  # ye sab code me na python pehle print krega fir condiotion check krega a
    i += 1"""


"""def average (num1, num2 , num3 ):
     result  = (num1 + num2 + num3) / 3        # why we have to write print first before return why it doesnt take after return
     return result


final = average(22,33,44)
print(final)


li = [1,2,3,4,"ad",8]

def lenoflist ():
     print(len(li))
     return lenoflist

lenoflist()"""

"""x = int(input("Enter first number: "))
y = input("Enter operator ")
z = int(input("Enter second number: "))

if y == "+":
    print(x + z)

elif x =="-":
        print(x-z)
elif x == "*":
            print(x*z)
else:print("invalid")"""""



"""usd = int(input("enter number"))
def converter (a):
        final = usd * 83
        print(final)
        return final 

converter(3)

x  = int(input("enter a number"))
def evenodd (a):
        if x % 2 == 0:
                print("even")
        else:print("odd")
        return evenodd


evenodd(3)
print(evenodd)"""





def add_tudents (name,marks):
    with open ("practice.txt","a") as f:
      f.write(("adrashhhhhh","99"))
       

        
  








