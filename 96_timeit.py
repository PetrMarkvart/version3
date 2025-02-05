import timeit

def mocniny():
    for i in range(100000):
        a = i * i

import time
st = time.time()
mocniny()
end = time.time()
print(f"Trvalo to {end-st:.5} sekund")


print(f"Trvalo to {timeit.timeit(mocniny, number=1000)/1000} sekund")