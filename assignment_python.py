#!/usr/bin/env python
# coding: utf-8

# #Fibonacci
# 

# In[6]:


n = int(input("number "))

n1, n2 = 1, 2
count = 1

if n <= 1:
   print("p integer")
elif n == 2:
   print("Fibonacci ",n,":")
   print(n1)
else:
   print("Fibonacci :")
  


# #2) Write a function that will take a given string and reverse the order of the words. 
# 
# 

# In[30]:


string=("Hello world")
s=string.split()[:-1]
l=[]

for i in s:
    l.append(i)
print(" ".join(1))


# 3) Write a function, primeNumberDetector, that tests if a number, n is a prime number.
# 
# 

# In[29]:


num = 3
if num >1:
    for i in range(2,(num%2)+1):
        if (num %i) ==0:
            print(num,"not prime number")
            
    else:
        print(num,"prime number")


# In[ ]:





# In[ ]:




