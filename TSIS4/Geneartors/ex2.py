def generator(n):
    for i in range(n+1):
        if i%2 == 0:
            yield i
            
n = int(input())
list1 = ', '.join(map(str, generator(n)))
print(f"even number in range from 0 to {n}-> {list1}")