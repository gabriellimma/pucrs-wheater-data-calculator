# Aluno: Gabriel Silva Lima
# entrega da fase 1 da disciplina de Lógica e Programação de Computadores
# repositório: https://github.com/gabriellimma/pucrs-wheater-data-calculator

def ler_temperaturas():
    """função que popula uma index com um valor através da leitura
    via terminal. O valor só é populado na index recebida caso
    atenda a lógica de ser menor ou igual a 50.0 e maior ou igual
    a -60.0. Do contrário, a função é chamada de forma recursiva
    até o valor passado atender a lógica.

    Returns:
    array: array com 12 temperaturas máximas

   """
    # cria um array vazio para armazenar as temperaturas
    temperaturas = []
    # enquanto o array de temperaturas não estiver completo com 12 valores
    while len(temperaturas) < 12:
        # le a temperatura com a mensagem 'digite a temperatura...'
        temp = float(input(f'Digite a temperatura máxima do mês {len(temperaturas) + 1}: '))
        # verifica se a temperatura é válida
        if temp <= 50.0 and temp >= -60.0:
            # se for válida, adiciona a temperatura ao array
            temperaturas.append(temp)
        else:
            # imprime uma mensagem de erro e mantem o array no mesmo estado
            print('Temperatura inválida. Digite novamente.')
    # retorna o array de temperaturas
    return temperaturas


def calcular_media(temperaturas):
    """função que calcula a média das temperaturas de um ano

    Args:
    temperaturas (array): array com 12 temperaturas

    Returns:
    float: média das temperaturas
    """
    # retorna a média das temperatura através da soma das temperaturas
    # dividido pela quantidade de temperaturas encontradas no array
    return sum(temperaturas) / len(temperaturas)


def meses_escaldantes(temperaturas):
    """função que retorna a quantidade de meses em que a temperatura
    foi maior que 33 graus celcius

    Args:
    temperaturas (array): array com 12 temperaturas

    Returns:
    int: quantidade de meses em que a temperatura foi maior que 33 graus celcius
    """
    # cria um contador para armazenar a quantidade de meses escaldantes
    qtd_meses_escaldantes = []
    # crian index para descobrir em qual mês a temperatura foi maior que 33
    index = 1
    # para cada temperatura no array de temperaturas
    for temp in temperaturas:
        # se a temperatura for maior que 33
        if temp > 33:
            # adiciona a temperatura ao contador junto a index (mes) onde foi encontrada
            # para recuperar o mês exato onde a temperatura foi maior que 33
            qtd_meses_escaldantes.append([index, temp])
        index += 1
    # retorna a quantidade de meses escaldantes
    return qtd_meses_escaldantes


def mes_mais_quente(temperaturas):
    """função que retorna o mês mais quente do ano

    Args:
    temperaturas (array): array com 12 temperaturas

    Returns:
    int: mês mais quente do ano
    """
    # retorna o mês mais quente do ano através da index do maior valor
    # encontrado no array de temperaturas
    num_mes_mais_quente = temperaturas.index(max(temperaturas))

    # array com os meses do ano
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
             'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    # retorna o mês mais quente do ano com base no index encontrada no array 'num_mes_mais_quente'
    # comparando com o array 'meses'
    return meses[num_mes_mais_quente]


def mes_mais_frio(temperaturas):
    """função que retorna o mês mais frio do ano

    Args:
    temperaturas (array): array com 12 temperaturas

    Returns:
    int: mês mais frio do ano
    """
    # retorna o mês mais frio do ano através da index do menor valor
    # encontrado no array de temperaturas
    num_mes_mais_frio = temperaturas.index(min(temperaturas))

    # array com os meses do ano
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
             'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    # retorna o mês mais frio do ano com base no index encontrada no array 'num_mes_mais_frio'
    # comparando com o array 'meses'
    return meses[num_mes_mais_frio]

def main():
    # para fazer um teste rápido, descomente a linha abaixo e comente a linha 119
    # temperaturas = [34.3, 36, 31, 31.7, 31, 20, 17, 42.5, 37, 32.1, 33, 23]

    temperaturas = ler_temperaturas()
    print('As temperaturas recebidas foram:', temperaturas)
    media = calcular_media(temperaturas)
    print(f'A média das temperaturas é {media:.2f}')
    meses_quentes = meses_escaldantes(temperaturas)
    print(f'A quantidade de meses em que a temperatura foi maior que 33 graus foram {len(meses_quentes)}')
    mes_quente = mes_mais_quente(temperaturas)
    print(f'O mês mais quente do ano foi o mês de {mes_quente}')
    mes_frio = mes_mais_frio(temperaturas)
    print(f'O mês mais frio do ano foi o mês de {mes_frio}')


main()
