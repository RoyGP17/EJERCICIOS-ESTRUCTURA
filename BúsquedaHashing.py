
class hashTabla():
    def __int__(self):
        self.tabla = [None]*127  # <---- El tamaño de mi tabla

    def FuncHash(self, valor):
        suma = 0
        for pos in range(0,len(valor)):
            suma = suma + ord(valor[pos])

        return suma % 127
    def Incertar(self,valor):
         hash = self.FuncHash(valor)
         if self.tabla[hash] is None:
             self.tabla[hash] = valor
    def Buscar(self,valor):
        hash = self.FuncHash(valor);
        if self.tabla[hash] is None:
            return None
        else:
            return hex(id(self.tabla[hash]))
    def Remover(self,valor):
        hash = self.FuncHash(valor);
        if self.tabla[hash] is None:
            print("No hay elmentos en ese valor", valor)
        else:
            print("Elemento con valor", valor, "eleminado")
            self.tabla[hash] is None;


### Inicializando

H = hashTabla()
H.Incertar("A")
H.Incertar("B")
H.Incertar("C")

print(H.Buscar("B"))

