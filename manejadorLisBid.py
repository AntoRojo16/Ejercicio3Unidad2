import csv
from menuejercicio2 import listaBidi
from ManejadorCamion import Manejador
class MListaBidi:
    
    def __init__ (self):
        self.__MListaBidi=[]
        
    def agregar (self,kilos):
        self.__MListaBidi.append(kilos)
    def testListaBidi (self,lista,lC):
        archivo=open("cosecha.csv")
        reader=csv.reader(archivo,delimiter=";")
        #lista=listaBidi()
        #lC=Manejador()
        band=True
        for fila in reader:
            if (band):
                band=not band
            else:
                x=fila[0]
                print(x)
                y=int(fila[1])
                print(y)
                z=int(fila[2])
                print(z)
                t=lC.buscarCamion(x)
                print("tara"+str(t))
                lista.modificar(t,z,y,x)
                self.agregar(t)
        archivo.close()
            

                