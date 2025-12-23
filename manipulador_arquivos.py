import json



CAMINHO_ARQUIVO = 'dados/carros.json'

def ler_carros():
    f = open(CAMINHO_ARQUIVO, 'r')
    return json.load(f)

def salvar_carros(lista):
    s = open(CAMINHO_ARQUIVO, 'w')
    json.dump(lista, s, indent=4)

def adicionar_carro(carro):
    carros = ler_carros()
    prox_id = calcular_proximo_id(carros)
    carros['id'] = prox_id
    carros.append(carro)
    salvar_carros(carros)

def buscar_carro_por_modelo(modelo):
    carro = ler_carros()
    for c in carro:
        if c['modelo'] == modelo:
            return c
    return None

def calcular_proximo_id(carros):
    ids = []
    for c in carros:
        ids.append(c['id'])
    return max(ids, default=0) + 1

def buscar_carro_por_id(id):
    carros = ler_carros()
    for n in carros:
        if n['id'] == id:
            return n
    return None

def remover_carro(id):
    antiga_lista = ler_carros()
    nova_lista = []
    for c in antiga_lista:
        if c['id'] != id:
            nova_lista.append(c)
    salvar_carros(nova_lista)

def atualizar_carro(id, novos_dados):
    carros = ler_carros()
    for indice, c in enumerate(carros):
        if c['id'] == id:
            novos_dados['id'] = id
            carros[indice] = novos_dados