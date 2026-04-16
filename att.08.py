import random

pressao = [random.randint(50, 150) for _ in range(20)]

for p in pressao:
    print(p)
    if p < 70 or p > 120:
        print("Pressão fora do normal!")