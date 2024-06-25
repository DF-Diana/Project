from io import open

class traductorIngEsp:
    word1 = ""
    word2 = ""

class traductorIngEsp:
    def __init__(self):
        self.word1 = ""
        self.word2 = ""

    def guardarWord1(self, word1):
        self.word1 = word1

    def guardarWord2(self, word2):
        self.word2 = word2

def buscarPalabra():
    palabras = {}
    with open("archivo.txt", "r", encoding="utf-8") as archivo:
        for linea in archivo.readlines():
            espanol, ingles = linea.strip().split(",")
            palabras[espanol] = ingles
            palabras[ingles] = espanol
    return palabras
#comentario de cambio 
def agregarPalabra(espanol, ingles):
    with open("archivo.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{espanol},{ingles}\n")
