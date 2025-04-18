import math
num=int(input("Enter a  number :"))

if(num>0):
    square_root=math.sqrt(num)
    print("square root of ",num,"is :",square_root)

    logarithm=math.log(num)
    print("Natural logarithm of",num,"is:",logarithm)

    sine=math.sin(num)
    print("sine of",num,"in radian is :",sine)

else:
    print("Please enter positive number")





