#Clase Padre
class Mamiferos:
    #Atributos
    #Métodos
    def descripcion(self):
        print("Son todos aquellos que necesitan de la mama de la madre.")

#Clase hijo
class Tigre(Mamiferos):
    #atributos
    pelaje="Naranja con rayas"
    #Métodos
    def carnivoro(self):
        print("El tigre come carne")
        self.descripcion()

mensaje=Tigre()
mensaje.carnivoro()
