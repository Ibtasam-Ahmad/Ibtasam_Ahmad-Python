#!/usr/bin/env python
# coding: utf-8

# In[2]:


print("twinkle twinkle, little star")
print("\t How i wonder what you are ")
print("\t\t Up above the world so high")
print("\t\t Like a diomond in the sky")
print("twinkle twinkle, little star")
print("\t How i wonder what you are")


# In[12]:


import sys
print("Python Version")
print(sys.version)
print("Version Info")
print(sys.version_info)


# In[8]:


import datetime
now = datetime.datetime.now()
print("Current date and time")
print(now.strftime(" %Y-%m-%d    %H-:%M:%S"))


# In[11]:


r = int(input("enter the radius "))
A = 3.14 * (r**2)
print(A)


# In[30]:


first_name = str(input("enter first name "))
last_name = str(input("enter last name "))
print(last_name, first_name)


# In[33]:


integer_1 = int(input("enter first integer "))
integer_2 = int(input("enter second integer "))
sum = integer_1 + integer_2
print("the sum of integers are", sum)


# In[2]:


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


num = int(input("enter the number "))
if num%2:
    print("number is odd")
else:
    print("number is even")


# In[15]:


list = [123, 'xyz', 'ibtasam', 'shibtasam@gmail.com']
print ("First list length : ", len(list))


# In[54]:


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


lis = [10, 20, 50, 30, 40]
print("Largest number in the list is:", max(lis))


# In[28]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i < 5:
        print(i)

