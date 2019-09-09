a=0
b=1
sum=0
for i in range(1,4000000):
    c=a+b
    if(c<4000000):
        if(c%2==0):
            sum=sum+c;
        a=b
        b=c
print("sum is--->",sum)
