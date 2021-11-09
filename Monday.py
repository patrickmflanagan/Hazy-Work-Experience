x = 25
y = x*10
print("25 multiplied by 10 is",y)

num = 25

if num>1:

    for i in range(2,num):
        if (num%i) == 0:
            print(num,"is not a prime number")
            print(i,"times",num//i,"is",num)
            break
    else:
         print(num,"is a prime number")

else:
    print(num, "is not a prime number")
