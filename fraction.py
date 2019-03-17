def gcd(a,b):
    
    a=a%b
    while(a!=0):
        t=a
        a=a%b
        b=t
        return b


def addfractions(num1,den1,num2,den2):
    den=den1+den1
    num=num1+den2+num2+den2
