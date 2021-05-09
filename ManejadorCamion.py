import csv
from claseCamion import Camion
class Manejador:
    
    def __init__ (self):
        self.__lista=[]
        
    def agregarCamion (self,unCamion):
        self.__lista.append(unCamion)
    
    #def mostrarelemento (self):
     #   print(self.__lista[0])
        
    
    def testCamion (self):
        archivo=open("Camion.csv")
        reader=csv.reader(archivo,delimiter=";")
        bandera=True
        for fila in reader:
            if bandera:
                bandera=not bandera
            else:
                ide=int(fila[0])
                nom=fila[1]
                pat=fila[2]
                marca=fila[3]
                tara=fila[4]
                unCamion=Camion(ide,nom,pat,marca,tara)
                self.agregarCamion(unCamion)
                #self.mostrarelemento()
        archivo.close()
                
    def mostrarlista (self):
        #i=0
        for fila in self.__lista:
            print (fila)
        
                
                
    def buscarCamion (self, i):
        print(i)
        unCamion=self.__lista[int(i)-1]
        tara=unCamion.gettara()
        return tara
    
    def mostrarCosas(self,i):
        unCamion=self.__lista[int(i)]
        conductor=unCamion.getnom()
        pa=unCamion.getpaten()
        #print (conductor, end=" ")
        print ("{:<12}{}".format(conductor, pa),end="")
            