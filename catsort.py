import random
import time


def catsort(L):
    while L != sorted(L):
        i = int(len(L)*random.random())
        
        if i == 0:
            L[i], L[i+1] = L[i+1], L[i]
        
        elif i == len(L) - 1:
            L[i], L[i-1] = L[i-1], L[i]
        
        else:
            mood = random.randint(-1, 1)
            if mood != 0:
                L[i], L[i + mood] = L[i + mood], L[i]

    return L


sizes = range(1, 14)

attempts = 100

print('elements(n), time(s)')
for size in sizes:
    times = []
    for _ in range(attempts):
        l = list(range(size))
        random.shuffle(l)

        
        start_time = time.time()
        catsort(l)
        times.append((time.time() - start_time))
    avg = sum(times) / len(times)
    print("%d, %.8f" % (size, avg))
    
