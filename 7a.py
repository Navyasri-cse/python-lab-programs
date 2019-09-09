fname=input("enter file name")
fn=open(fname,"r")
for line in fn:
    line2=" "
    for ch in range(len(line)-1,-1,-1):
        line2=line2+line[ch]
    print(line2)
fn.close
