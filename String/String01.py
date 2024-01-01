#!/usr/bin/env python
# coding: utf-8

# 1) write a python program to calculate length of string

# In[1]:


s="sonali satish nikam"
print(len(s))


# 2)write a program to check if the word 'orange'is present in "This is orange juice"

# In[2]:


a = "This is orange juice"
print ('orange' in a.split())


# In[7]:


a = "This is orange juice"
print('orange'in a)


# In[3]:


a = "This is orange juice"
a[8:14]


# 3. capitalize the first character of the string

# In[4]:


a = "this is orange juice"
a.capitalize()


# 4. reverse the string "hello world"

# In[5]:


a="hello world"
a[::-1]


# 5. convert integer into str

# In[6]:


a=24
str(a)


# 6. check if string contain only number

# In[25]:


str1 = '12343445588665'
for i in str1:
    if str1.isdigit():
        print("Str1 contains all numbers")
    else:
        print("Str1 doesn't contains all numbers")


# 7.give example of string slicing

# In[26]:


b = "Hello, World"
print(b[:5])


# 8.write a program to find the length of the string "machine learning"

# In[27]:


a="machine learning"
print(len(a))


# 9. check if the string contains only characters of the alphabets

# In[29]:


a="datascience"
a.isalpha()


# 10. write a python program to get a string made of the first 2 and last 2 character from a given string.

# In[31]:


a="hello world"
count = 0
for i in a:
      count = count + 1
newString = a[ 0:2 ] + a[count - 2: count ] 
print("a = " + a)
print("New String = "+ newString)


# 11. how would you conform that 2 strings have the same identity?

# In[32]:


s1 = "Hello"
s2 = "Hello"
print(id(s1) == id(s2))


# 12. count the no. of special characters in the string

# In[33]:


string="Sonali Satish Nikam, sonalinikam12@gmail.com"

def count_special_characters(string):
    special_char = 0
    for i in range(0, len(string)):
        ch = string[i]
        if (string[i].isalpha()):
            continue
        elif (string[i].isdigit()):
            continue
        else:
            special_char += 1
    return special_char


# In[34]:


count_special_characters(string)


# 13.remove white space from string

# In[35]:


a="sonali satish nikam"
a = a.replace(" ", "")
print(a)


# 14.following string convert into uppercase

# In[39]:


s="my name is sonali"
s.upper()


# 15. check the first character in a string is lowercase

# In[40]:


s='sonalinikam'
if s[0].islower():
    print("True")
else:
    print("False")

