##leap year

def Isaleapyear(n):
    if (n%4==0 and n%100!=0) or (n%400==0):
        return  "It is a leap year"
    else:
        return  "Not a leap year"

print(Isaleapyear(1900))