def mutate(w):
    out_list=[]
    letters="abcdefghijklmnopqrstuvwxyz"
    for i in range(len(w)+1):
        for j in range(26):
            out_list.append(w[:i]+letters[j]+w[i:])
    for i in range(len(w)):
        out_list.append(w[:i]+w[i+1:])
    for i in range(len(w)):
        for j in range(26):
            out_list.append(w[:i]+letters[j]+w[i+1:])
    return out_list
def nearlyequal(w1,w2):
    return w1 in mutate(w2)
print(nearlyequal("welcome","welcom"))
