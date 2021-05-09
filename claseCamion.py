class Camion:
    __ident=0
    __nombre=""
    __patente=""
    __marca=""
    __tara=""
    
    def __init__ (self,i,n,p,m,t):
        self.__ident=i
        self.__nombre=n
        self.__patente=p
        self.__marca=m
        self.__tara=t
        
    def getiden (self):
        return self.__ident
    
    def getnom (self):
        return self.__nombre
    
    def getpaten (self):
        return self.__patente
    
    def gtemarca (self):
        return self.__marca
    
    def gettara (self):
        return self.__tara
    
    def __str__ (self):
        return "%s %s %s %s %s" % (self.__ident, self.__nombre, self.__patente, self.__marca, self.__tara)
    