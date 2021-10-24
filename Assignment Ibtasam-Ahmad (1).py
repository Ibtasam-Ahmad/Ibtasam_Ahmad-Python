#!/usr/bin/env python
# coding: utf-8

# In[55]:


"""1. Write a Python program to print the following string in a specific format (see the 
output). 
Twinkle, twinkle, little star, 
 
How I wonder what you are! 
 
Up above the world so high, 
Like a diamond in the sky. 
 
Twinkle, twinkle, little star, 
 
How I wonder what you are """

print("twinkle twinkle, little star")
print("\t How i wonder what you are ")
print("\t\t Up above the world so high")
print("\t\t Like a diomond in the sky")
print("twinkle twinkle, little star")
print("\t How i wonder what you are")


# In[56]:


"""2. Write a Python program to get the Python version you are using"""
import sys
print("Python Version")
print(sys.version)
print("Version Info")
print(sys.version_info)


# In[8]:


"""
3. Write a Python program to display the current date and time."""
import datetime
now = datetime.datetime.now()
print("Current date and time")
print(now.strftime(" %Y-%m-%d    %H-:%M:%S"))


# In[11]:


"""4. Write a Python program which accepts the radius of a circle from the user and compute 
the area. """
r = int(input("enter the radius "))
A = 3.14 * (r**2)
print(A)


# In[30]:


""" 
5. Write a Python program which accepts the user's first and last name and print them in 
reverse order with a space between them. """
first_name = str(input("enter first name "))
last_name = str(input("enter last name "))
print(last_name, first_name)


# In[33]:


"""6. Write a python program which takes two inputs from user and print them addition"""
integer_1 = int(input("enter first integer "))
integer_2 = int(input("enter second integer "))
sum = integer_1 + integer_2
print("the sum of integers are", sum)


# In[2]:


"""7. Write a program which takes 5 inputs from user for different subject’s marks, total it 
and generate mark sheet using grades ? """
sub_1 = int(input("enter first subject marks from 100 "))
sub_2 = int(input("enter second subject marks from 100 "))
sub_3 = int(input("enter third subject marks from 100 "))
sub_4 = int(input("enter fourth subject marks from 100 "))
sub_5 = int(input("enter fifth subject marks from 100 "))
total = sub_1 + sub_2 + sub_3 + sub_4 + sub_5
print("total marks are ", total)
Percentage = (total/500)*100;
print("Percentage is " , Percentage , "%")
if Percentage<101 and Percentage>79:
    print("A Grade")
elif Percentage<80 and Percentage>64:
    print("B Grade")
elif Percentage<65 and Percentage>55:
    print("C Grade")
elif Percentage<56 and Percentage>49:
    print("D Grade")
elif Percentage < 0 and Percentage >100:
    print("enter valid grades")
else:
    print("F Grade")


# In[35]:


"""8. Write a program which take input from user and identify that the given number is even 
or odd? """
num = int(input("enter the number "))
if num%2:
    print("number is odd")
else:
    print("number is even")


# In[15]:


"""8. Write a program which take input from user and identify that the given number is even 
or odd? """
list = [123, 'xyz', 'ibtasam', 'shibtasam@gmail.com']
print ("First list length : ", len(list))


# In[54]:


"""8. Write a program which take input from user and identify that the given number is even 
or odd? """
org_list = [1, 2, 3, 4, 'a', 'b', 'c', 5, 'd', 'e', 10]
print ("initial list", str(org_list))
res = 0
for item in org_list:
    try:
        res+= int(item)
    except ValueError:
        pass
print ("resultant sum of numeric letters is", res)


# In[45]:


"""11.Write a Python program to get the largest number from a numeric list. """
lis = [10, 20, 50, 30, 40]
print("Largest number in the list is:", max(lis))


# In[28]:


"""12. Take a list, say for example this one: 
 
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
 Write a program that prints out all the elements of the list that are less than 5."""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)

