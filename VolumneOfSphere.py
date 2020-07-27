#Write a Python program to find the volume of a sphere with diameter 12 cm.

def VolumeOfSphere(r):
  PI = 3.142
  return (4/3)*PI*Cube(r);

def Cube(r):
  return r*r*r;
  
def radius(d):
    return d/2;

d = 12  
print("The diameter of Sphere : %.i " % d);
r = radius(d)
print("The Volume of Sphere of radius 12 is:  %.6f " % VolumeOfSphere(r));
