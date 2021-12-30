print("Calculadora, eliga una operacion")
print("1  - suma")
print("2  - resta ")
print("3  - Multiplicacion ")
print("4  - Divicion ")

opcion = int(input("ingresar operacion"))

def suma(a, b):
    return(a + b)
    
def resta(a, b):
    return(a - b)
    
def Multiplicacion(a, b):
    return(a * b)
    
def Divicion(a, b):
    return(a // b)

    
    
    
    
if (opcion == 1):
    
    a = int(input("ingrese un numero"))
    b = int(input("ingrese otro numero"))
    print(" El resultado es")
    print(suma(a, b))
    
   

elif (opcion == 2):
     
    a = int(input("ingrese un numero"))
    b = int(input("ingrese otro numero"))
    print(" El resultado es")
    print(resta(a, b))
     
elif (opcion == 3):
     
    a = int(input("ingrese un numero"))
    b = int(input("ingrese otro numero"))
    print(" El resultado es")
    print(Multiplicacion(a, b))


    
    
elif (opcion == 4):
    a = int(input("ingrese un numero"))
    b = int(input("ingrese otro numero"))
    if (b == 0):
        print("no se puede dividir en 0")
    else:
        print(" El resultado es")
        print(Divicion(a, b))
        
else: 
    print("Eliga una operacion del 1 al 4")
    opcion = int(input("ingresar operacion")) 
