import os
from manejadorLisBid import MListaBidi
from menuejercicio2 import listaBidi
from ManejadorCamion import Manejador
from claseMenu import Menu
def verificar (j,i):
    if int(j)<46:
        if int(i)<21:
            
            return True
        else:
            print("Se ingreso un dato incorrecto")
            return False
    else:
        print("Se ingreso un dato incorrecto")
        return False
 
def test   ():
    lista=listaBidi() 
    lista.agregarLista(20,45)
    unManejador=Manejador()
    unManejador.testCamion()
    lista.mostrar()  
    print("REALIZAR LA CARGA POR TECLADO")
    valor="si"
    while (valor!="no"):

        i=input("ingrese identificador de camion: ")
        j=input("ingrese dia ")
        k=input("ingrese kilos ")
        if verificar(j, i):
            t=unManejador.buscarCamion(i)
            lista.modificar(t,k,j,i)
        valor=input("Deseas seguir ingresando valores? Ingrese si si desae seguir ingresando valores, o no de lo contrario: ")
    lista.mostrar()
    listaBi=MListaBidi()
    listaBi.testListaBidi(lista,unManejador)
    lista.mostrar()
    menu = Menu()
    salir = False
    while not salir:
        print("\n------------Menu------------\n1. Inciso 1\n2. Inciso 2 \n3. Salir")
        op = int(input('Ingrese una opcion: '))
        os.system('cls')
        menu.opcion(op,lista,unManejador)
        salir = op == 3

    
    
    
if __name__=="__main__":
   test()