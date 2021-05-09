from ManejadorCamion import Manejador
class listaBidi:

    def __init__ (self):
        self.__lista=[]
        
    def agregarLista (self, columnas, filas):
        for i in range(filas):
            self.__lista.append([0]*columnas)
        
            
    def modificar (self,tara,kilos,dia,iden):
        tot=int(kilos)-int(tara)
        self.__lista[int(dia)-1][int(iden)-1]=self.__lista[int(dia)-1][int(iden)-1]+int(tot)
        
    def mostrar (self):
        for fila in self.__lista:
            print (fila)
        
    def totalkilos (self,i):
        acu=0
        lon=len(self.__lista)
        print("long"+str(lon))
        for j in range(lon):
            acu=acu+self.__lista[j][i]
        print (acu)
        
    def mostrarformato (self,j,unManejador):
        lon=len(self.__lista[j])
        i=0
        print("long"+str(lon))
        print ("CONDUCTOR   PATENTE   KILOS")
        for i in range(lon):
            unManejador.mostrarCosas(int(i))
            print ("{:>5}".format(self.__lista[int(j)][int(i)]))