
#Write a Python program to accept the user's first and last name and then getting them
#printed in the the reverse order with a space between first name and last name.

fname = input("Enter first name : ")
space = " "
lname = input("Enter last name : ")
name = fname + space + lname
print("Your full name is : {0}".format(name))

def ReverseName(n) :
    rev = ""
    for i in n:
        rev = i + rev
    return rev;
    
print("{0} in reverse order : ".format(name),end="") 
print (ReverseName(fname),ReverseName(lname), sep=' ')
