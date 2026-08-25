""""
#Actividad 1 
horas = float(input("Ingrese horas trabajadas: "))
valor = float(input("Ingrese valor por hora: "))

Suelbruto = horas * valor
descuento = Suelbruto * 0.05
neto = Suelbruto - descuento

print("Sueldo bruto: S/.", Suelbruto)
print("Descuento AFP: S/.", descuento)
print("Sueldo neto: S/.", neto)
"""
"""# Actividad 2
print("Ingrese votos (1,2,3,4) - 0 para terminar")

c1=0
c2=0
c3=0
c4=0
total=0

while True:
    voto = int(input("Voto: "))
    
    if voto == 0:
        break
    elif voto == 1:
        c1 = c1 + 1
        total = total + 1
    elif voto == 2:
        c2 = c2 + 1
        total = total + 1
    elif voto == 3:
        c3 = c3 + 1
        total = total + 1
    elif voto == 4:
        c4 = c4 + 1
        total = total + 1
    else:
        print("Voto invalido")

# Resultados
print("\nRESULTADOS")
print("Candidato 1:", c1, "votos -", (c1*100)/total, "%")
print("Candidato 2:", c2, "votos -", (c2*100)/total, "%")
print("Candidato 3:", c3, "votos -", (c3*100)/total, "%")
print("Candidato 4:", c4, "votos -", (c4*100)/total, "%")
print("Total votos:", total)
"""
"""
#actividad 3 
print("Calcular serie")
print("1 + X + X^2/2! + X^3/3! + ...")

X = float(input("Dame X: "))
N = int(input("Dame N: "))

suma = 1  
factorial = 1
potencia = 1

for i in range(1, N):
    potencia = potencia * X
    factorial = factorial * i
    termino = potencia / factorial
    suma = suma + termino
    print("Termino", i+1, "=", termino)
print("Suma final =", suma)
"""