import os
class Archivo:
    def __init__(self):
        self.lista = []

    def iniciarArchivo(self):
        archivo = open("agenda.txt", "a")
        archivo.close()

    def escribirArchivo(self):
        archivo = open("agenda.txt", "w")
        self.lista.sort()
        for elemento in self.lista:
            archivo.write(elemento + "\n")
        archivo.close()

    def cargarAgenda(self):
        archivo = open("agenda.txt", "r")

        linea = archivo.readline()
        if linea:
            while linea:
                if linea[-1] == '\n':
                    linea = linea[:-1]
                    self.lista.append(linea)
                    linea = archivo.readline()
                archivo.close()

    def crearContacto(self):
        nombre = input("escribe tu nombre: ")
        telefono = input("Escribe el teléfono de " + str(nombre) + " : ")
        correo = input("Escribe el correo de " + str(nombre) + " : ")
        self.lista.append(nombre + "$" + telefono + "$" + correo)

    def imprimirContacto(self):
        self.lista.sort()

        for elemento in self.lista:
            arreglo = elemento.split('$')
            print("Nombre: " + arreglo[0] + "\t Teléfono: " + arreglo[1] + "\t Correo: " + arreglo[2])
            print("*******************************")

def buscarContacto(self):
    nombre = input("Inserta el nombre a buscar: ")
    Noencotrado = True
    for elemento in self.lista:
        arreglo = elemento.split('$')
    if nombre in arreglo[0]:
        print("Nombre: " + arreglo[0] + " Teléfono: " + arreglo[1] + " Correo: " + arreglo[2])
    print("*******************************")
    Noencotrado = False
    if Noencotrado == True:
        print("Contacto no encontrado")

    def eliminarContacto(self):
        nombre = input("Inserta el nombre a eliminar: ")

    Noencontrado = True
    for elemento in self.lista:
        arreglo = elemento.split('$')
    if nombre in arreglo[0]:
        self.lista.remove(elemento)
    Noencontrado = False
    if Noencontrado == True:
        print("Contacto no encontrado")


archivo = Archivo()
archivo.iniciarArchivo()
archivo.cargarAgenda()
while True:
    os.system('cls')
    print("1.- Escribir contacto")
    print("2.- Lee contactos")
    print("3.- Buscar contacto")
    print("4.- Eliminar contacto")
    print("5.- salir contacto")
    try:
        opcion = int(input("Inserte la opción a elegir: "))
    except:
        print("Opción no valida")
    os.system('pause')
    continue
    if opcion == 1:
        archivo.crearContacto()
    elif opcion == 2:
        archivo.imprimirContacto()
    elif opcion == 3:
        archivo.buscarContacto()
    elif opcion == 4:
        archivo.eliminarContacto()
    elif opcion == 5:
        archivo.escribirArchivo()
    break
else:
    print("Opción no valida")
os.system('pause')