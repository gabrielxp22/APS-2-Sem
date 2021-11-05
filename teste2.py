def distancia(lista_latitude, lista_longitude, p1, lista_ecoponto):

    lista_dist = []

                    y = 0
                    while y < len(lista_latitude):
                        dist_ecoponto = geopy.distance.distance(p1, (lista_latitude[y], lista_longitude[y])).km
                        lista_dist.append(dist_ecoponto)
                        y = y + 1
                    print(linha())

                    print('''[ 1 ] - Ecoponto mais próximo
    [ 2 ] - Ecopontos dentro de um determinado raio''')

                    funcao = str(input("Qual função deseja realizar? "))

                    while funcao != "1" and funcao != "2":

                        funcao = str(input("Função inválida, escolha alguma função presente no menu acima "))

                    else:

                        if funcao == "1":

                            # variavel que recebe a posição do valor a cima na lista de distancia

                            posicao = lista_dist.index(min(lista_dist))

                            print("O ecoponto mais próximo de você é o :", lista_ecoponto[posicao])

                        elif funcao == "2":

                            raio = int(input("A partir de um raio de quantos quilometros deseja listar os pontos de "
                                             "coleta? "))

                            # cria uma lista com todos os valores da lista_dist menores ou igual a 5

                            lista_raio = [x for x in lista_dist if x <= raio]

                            # verifica cada valor de lista_raio na lista_dist para saber seu indice
                            # compara com o indice da lista_ecoponto para pegar o nome dos locais

                            x = 0

                            if lista_raio == []:
                                print("Não possuem ecopontos dentro de um raio de 5 km do seu endereço")
                            else:
                                print(linha())
                                print(f"O(s) ecopontos dentro de um raio de {raio} km do seu endereço são :")
                                while x < len(lista_raio):
                                    posicao1 = lista_dist.index(lista_raio[x])
                                    print(lista_ecoponto[posicao1])
                                    x = x + 1