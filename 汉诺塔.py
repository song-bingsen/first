def han(n,p1,p2,p3):
    if n==0:
        return
    han(n-1,p1="A",p3="C",p2="B")
    print(f"{p1}->{p3}")
    han(n-1,p2="B",p1="A",p3="C")
han(5,"A","B","C")