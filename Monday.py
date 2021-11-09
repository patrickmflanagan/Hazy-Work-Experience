#Multiplication formula using x and y variables
x = 25
y = x*10
print("25 multiplied by 10 is",y)



#Testing if a number is Prime
num = 25
#Prime numbers must be greater than 1
#if...else function used to state numbers less than 1 are not Prime
if num>1:
    #for...else function used to create loop testing for factors
    #Prime condition is met when no factors are found
    for i in range(2,num):
        if (num%i) == 0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
            break
    else:
         print(num,"is a prime number")

else:
    print(num, "is not a prime number")
