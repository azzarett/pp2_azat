def generator(n):
    for i in range(n, 0-1, -1):
        yield i
        
n = int(input())
list1 = generator(n)
list1 = list(list1)
print(*list1)