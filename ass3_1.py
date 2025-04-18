n=int(input("enter a number :"))

def fact(n):
    if(n<0):
        return "error"
    elif(n==0 or n==1):
        return 1
    else:
        return n * fact(n - 1)

result=fact(n)
print("factorial of",n,"is :",result)


