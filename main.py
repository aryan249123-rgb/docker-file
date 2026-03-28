def palandrome(a):
    x=0
    y=len(a)-1

    flag=True
    while(x<=y):
        if(a[x]==a[y]):
            flag=True
        else:
            flag=False
            break
        x=x+1
        y=y-1
    if(flag==True):
        print("array is palandrome")
    else:
        print("not a palandroem")

palandrome([1,2,2,1])






