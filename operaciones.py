from os import system 
class OperasBas: 
    #definicion de las propiedades de la clase.
    num1= 0
    num2=0
    res=0
    #declaració de constructor de la clase. 
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.res = 0

    #declaracion de los metodos de la clase. 
    def suma(self):
        self.res=self.num1+self.num2
        #print("La suma es {}".format(self.res))
        return self.res
    
    def resta(self):
        self.res=self.num1-self.num2
        return self.res
        #print("La resta de {} - {} = {}".format(self.num1, self.num2, self.num3))
    
    def multi(self):
        self.res=self.num1*self.num2
        return self.res
        #print("La multiplicacion es: {} * {} = {}".format(self.num1, self.num2, self.res))
    
    def div(self):
        self.res = self.num1 / self.num2
        return self.res
        #print("La division es: {} / {} = {}". format(self.num1, self.num2, self.res))
    
def main():

    obj=OperasBas
    op=0

    while op!=5:
        system('cls')
        print("Seleccione la operacion a realizar\n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n 5.Salir")
        op=int(input("Opcion: "))
        if op==5:
            break
        obj.num1=int(input("n1 "))
        obj.num2=int(input("n2 "))
        if op==1:
            print("La suma es:", obj.suma())
            
        if op==2:
            print("La resta es:", obj.resta())
            
        if op==3:
            print("La multiplicación es:", obj.multi())
        
        if op==4:
            obj.div()
            print("La división es:", obj.div())

        input()
#comentario

if __name__=="__main__":
    main()
