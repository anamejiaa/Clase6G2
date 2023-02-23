class Mascota:
    
    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__medicamento=[]

    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def ver_Medicamento(self):
        return self.__medicamento
    
    def eliminarMedicamento(self, nommed):
        self.medicamento.remove(nommed)
    
            
    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_medicamento(self,n):
        self.__medicamento = n 


class sistemaV:
    def __init__(self):
        self.__lista_caninos = {}
        self.__lista_felinos= {}
        # self.__lista_mascotas = {}

    def verificarExiste(self,historia):
        if historia in self.__lista_caninos:
            if historia == m.verHistoria():
                return True
        elif historia in self.__lista_felinos:
            return
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False

    def verNumeroCaninos(self):
        return len(dict.keys(self.__lista_caninos))
    
    def verNumeroCaninos(self):
        return len(dict.keys(self.__lista_felinos))

    def ingresarMascota(self,tipo, mascota, historia):
        if tipo == 1:
            self.__lista_caninos[historia]=mascota
        elif tipo== 2:
            self.__lista_felinos[historia]=mascota

        # self.__lista_mascotas[mascota.verHistoria()]=mascota

    def verFechaIngreso(self,historia):

        if (historia in self.__lista_caninos):
            return self.__lista_caninos[historia].verFecha()
        if (historia in self.__lista_felinos):
            return self.__lista_caninos[historia].verFecha()

        #busco la mascota y devuelvo el atributo solicitado

        #for masc in self.__lista_mascotas:
         #   if historia == masc.verHistoria():
          #      return masc.verFecha() 
        #return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
        if historia in self.__lista_caninos:
                return self.__lista_caninos[historia].ver_Medicamento() 
        
        if historia in self.__lista_felinos:
                return self.__lista_felinos[historia].ver_Medicamento()
         
        return None
    

    #def eliminarMedicamento(self, historia):
        

    def eliminarMascota(self, historia):
        if historia in self.__lista_caninos:
            del self.__lista_caninos[historia]
            return True

        if historia in self.__lista_felinos:
            del self.__lista_felinos[historia]
            return True
        return False 


class Medicamento: #Está para un solo medicamento
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 
    
    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 
    
    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 
        