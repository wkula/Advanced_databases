# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 11:17:19 2020

@author: wkula
"""

import math

d = math.sqrt(10)

print(d)
print("%1.3f"%d)
print("%1.20f"%d)

h=33
r=17
S=h*r*r*math.pi

print(S)

"""
Multiline comments
"""


def function(x,t,r):
    B=((x+t)/(r*math.sin(2*x)+3.3456))*x**(t*r)
    return B

print("Result of function",function(10,3,5))

import numpy as np

a = math.sqrt(2)

M=np.array([[a,1,-a],[0,1,1],[-a,a,1]])
Minv=np.linalg.inv(M)
Mt=np.transpose(M)
Mdet=np.linalg.det(M)

print(M,Minv,Mt,Mdet)

print(M[0,0],M[2,2],M[2,1])

w1=M[:,2]
w2=M[1,:]

print("W1",w1)
print("W2",w2)

polynomial=[1,-7,-3,-43,-28,-60]
print(np.roots(polynomial))

list_arange=np.arange(1,51,1)
list_linspace=np.linspace(1,50,50)
print(list_arange)
print(list_linspace)

"""
arange need step as parameter, when linspace need number of steps
also linspace create by defoult floating point table
"""

def fun1(x):
    return x**2 -3*x-2 + 1

import matplotlib.pyplot as plt

x = np.linspace(-10,10)
y=fun1(x)
plt.plot(x,y)
plt.title('Example chart')
plt.xlabel('x')
plt.ylabel('y')
plt.legend('Charte 1')
plt.show()

m=2500
v=60
def heat(m,v):
    q=(m*v**2)/2
    return q,q/4.184

kcal,j=heat(m,v)

plt.figure()
vel = np.linspace(200,0)
mass=3000
Kcal,J = heat(mass,vel)
plt.plot(vel,Kcal)
plt.xlim([200,0])
plt.semilogy()
plt.show()

class Animal:
    def __init__(self, kind, place):
        self.kind = kind
        self.place = place
        
animal1 = Animal('Dog','whole world')
print('The {0} is living in {1}'.format(animal1.kind, animal1.place))

animal2 = Animal('Dog',['Africa','Asia','Europ','America','Australia'])
print('The {0} is living in {1}'.format(animal2.kind, animal2.place))

from numpy import random

class Animal:
    
    def __init__(self, kind, place):
        self.kind = kind
        self.place = place
        
    @classmethod
    def general_info(self):
        print('The {0} is living in {1}'.format(self.kind, self.place))
        
class Dog(Animal):
    
    def __init__(self, name, species, place):
        self.name = name
        self.species = species;
        Animal.__init__(self, 'Dog', place)
    
    def general_info(self):
        print('{0} is the {1} species {2} is living in {3}'.format(self.name, self.kind, self.species, self.place))
    
    @staticmethod
    def make_sound():
        print()
        for i in range(1,random.randint(2,10,size = 1)[0]):
            print('Hau')
            
dog = Dog('Ales','Terrier','Boston')
dog.general_info()
dog.make_sound()



























