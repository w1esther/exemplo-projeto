import manipulador_arquivos as ma

'''chassi = int(input('Digite o chassi do carro: '))
marca = input('Digite a marca do carro: ')
modelo = input('Digite o modelo do carro: ')
ano = int(input('Digite o ano do carro: '))

carros = {
    'chassi': chassi,
    'marca': marca,
    'modelo': modelo,
    'ano': ano
}'''

ma.adicionar_carro({
    'chassi': 123456,
    'marca': 'Toyota',
    'modelo': 'Corolla',
    'ano': 2020
})