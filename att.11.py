valores = [10, 20, 90, 85, 30]

falhas = 0

for v in valores:
    if v > 80:
        print("Alarme!")
        falhas += 1

print("Total de falhas:", falhas)