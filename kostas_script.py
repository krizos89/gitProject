import sys

sys.path.insert(1,'C:/Users/ri_ko/Desktop/Modules')
import my_math
import numpy as np

x = int(input("Enter a value for x: "))
y = int(input("Enter a value for y: "))

vec1 = np.array([x,y])
vec2 = np.array([-x,-y])

def add(a,b):
    return a + b

def mult(a,b):
    return a * b

def dot(a,b):
    return a[0]*b[0] + a[1]*b[1]

answer1 = my_math.add(x,y)
answer2 = my_math.mult(x,y)
answer3 = my_math.dot(vec1,vec2)

print (answer1)
print (answer2)
print (answer3)