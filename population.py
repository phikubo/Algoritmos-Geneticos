print("Algoritmos Geneticos")
'''Adapcion por PHIKUBO'''
import random
import time
from random import randint

class individuo:
    def __init__(self):
        #self.tamanoGen=4
        #--------------------------------------->CAMBIAR TAMAÑO CON GLOBAL gen maximo
        global cadenaGen
        self.tamanoGen=len(cadenaGen)
        self.genes=bytearray(self.tamanoGen)
        self.fitness=0
    #crea una cadena de bits para un individuo.
    def crearGenes(self):
        for i in range(self.tamanoGen):
            self.genes[i]= randint(0,1)

    def cambiarTamano(self,tamano):
        self.tamanoGen=tamano
        self.genes=bytearray(self.tamanoGen)
    
    def genTamano(self):
        return len(self.genes)
    
    #logica de seleccion
    def obtenerValorFit(self):
        global calculadora
        if 'calculadora' in globals():
            if self.fitness==0:
                self.fitness=calculadora.calcular_fitness(self.genes)
            return self.fitness
        else:
            #Solo para pruebas, por que esto es implementado por si.
            calculadora=calculadora_fitnnes()
            if self.fitness==0:
                self.fitness=calculadora.calcular_fitness(self.genes)
            return self.fitness
        #---------------------------------------------------------------------->GLOBAL CALCULADORA
       

class poblacion:   
    def __init__(self, sizePoblacion,inicializar):
        self.tamanoPoblacion=sizePoblacion
        self.inicializar=inicializar
        self.individuos=[]
        if inicializar:
            for i in range(self.tamanoPoblacion):
                self.obj=individuo()
                self.individuos.append(self.obj)
                self.individuos[i].crearGenes()            
        else:
            for i in range(self.tamanoPoblacion):
                self.obj=individuo()
                self.individuos.append(self.obj)

    def encontrar_fittest(self):
        #loop en individuos con el valor de fittest para encontar el fittest
        primerFit=self.individuos[0]
        for i in self.individuos:
            #Se referencia el primer elemento de todos los individuos.
            if primerFit.obtenerValorFit() <= i.obtenerValorFit():
                primerFit=i
            else:
                pass
        return primerFit #objeto individuo


class calculadora_fitnnes:
    def __init__(self):
        self.tamanoGen=4
        self.solucion = bytearray(self.tamanoGen)
        #No es necesario el parametro anterior because python. Resulta que si era necesario lol
    '''se valida que hayan solo unos y ceros y si hay otra cosa, se remplaza por cero'''    
    def crear_gen_maximo(self, nuevaSolu):
        print("crear_gen_maximo")
        self.solucion=bytearray(len(nuevaSolu))
        for i in range(len(nuevaSolu)):
            if nuevaSolu[i]=='0' or nuevaSolu[i]=='1':
                caracter=nuevaSolu[i]
                self.solucion[i]=int(caracter)
            else:
                self.solucion[i]=0
            time.sleep(0.1)
        #return self.solucion
        print(self.solucion)

    def calcular_fitness(self, indivGenes):
        '''Fitness es un numero de etiqueta de un individuo, dice que tan parecido es al resultado que buscamos'''
        fitness=0
        for i in range(len(indivGenes)):
            if indivGenes[i]==self.solucion[i]:
                fitness+=1
            else:
                pass

        return fitness #como fitness es una variable y no un obj. por eso se puede tener error. (solucionado)
     

class algoritmoEvolutivo():
    def __init__(self):
        self.rataUniforme=0.5
        self.rataMutacion=0.015
        self.tamanoTorneo=5
        self.elite=True
    
    def evolucionar(self, pobla):
        #print("evolucionando poblacion de ", len(pobla.individuos), "habitantes")
        emptyPoblacion=poblacion(len(pobla.individuos), False)
        #emptyPoblacion es una poblacion vacia
        if self.elite:
            emptyPoblacion.individuos[0]=pobla.encontrar_fittest()
            #print("EVOLUCIONAR DICE: ", emptyPoblacion.individuos[0].genes)

        if self.elite:
            offSetElite=1
        else:
            offSetElite=0

        for i in range(offSetElite,len(pobla.individuos)):
            indv1=self.elegirCandidatosMejorados(pobla)
            indv2=self.elegirCandidatosMejorados(pobla)
            mejorIndividuo=self.aparear(indv1,indv2)
            emptyPoblacion.individuos[i]=mejorIndividuo
        
        #print("OK")
        for i in range(offSetElite, len(emptyPoblacion.individuos)):
            #print("mutar: ",i)
            self.mutar(emptyPoblacion.individuos[i])
        
        return emptyPoblacion

        
    def aparear(self, indv1, indv2):
        '''50% de probabilidad de escoger un gen de uno o del otro y guardarlo en el nuevo individuo'''
        individuoMejorado=individuo() #no tiene genes.
        for i in range(len(indv1.genes)):
            #se 'aparean':
            if random.random() <= self.rataUniforme:
                individuoMejorado.genes[i]=indv1.genes[i]
            else:
                individuoMejorado.genes[i]=indv2.genes[i]
        #print("resultado: ", individuoMejorado.genes)
        return individuoMejorado
        

    def mutar(self, indv):
        '''Muta para bien o para mal, pero a una bajisima probabilidad de 0.015, solo muta por debajo de ese porcentaje'''
        count=0
        for i in range(len(indv.genes)):
            ran=random.random()
            if ran <= self.rataMutacion:
                count+=1
                genAleatorio=randint(0,1)
                indv.genes[i]=genAleatorio
        #print("mutar dice: ", indv.genes, "con ", count, " mutaciones, %",ran)
    

    def elegirCandidatosMejorados(self, pobl):
        poblacionTorneo=poblacion(self.tamanoTorneo,False)
        for i in range(self.tamanoTorneo):
            '''En el arreglo poblacion enviado, voy a seleccionar cinco. Esos cinco los guardo en el nuevo 
            set de indiviudos de la poblacion del torneo'''
            try:
                aleatorio=randint(0,len(pobl.individuos)-1)
                poblacionTorneo.individuos[i]=pobl.individuos[aleatorio]  
            except Exception as e:
                print(e)
        
        #de la poblacion tournamente, sacamos 1 fittest, el mas parecido a la necesidad.
        fittest=poblacionTorneo.encontrar_fittest()
        return fittest


#------------------------------------------------------------------------------------>DEBUG

print("MAIN...")
'''A diferencia del script original en java, esta cadena puede ser de longitud variable'''
#Gen al que queremos llegar.
cadenaGen='1111110000100001000001000111111111111111000100001000000'
print("Tamaño: ", len(cadenaGen))
#Poblacion de 10 individuos, con sus propios genes aleatorios
pop=poblacion(50,True)
'''Entre mas pequeña la poblacion mas tarde el algoritmo genetico en encontrar el individuo ganador'''

#contador para reconocer las generaciones.
contador=0
'''
La solucion maxima es cuando el valor de fitness es maximo, es decir cuando se parece en aproximadamente 100%
a el candidato o cadenaGen'''


#clase que posee la logica evolutiva
ae=algoritmoEvolutivo()

#variable global que permite obtener el individuo mas parecido y calcular sus genes.
calculadora=calculadora_fitnnes()

#modificamos el tamaño de nuestro gen maximo, por eso es variable.
calculadora.crear_gen_maximo(cadenaGen)

'''Si no se crea el gen_maximo, entonces el tamaño maximo que se puede obtener es de cuatro predefinido por codigo, y si
no se declara la cadena, en ese caso solo se obtiene el que mas se parece con 00000, para cambiarlo se valida con crear_gen_max()'''
print("---->>Iniciando, espere...")
#b=ae.elegirCandidatosMejorados(pop)
'''for i in range(len(mejorPoblacion.individuos)):
    print(mejorPoblacion.individuos[i].genes, mejorPoblacion.individuos[i].fitness)
'''
#obj=pop.encontrar_fittest()
#print("mas fit: ", obj.genes, 'fitness: ',calculadora.calcular_fitness(obj.genes))

def byte_a_str(cadenaBytes):
    solucionFinal=""
    for i in range(len(cadenaBytes)):
        solucionFinal+=str(cadenaBytes[i])
    return solucionFinal

while calculadora.calcular_fitness(pop.encontrar_fittest().genes)<len(cadenaGen):
    print("Generacion: ",contador, "Fittest:",byte_a_str(pop.encontrar_fittest().genes))
    contador+=1
    pop=ae.evolucionar(pop)

print("solucion encontrada!, en la generacion: ",contador)
print("Genes ganador: ",byte_a_str(pop.encontrar_fittest().genes))


