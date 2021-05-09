import os

class Menu:
    __switcher:None
    
    def __init__(self):
        self.__switcher={ 1: self.opcion1,
                          2: self.opcion2,
                          3: self.salir}
        
    def getSwitcher (self):
        return self.__switcher
    
    def opcion (self,op,cosechas,camiones):
        func=self.__switcher.get(op, lambda: print("opcion no valida")) #busco la clve op dentro del diccionario y si no la encuentra devuelve un print
        func(cosechas,camiones)
        
    def salir (self,cosechas,camiones):
        print ("Salir")
        
    def opcion1 (self,cosecha,camiones):
        os.system('cls')
        i=int(input("Ingrese el identificador de un camion"))
        if i in range(21):
            cosecha.totalkilos(i)
        else:
            print("Los datos ingresados son incorrectos")
            
            
    def opcion2 (self,cosecha,camiones):
        os.system('cls')
        i=int(input("Ingrese un dia"))
        if i in range(46):
            cosecha.mostrarformato(i,camiones)
        else:
            print("Los datos ingresados son incorrectos")