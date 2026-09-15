def encontrar_numero(lista, num):
    inicio = 0
    final = len(lista) - 1
    
    for i in range(len(lista)):
        medio = (inicio + final) // 2
        
        if lista[medio] == num:
            return medio
        elif lista[medio] < num:
            inicio = medio + 1
        else:
            final = medio - 1
        
        if final < inicio:
            break
    
    return -1

numeros = [4, 5, 10, 20, 25, 30, 35, 40, 45, 50, 58, 65, 80, 98]
print("Numeros:", numeros)
num = int(input("Numero a buscar: "))
pos = encontrar_numero(numeros, num)

if pos != -1:
    print(f"Encontrado en la posicion {pos}")
else:
    print("No existe el numero")