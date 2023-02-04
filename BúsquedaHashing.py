
class hashTabla:
    def __init__(self):
        self.tabla = [None] * 127

    # Función hash
    def Hash_func(self, value):
        suma = 0
        for pos in range(0 ,len(value)):
            suma += ord(value[pos])
        return suma % 127

    def Insertar(self, valor):  # Metodo para ingresar elementos
        hash = self.Hash_func(valor)
        if self.tabla[hash] is None:
            self.tabla[hash] = valor

    def Buscar(self ,valor): # Metodo para buscar elementos
        hash = self.Hash_func(valor);
        if self.tabla[hash] is None:
            return False
        else:
            return True

    def Remover(self ,valor): # Metodo para eleminar elementos
        hash = self.Hash_func(valor);
        if self.tabla[hash] is None:
            print("No hay elementos con ese valor", valor)
        else:
            print("Elemento con valor", valor, "eliminado")
            self.tabla[hash] is None;


H = hashTabla()
H.Insertar("A")
H.Insertar("B")
H.Insertar("C")
print(H.Buscar("A"))
