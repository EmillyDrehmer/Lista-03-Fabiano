import random

phs = [round(random.uniform(4, 10), 1) for _ in range(20)]

for ph in phs:
    print(ph)
    if ph < 6 or ph > 8:
        print("pH fora do ideal!")