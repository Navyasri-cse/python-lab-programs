fname=input("enter file name")
fn=open(fname,"r")
c=w=l=0
for line in fn:
    l=l+1
    words=line.split()
    for word in words:
        w=w+1
        for ch in word:
            c=c+1
print("number of line=",l)
print("number of words=",w)
print("number of charecters=",c)
fn.close()
