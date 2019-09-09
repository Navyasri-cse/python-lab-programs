def uni(a):
    s=set()
    d=set()
    u=set()
    for i in a:
        if i in s:
            d.add(i)
        else:
            s.add(i)
    for i in a:
        if i not in d:
            u.add(i)
    print(u)
uni([1,1,3,4,6,7,6,8])
