from model.resultados import *
from controller.gerar_sugestao_de_jogo import *
from controller.analisar import *

#Pegar resultado de sorteios dos dois ultimos ate os dias atuais
#que houveram ganhadores da Mega Sena e calcula a frequencia de
#cada numero.
resultados = numeros_s

#Analisar frequencia dos numeros sorteados
dados = analisar(resultados)

#Ordenar dados coletados
lista = ordenar(dados)

#Aqui sao escolhidas as n os numeros mais sorteados
n = int(input("Selecione o numero de dezenas mais sorteadas: "))

#Gera uma lista com os n numeros mais sorteados
numeros = selecionar_quantidade_de_dezenas(n, lista)

#Escolher quantos numeros serao escolhidos 
qt_numeros = int(input("Quantos números você vai jogar: "))

gerar_jogo(qt_numeros, numeros)



