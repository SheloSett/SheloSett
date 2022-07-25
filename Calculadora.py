def suma(a,b):
    return a + b
    
def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def divicion(a,b):
    return a // b

def menu():
    bandera = False
    while bandera == False:
        print("1- suma")
        print("2- resta")
        print("3- multiplicacion")
        print("4- divicion")
        print("5- salir")
        seleccion = int(input("seleccione una opcion del 1 al 5: "))


        if seleccion == 1:
            a = int(input("seleccione un valor: "))
            b = int(input("seleccione otro valor: "))
            print("el resultado de la operacion es",suma(a,b))
            print(menu())
    
        elif seleccion == 2:
            a = int(input("seleccione un valor: "))
            b = int(input("seleccione otro valor: "))
            print("el resultado de la operacion es",resta(a,b))
            print(menu())
     
        elif seleccion == 3:
            a = int(input("seleccione un valor: "))
            b = int(input("seleccione otro valor: "))
            print("el resultado de la operacion es",multiplicacion(a,b))
            print(menu())
        
        elif seleccion == 4:
            a = int(input("seleccione un valor: "))
            b = int(input("seleccione otro valor: "))
            print("el resultado de la operacion es",divicion(a,b))
            print(menu())
        
        elif seleccion == 5:
            bandera = True
        return ""    
print(menu())    
