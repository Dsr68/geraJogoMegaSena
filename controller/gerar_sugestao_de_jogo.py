import random

def ordenar(dados):
    valor = ""
    indice = 0
    tM = len(dados)

    for i in range(tM - 1):
        indice = i
        for j in range(i, tM):
            if dados[j][1] > dados[indice][1]:
                indice = j  
        if dados[i][1] < dados[indice][1]:
            aux = dados[i]
            dados[i] = dados[indice]
            dados[indice] = aux
    return dados

def selecionar_quantidade_de_dezenas(qt_dezenas, lista):
    lista_numeros = []
    for i in range(15):
        lista_numeros.append(int(lista[i][0]))

    return lista_numeros

def gerar_jogo(qt_dezenas, lista_numeros): 
    jogo = []

    for i in range(qt_dezenas):
        n = len(lista_numeros) - 1
        sorte = random.randint(0, n)
        jogo.append(lista_numeros.pop(sorte))

    tamanho = len(jogo)

    for i in range(tamanho - 1):
        indice = i
        for j in range(i, tamanho):
            if jogo[j] < jogo[indice]:
                indice = j
        if jogo[i] > jogo[indice]: 
            aux = jogo[i]
            jogo[i] = jogo[indice]
            jogo[indice] = aux

    for i in range(tamanho): 
        print(str(jogo[i]) + " - ", end="")