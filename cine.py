from io import open

class cine:
    def __init__(self):
        self.name = ""
        self.numPersonas = 0
        self.numBoletos = 0
        self.tarjeta=""
        self.total = 0

    def totalInicial(self):
        precio = 12

        if self.numPersonas == 1 and self.numBoletos > 7:
            raise ValueError("Una sola persona no puede comprar más de 7 boletos")
        
        if self.numBoletos < 3:
            if self.tarjeta == "No Tarjeta":
                self.total = (self.numBoletos * precio)
        
            if self.tarjeta == "Si Tarjeta":
                self.total = (self.numBoletos * precio)
                self.descuento = (self.total * 0.10)
                self.total = (self.total - self.descuento)

        elif self.numBoletos >= 3 and self.numBoletos <= 5:
            self.total = self.numBoletos * precio
            self.descuento = self.total * 0.10

            if self.tarjeta == "No Tarjeta":
                self.total = self.total - self.descuento

            if self.tarjeta == "Si Tarjeta":
                self.descuento1 = (self.total - self.descuento) * 0.10
                self.total = (self.total - self.descuento) - self.descuento1
        
        elif self.numBoletos > 5:
            self.total = self.numBoletos * precio
            self.descuento = self.total * 0.15

            if self.tarjeta == "No Tarjeta":
                self.total = self.total - self.descuento

            if self.tarjeta == "Si Tarjeta":
                self.descuento1 = (self.total - self.descuento) * 0.10
                self.total = (self.total - self.descuento) - self.descuento1
    
    def agregarCompra(self):
        with open("archivo1.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"{self.name},{self.numPersonas},{self.numBoletos},{self.tarjeta},{self.total}\n")

    @staticmethod #solo acciones de lectura
    def buscarCompra():
        compras = []
        with open("archivo1.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                partes = linea.strip().split(",")
                if len(partes) == 5:
                    name, numBoletos, numPersonas, tarjeta, total = partes
                    compras.append((name, numBoletos, numPersonas, tarjeta, total))
        return compras

#comentario

'''def guardarInformacion(self, numBoletos, total, name, tarjeta, numPersonas):
    self.numBoletos = numBoletos
    self.total = total
    self.name = name
    self.tarjeta = tarjeta
    self.numPersonas = numPersonas
'''
