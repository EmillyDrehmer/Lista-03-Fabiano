import random

temps = [random.randint(0, 15) for _ in range(20)]

for t in temps:
    print(t)
    if t > 10:
        print("Temperatura alta!")