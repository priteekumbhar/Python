#!/usr/bin/env python
# coding: utf-8

# In[3]:


print("hello world")


# In[4]:


print("123")


# In[5]:


print("1.2")


# In[6]:


print(124)


# In[5]:


print(10.4)


# In[6]:


print(True)


# In[7]:


print(False)


# In[10]:


print(True,"hello world",12,12.3,sep=",")


# In[18]:


print("hello",end=" ")
print("world")


# Data types

# In[19]:


#string
print('hello world')
print("hello world")
print('''hello world''')


# In[20]:


print('I don't like it')


# In[21]:


print("I don't like it")


# In[22]:


#integer
print(12)


# In[23]:


print(1e309)


# In[24]:


print(1e308)


# In[25]:


#float
print(17.2)


# In[26]:


print(1.8e308)


# In[27]:


print(1.7e308)


# In[28]:


#complex
print(3+5j)


# In[29]:


#boolean
print(True)
print(False)


# #collection data types
# 

# In[30]:


#list
print([1,True,2,'hello world'])


# In[31]:


type([1,True,2,'hello world'])


# In[32]:


#tuple
print((1,True,"hello world"))


# In[33]:


type((1,True,"hello world"))


# In[38]:


#set
print({1,2,"hello world"})


# In[37]:


type({1,2,"hello world"})


# In[41]:


#dictionary
print({'name':'abc','age':23})


# In[40]:


type({'name':'abc'})


# In[44]:


a=5
b=5
b=10
print(id(a))
print(id(b))
print(a+b)


# In[43]:


print(id(a))
print(id(b))


# In[45]:


2a=10


# In[2]:


firstnumber=1


# In[47]:


firstnumber=3


# In[48]:


fist_num=5


# In[49]:


_abd=10


# In[50]:


import keyword
print(keyword.kwlist)
len(keyword.kwlist)


# In[51]:


firstnumber=2
secondmuber=4
print(firstnumber+secondmuber)


# input function

# In[10]:


a=int(input())
b=int(input())
print(a+b)


# In[7]:


print(a+b)


# In[2]:


print(bool())


# In[5]:


bool('')


# In[6]:


bool(' ')


# # type casting

# In[2]:


int(10)


# In[5]:


int(10+3j)


# In[6]:


int(True)


# In[7]:


int(False)


# In[8]:


int("hello")


# In[9]:


int("10")


# In[16]:


float("3.4")


# In[17]:


float(9)


# In[18]:


str(12)


# In[19]:


str(3+4j)


# In[20]:


str(12.5)


# In[21]:


bool(34)


# In[22]:


bool(0)


# In[24]:


bool('sona')


# In[25]:


bool("0")


# In[26]:


bool("")


# In[28]:


bool(3+4j)


# # operators in python

# # arithmetic operators

# In[31]:


a=5
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)


# In[33]:


print(a//b)#flooar division


# In[34]:


#modulo
# for reminder written %
print(a%b)


# In[35]:


#power
a**2


# In[36]:


a**3


# # Relational operators

# In[37]:


print (4<5)


# In[38]:


print(4>5)


# In[39]:


print(4>=5)


# In[40]:


print(4<=5)


# In[44]:


print(4==5)#equal to


# In[43]:


print(4!=5)# not equal to


# # Logical Operators

# and - if both conditions True =1
# 
# 
# or - if at least one condition true=1
# 
# 
# not

# In[45]:


1 and 0


# In[46]:


1 or 0


# In[47]:


not 0


# In[48]:


not 1


# In[49]:


1 and 0


# In[50]:


1 or 0


# In[51]:


4<5 and 4>5


# In[52]:


4<5 or 4>5


# # assignment operator

# In[53]:


a=5
a=a+1
print(a)


# In[55]:


b=5
b+=1 #short hand method
print(b)


# In[56]:


b=4
b-=1
print(b)


# # Membership operator

# in
# 
# not in

# In[57]:


print("p" in "pune")


# In[58]:


print("P" in "pune")


# In[59]:


print("P" not in "pune")


# In[63]:


int(input())


# In[6]:


number=int(input())
#345-->5
a=number%10

#345--->34
number=number//10
b=number%10
number=number//10
c=number%10
print(a+b+c)


# In[3]:


#area of triangle
base=int(input())
height=int(input())
area=base*height/2
print(area)


# In[6]:


#area of triangle

base=int(input())
height=int(input())
area=base*height//2
print(area)


# In[11]:


fer=int(input())
print((fer-32)*5/9)


# In[9]:


fer=int(input())
a=(fer-32)*(5/9)
print(a)


# In[2]:


number=int(input())
a=number%10
print(a)


# In[5]:


a=5
b=5
if a==5:
    print('both are equal')


# In[12]:


a=5
b=5
if a<5:
    print('a is greater than 5 ')


# In[17]:


number=int(input())
if number%2==0:
    print("number is even")
    
else:
    print("number is odd")


# In[13]:


a=10
b=10

if a>b:
    print ("a is greter")


# In[14]:


a=90
b=100

if a>b:
    print("a is greater")

elif b>a:
    print("b is greater")
    
else:
    print("both are equal")


# In[20]:


score=eval(input())
                 
if score>=90 and score<100:
                 print ('your grade is A+')
elif score>=80:
                 print('your grade is A')
elif score>=70:
                 print('your grade is B')
elif score>=60:
                 print('your grade is C')
elif score>=50:
                 print('your grade is D')
elif score>=40:
                 print('you just pass')
else:
                 print('fail...')



# In[21]:


mail_ID=input("Enter your mail_ID")
password=input("Enteryour password")
if mail_ID=="sgm@gmail.com" and password=="123":
    print("welcome")
else:
    print("Information is not valid")


# In[23]:


mail_ID=input("Enter your mail_ID")
password=input("Enteryour password")
if mail_ID=="sgm@gmail.com" and password=="123":
    print("welcome")
elif mail_ID=="sgm@gmail.com" and password!="123":
    print("password wrong..")
else:
    print("Information is not valid")


# nastle if elif

# In[ ]:





# In[5]:


mail_ID=input("Enter your mail_ID")
password=input("Enteryour password")
if mail_ID=="sgm@gmail.com" and password=="123":
    print("welcome")
elif mail_ID=="sgm@gmail.com" and password!="123":
    print("password wrong..")
    
    password=input("Enter your password again...")
    
    if password=="123":
        print("Finally Welcome...")
    else:
            print("Get lost...")
else:
    print("Information is not valid")


# In[6]:


mail_ID=input("Enter your mail_ID")
password=input("Enteryour password")
if mail_ID=="sgm@gmail.com" and password=="123":
    print("welcome")
elif mail_ID!="sgm@gmail.com" and password=="123":
    print("mail_ID wrong..")
    
    mail_ID=input("Enter your mail_ID again...")
    
    if mail_ID=="123":
        print("Finally Welcome...")
    else:
            print("Get lost...")
else:
    print("Information is not valid")


# # Modules in Python

# In[7]:


import math


# In[10]:


math.sqrt(9)


# In[12]:


import keyword
print(keyword.kwlist)
len(keyword.kwlist)


# In[14]:


import random


# In[26]:


print(random.random())
print(random.randint(1,14))


# In[21]:


import datetime


# In[23]:


print(datetime.datetime.now())


# In[24]:


help("modules")


# # Loop

# In[1]:


number=int(input("Enter your number"))
i=1

while i<11:
    print(i*number)
    i+=1



# In[2]:


number=int(input("Enter your number"))
i=1

while i<11:
    print(i,"X",number,"=",i*number)
    i+=1


# In[1]:


number=int(input("enter your number"))
i=1

while i<11:
    print(i)
    i+=1


# In[3]:


number=int(input("enter your number"))
i=10

while i>=1:
    print(i)
    i-=1


# In[7]:


import random
x=random.randint(1,100)

i=1

while i>100:
    print(i)
    i=x
    


# # Day 3

# In[2]:


str="python"
for i in str:
    print(i)


# In[5]:


for i in range(1,6):
    print("good morning ")


# In[7]:


A="1256"
for i in A:
    print(A)


# In[9]:


A=1256
for i in A:
    print("A")


# In[12]:


ste="we are learning python"
for i in ste:
    print(ste)


# In[14]:


str="we are learning python"
for i in range(5):
    print(str)
    print("hi")
    print(" ")


# In[15]:


string="python"
for i in range(100):
    print(string)


# In[ ]:


marks=int(input("Enter marks of students=34"))
if marks>150:
    print('welcome to medical admissions process')
    


# In[16]:


List1=[1,2,3,4,5]
for i in List1:
    print(i)


# In[24]:


list=[1,7,True,"#","str"]


# In[25]:


list


# In[32]:


for i in list:
    if type(i)==int:
        print(i)
    
    


# In[34]:


print("Integer",1)


# In[37]:


for i in range(1,10):
    print("*"*i)

    


# In[1]:


list2=[1,2,3.7,5.8,"python",'*','12.5',25]
for i in list2:
    if type(i)==int:
        print(i)


# In[5]:


for i in list2:
    if type(i)==float:
        print('character is float',i)
    elif type(i)==int:
        print('character is integer',i)
    else :
        print('character is string',i)


# In[3]:


for i in list2:
    if type(i)==str:
         print(i)


# In[6]:


set={1,2,3,4,4}


# In[7]:


for i in set:
    print(i)


# In[3]:


Tuple=(1,2,2,4,5)


# In[4]:


for i in Tuple:
    print(i)


# In[10]:


dict=({"Name":"pritee","Age":"22"})


# In[11]:


for i in dict:
    print(i)


# In[12]:


x=5
print(type(x))


# In[13]:


if 5>2:
    print("five is greater than two")


# In[1]:


x=(4,5)
for i int(i,5)


# In[19]:


string='training'
for i,v in enumerate(string):
    print(i,v)


# In[20]:


range=(1,5)
for i,v in enumerate(range):
    print(i,v)


# In[21]:


list=[1,2,3,4,5,7]
for i,v in enumerate(list):
    print(i,v)


# In[30]:


tuple=(1,2,3,4,5,6,6,78)
for i,v in enumerate(tuple):
    print(i,v)


# In[31]:


set={1,3,"tul",3}
for i,v in enumerate(set):
    print(i,v)


# In[32]:


set={1,3,"tul",3,3,4,5,5,6,7}
for i,v in enumerate(set):
    print('index',i,'value',v)


# In[41]:


list1=[1,3,5,3,6,64,4,4,3]
for i,v in enumerate(reversed(list1)):


# In[39]:


for item in enumerate("string"):
    index,value=item
    print(item)
    print(index,value)


# In[40]:


list1=[1,3,5,3,6,64,4,4,3]
for i,v in enumerate(reversed(list1)):
    print('index',i,'value',v)


# In[3]:


#Control transfer statement-1 continue
range(1,16)
for i in range(1,16):
    if i==5:
     continue
    print(i)


# In[6]:


for i in range(1,11):
    if i%2==1:
        continue
    print(i)
        
     


# In[8]:


for i in range(1,201):
    if i%2==1:
        continue
    print(i)
    


# In[10]:


for i in range(1,201):
    if i%7!=0:
        continue
    print(i)


# In[12]:


for i in range(1,201):
    if i%7!=0:
     print(i)


# In[13]:


#break


# In[2]:


for i in range(1,11):
    if i==5:
        break
    print(i)


# In[5]:


for var in "Greek":
    if var=='e':
        continue
    print(var)


# In[8]:


number=[1,2,3,9,8,8,9]
for i in number:
    if i%2==0:
        break
    print(i)


# In[10]:


for i in range(9):# continue -skip the iteration if the variable i is 3,but continue with next iteratio
    if i==3:
        continue
    print(i)


# In[11]:


for i in range(9):
    if i>3:
        break
    print(i)


# In[12]:


#pass
for i in range(1,11):
    pass
print('hello')


# In[20]:


for i in range(1,11): 
    if i==3:
        pass
    else:
        print(i)


# In[ ]:





# In[ ]:




