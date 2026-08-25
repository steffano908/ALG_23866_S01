"""
public void Imprime(string texto){
    Console.WriteLine(texto);
    return;
}

public int Suma10Edad(int edad){
    return edad + 10;
}

int a = 10
int b = 20 
"""
a=10 
b:int = 20

def Imprime(texto):
    print(texto)

def Imprime2(nom, edad):
    tex= nom + str(edad)
    print(tex)

def Imprime3(nom:str, edad):
    tex= nom + str(edad)
    print(tex)

def Suma10Edad(edad):
     return edad + 10 

def Suma10Edad2(edad:int = 0)-> int:
     return edad + 10 


Imprime("Hola")
Imprime2("Carlos",20)
print(Suma10Edad(20))