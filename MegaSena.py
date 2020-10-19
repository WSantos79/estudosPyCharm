'''for dez1 in range(60):
    for dez2 in range(dez1 + 1, 60):
        for dez3 in range(dez2 + 1, 60):
            for dez4 in range(dez3 + 1, 60):
                for dez5 in range(dez4 + 1, 60):
                    for dez6 in range(dez5 + 1, 60):
                        print(dez1 + 1, dez2 + 1, dez3 + 1, dez4 + 1, dez5 + 1, dez6 + 1)'''

total = 0
for dez1 in range(60):
    for dez2 in range(dez1 + 1, 60):
        for dez3 in range(dez2 + 1, 60):
            for dez4 in range(dez3 + 1, 60):
                for dez5 in range(dez4 + 1, 60):
                    for dez6 in range(dez5 + 1, 60):
                        total += 1
print(total)