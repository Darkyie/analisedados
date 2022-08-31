import statistics
import math
import matplotlib.pyplot as plt
import numpy
lista = []
qnt = int(input("Qual será a quantidade de valores inseridos na lista? "))
if qnt == 0:
      print("Você colocou 0 na quantidade de números.")
else:
    for x in range(qnt):
      lista.append(float(input("Insira os valores da lista de um por um: ")))
    print ("A lista é: ",lista)
    desvio = statistics.pstdev(lista)
    print("O valor do desvio padrão populacional é (pre-programado): ",desvio)
    desvioamostral = statistics.stdev(lista)
    print("O valor do desvio padrão amostral é (pre-programado): ",desvioamostral)

    var = statistics.pvariance(lista)
    print("O valor da variância populacional é (pre-programado): ",var)
    varamo = statistics.variance(lista)
    print("O valor da variância amostral é (pre-programado): ",varamo)
    

    maior = max(lista)
    menor = min(lista)

    amplitude = maior - menor
    print("O valor da amplitude é: ", amplitude)


    a = len(lista)
    b = sum(lista)
    media = b/a
    print(f"A média é: ",media)
media2 = statistics.mean(lista)
print("A média é (pre-programado): ",media2)


if((len(lista)%2) == 0):
        lista.sort
        mediana1= lista[int(len(lista) / 2)]
        mediana = lista[int(len(lista) / 2) - 1]
        mediana = mediana + mediana1
        mediana = mediana / 2
else:
        mediana = lista[int(len(lista) / 2)]
        print("A mediana é:", mediana)
mediana2 = statistics.median(lista)
print("A mediana é (pre-programado): ",mediana2)

x = 0
desviop = []
abobora = []
for x in range (qnt):
    sla = (lista[x] - media)
    desviop.append(sla)
    x = x + 1

for x in range (qnt):
    desvioquad = desviop[x] ** 2
    abobora.append(desvioquad)
    x = x + 1

somaab = sum(abobora)

desviopadraopop = somaab / len(desviop) 
sla2 = len(desviop) -1
desviopadraoamo = somaab / sla2
print("A variação populacional é: ",desviopadraopop)
print("A variação amostral é: ",desviopadraoamo)
desviopadraofinalmesmo = math.sqrt(desviopadraopop)
print("O desvio padrão populacional é: ",desviopadraofinalmesmo)
desviopadraoamofinal = math.sqrt(desviopadraoamo)
print("O desvio padrão amostral é: ",desviopadraoamofinal)

coef_pop = (desviopadraofinalmesmo / media) * 100
print("O coeficiente populacional é: ", coef_pop)
coef_amostra = (desviopadraoamofinal / media) * 100
print("O coeficiente amostral é: ", coef_amostra)

lista.sort()
if((len(lista)%2) == 0 ) and (((len(lista)/2)%2) == 0):
        mediana1= lista[int(len(lista) / 2)]
        mediana = lista[int(len(lista) / 2) - 1]
        mediana = mediana + mediana1
        mediana = mediana / 2

        quartil_1 = lista[int(len(lista) / 4 )]
        quartil_p = lista[int(len(lista) /4) - 1]
        quartil_1 = quartil_1 + quartil_p
        quartil_1 = quartil_1 / 2

        quartil_3 = lista[int(len(lista) * (3/4))]
        quartil_m = lista[int(len(lista) * (3/4)) - 1]
        quartil_3 = quartil_3 + quartil_m
        quartil_3 = quartil_3 / 2

        print(f"Primeiro Quartil: {quartil_1}, Segundo Quartil: {mediana}, Terceiro Quartil: {quartil_3}")
elif ((len(lista)%2) == 0 ) and (((len(lista)/2)%2) != 0):
        mediana1 = lista[int(len(lista) / 2)]
        mediana = lista[int(len(lista) / 2) - 1]
        mediana = mediana + mediana1
        mediana = mediana / 2

        quartil_1 = lista[int(len(lista) / 4)]

        quartil_3 = lista[int(len(lista) * (3 / 4))]

        print(f"Primeiro Quartil: {quartil_1}, Segundo Quartil: {mediana}, Terceiro Quartil: {quartil_3}")

else:
        mediana = lista[int(len(lista) / 2)]

        quartil_1 = lista[int(len(lista) / 4)]
        quartil_p = lista[int(len(lista) / 4) - 1]
        quartil_1 = quartil_1 + quartil_p
        quartil_1 = quartil_1 / 2

        quartil_3 = lista[int(len(lista) * (3 / 4))]
        quartil_m = lista[int(len(lista) * (3 / 4)) - 1]
        quartil_3 = quartil_3 + quartil_m
        quartil_3 = quartil_3 / 2
        print(f"Primeiro Quartil: {quartil_1}, Terceiro Quartil: {quartil_3}, Mediana: {mediana}")

print(f'O Quartil é (pre-programado): {numpy.quantile(lista, [0.25,0.5,0.75])}')
print("Não achei como fazer o coeficiente populacional e amostral por uma função pre-programada :/")
plt.hist(lista)
plt.show()
plt.boxplot(lista)
plt.show()
        