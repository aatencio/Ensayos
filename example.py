class Estudiante:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hola(self):
        return "Mi nombre es %s" % self.nombre

e = Estudiante("Andres", 37)
e2 = Estudiante("Moraines", 34)

print e.hola()

print e2.hola()
