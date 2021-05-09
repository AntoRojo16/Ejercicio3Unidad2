import os

class Menu:
    __switcher:None
    
    def __init__(self):
        self.__switcher={ 1: self.opcion1,
                          2: self.opcion2,
                          3: self.opcion3,
                          4: self.salir}
        
    def getSwitcher (self):
        return self.__switcher
    
    def opcion (self,op,cosechas):
        func=self.__switcher.get(op, lambda: print("opcion no valida")) #busco la clve op dentro del diccionario y si no la encuentra devuelve un print
        func(cosechas)
        
    def salir (self,cosechas):
        print ("Salir")
        
    def opcion1 (self,cosecha):
        os.system('cls')
        print("Ingrese el identificador de un camion")
        if (viajeros.buscarViajero(num)==True):
            print("Error el numero ingresado no pertenece a un viajero")
        else:
            i=viajeros.buscarViajero(num)
            viajeros.consultarMillas(i)
            
            
    def opcion2 (self,viajero,num):
        os.system('cls')
        i=viajero.buscarViajero(num)
        if (viajero.buscarViajero(num)==True):
            print("Error el numero ingresado no pertenece a un viajero")
        else:
            j=input("Ingrse la cantidad de millas")
            viajero.acumularMillas(i,j)
            