#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np 
import matplotlib.pyplot as plt

f=150 # given force
a1=1.5 # length over bar or collar from A to B
a2=1.5 # FROM  B to C
a3=1.5 # FROM  A to D

Ay=f

Dx=f*(a1+a2)/a3
Mb=Dx*a3

print("Moment at B:",Mb)
print("Vertical Reaction force at A:",Ay) 
print("Horizontal Reaction force at D:", Dx)

#Shear Force 
a=([0,a1+a2,a1+a2,0,0])
b=([0,0,Ay,Ay,0])

#Bending Moment
x=([0,a1,a1,a1+a2,0])
y=([0,Mb/2,-Mb/2,0,0])

fig=plt.subplots(figsize=(12,8)) # to set figure size
plt.grid(True)
plt.xticks(np.arange(0,4,step=0.3)) 
plt.yticks(np.arange(-300,300,step=50))
plt.xlim([0,3])
plt.ylim([-250,250])
plt.fill_between(a,b) #plt.fill used to colour or highlight shear force area
plt.fill_between(x,y) #plt.fill used to colour or highlight benging moment


# In[ ]:




