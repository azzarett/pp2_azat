def myfunc(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i

n = int(input())
list1 = myfunc(n)
list1 = list(myfunc(n))
print(f"THIS LIST THAT DIvides by3 or 4-> {list1}")