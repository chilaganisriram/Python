#leap year

def Isaleapyear(n):
    if (n%4==0 and n%100!=0) or (n%400==0):
        return  "It is a leap year"
    else:
        return  "Not a leap year"

print(Isaleapyear(1900))

#24-02-25

N=int(input("enter the number"))
for i in range(21):
    print(N,"*",i,"=",N*i)
    
#2
# num=int(input())
fac=1
while num!=1:
    fac=fac*num
    num=num-1
print(fac)

#3
for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)