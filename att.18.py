dados = [10, 12, 11, 50, 13]

for i in range(len(dados)-1):
    if abs(dados[i] - dados[i+1]) > 20:
        print("Anomalia detectada!")