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
num=int(input())
fac=1
while num!=1:
    fac=fac*num
    num=num-1
print(fac)

#3
for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)
        
#1. The Ticket Machine (If-Else & Number System)
age = int(input("enter the age"))
 
if age<10:
    print("free ticket price")
elif(age>=10 and age<=18):
    print("50% discount")
elif(age>=60):
    print("30% discount")
else:
    print("Pay full price $10")
    
# 2. The Festival Discount (Number System & If-Else)
digit = int(input("enter the last digit "))
 
if digit%2==0:
    print("discount 10%")
elif digit%2!=0:
    print("discount 15%")
elif digit==0:
    print("discount 20%") 

#  3. The Bank Account Pin (Number System & Loops)
PIN = 1234
pincode= int(input("enter the PIN"))
attempt = 3
if PIN == pincode:
    print("get access")
while PIN != pincode:
    attempt-=1
    if attempt>=0:
        pincode= int(input("enter the PIN"))
    if attempt == 0:
        print("account blocked")
        break

# 4. Print all prime numbers in a given range – min number and max number

min=int(input("enter the min value-"))
max=int(input("enter the max value-"))

def checkprime(num):
    if num==0 or num==1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            return False
            # break
    
    return True

for j in range(min,max+1):
    if checkprime(j):
        print(j,"is prime")


#5
n=int(input("enter the number"))
budget=0
for i in range(n):
    if i%2==0:
        budget=budget+i*1000
print(budget)

#05-03-25

# 1. Find the sum of odd digits in a given number

def sum_odd(num):
    sum=0
    while num!=0:
        digit=num%10
        if digit%2!=0:
            sum+=digit
        num=num//10
    return sum

print(sum_odd(146))

# 2. Print all the Armstrong numbers in given range

def armstrong_number(num):
    sum=0
    temp=num
    while temp!=0:
        digit = temp%10
        sum+=digit**len(str(num))
        temp=temp//10
    if sum==num:
        return True
    else:
        return False
start=int(input("enter the first num"))
end=int(input("enter the end num"))

for i in range(start,end+1):
    if armstrong_number(i):
        print(i)

# 3. Find the smallest prime digit in a given number

number=int(input("enter the number"))
small=float("inf")
while num!=0:
    digit=num%10
    if checkprime(digit):
        small=min(small,digit)
    num=num//10

print(small)
        
        
        
    
    
    






