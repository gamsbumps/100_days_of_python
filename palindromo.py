palindromo = 195
contador = 0
while True:
    #convertendo para string para que eu possa inverter.
    string = str(palindromo)
    if string == string[::-1]:
        break
    else:
        palindromo_invertido = int(string[::-1])
        palindromo += palindromo_invertido
        contador += 1

print(f'{contador}, {palindromo}') 
        