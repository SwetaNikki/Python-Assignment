#Write a program which will find all such numbers which are divisible by 7 but are not a
#multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed
#in a comma-separated sequence on a single line.

 
a = []
def mul():
    for i in range(2000,3201):
        if (i%7==0) and (i%5!=0):
            a.append(str(i))

print ("The number numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 are : ")
mul()
print (','.join(a))
