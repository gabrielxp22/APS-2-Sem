import geopy.distance
from geopy.geocoders import Nominatim
import pycep_correios
from pycep_correios import exceptions


def titulo(txt):
    print(linha())
    print(txt.center(42))
    print(linha())


def linha():
    return "-" * 42


def menu_inicial():
    titulo("MENU PRINCIPAL")
    print(''' [1] - Informações a respeito dos materiais recicláveis
 [2] - Visualizar pontos de coleta
 [3] - Visualizar ponto de coleta mais próximo
 [4] - Listar pontos de coleta a partir do raio do usuário
 [5] - Calculadora
 [6] - Sair
     ''')


def menu_material():
    print(''' [1] - Plástico  
 [2] - Vidro                
 [3] - Metal 
 [4] - Papel
 [5] - Pilhas e baterias
 [6] - Voltar 
 [7] - Sair               
     ''')

menu_inicial()

escolha_inicial = str(input("Qual opção deseja escolher do menu acima? "))


while escolha_inicial != "6":

    if escolha_inicial == "1":

        titulo("MENU DOS MATERIAIS RECICLÁVEIS")
        menu_material()
        escolha_material = str(input("Qual opção deseja escolher do menu acima? "))

        while escolha_material != "7":

            if escolha_material == "1":
                print("Plástico")
                break
            elif escolha_material == "2":
                print("Vidro")
                break
            elif escolha_material == "3":
                print("Metal")
                break
            elif escolha_material == "4":
                print("A industria do papel no Brasil iniciou-se em meados dos anos 1850, com a instalação da primeira"
                      "fábrica, no entanto, só 100 anos depois que o setor recebeu investimento para que pudesse se"
                      "estruturar.\n"
                      "Atualmente esse mercado é responsável por mais de 1% do PIB do país. Aliado ao aumento constante"
                      "de fabricação do papel, o setor de reciclagem tem aumento gradativo no país.\n"

                      "A reciclagem de papel foi algo que demorou para ser realmente vista como benéfico e lucrativo "
                      "no\n"
                      "Brasil. Antes da Lei 12.305, Política Nacional de Resíduos Sólidos (PNRS) que foi sancionada em "
                      "2010, a\n"
                      "logística por volta da reciclagem do papel era muito fraca, fazendo com que existisse uma falta de"
                      "estímulo por parte das empresas e da população em consumir papel reciclado,\n o que tinha como "
                      "consequência o aumento do valor do papel reciclado, mesmo que o seu processo de fabricação "
                      "fosse mais\n"
                      "barato em comparação com o papel virgem.\n"

                      "Atualmente o Brasil recicla mais de 66,9% (2019) de todo o papel, papelão e papeis de embalagem "
                      "produzidos, número que coloca o páis como um dos principais recicladores de papel do mundo.\n Essa"
                      "reciclagem passa por um processo de diversas etapas, até que as asparas coletadas virem novos papéis e"
                      "voltem para o comércio.\n"

                      "Processo de reciclagem do papel\n:"

                      "O processo pode ser resumido em duas etapas, a primeira etapa, na qual ocorre a separação das asparas "
                      "de papel,"
                      "pelo seu tipo e cor, e a separação manual para verificar possiveis objetos indesejados ou erros de "
                      "separação.\n"
                      "Já na segunda etapa, é onde entra a industria, nessa fase é formada uma polpa marrom com o uso de"
                      "diversos produtos químicos, ainda como polpa é removido as impurezas e cores do \"papel\n",
                      "após isso a"
                      "polpa é transformada em papel por uma série de dispositivos e cilindros, posteriro a isso é pintado de"
                      "branco dos dois lados e armazenado em grandes rolos que podem pesar até 3 toneladas.")
                break
            elif escolha_material == "5":
                print("Pilhas e baterias")
                break
            elif escolha_material == "6":
                menu_inicial()
                escolha_inicial = str(input("Qual opção deseja escolher do menu acima? "))
                break
            elif escolha_material == "7":
                print("Sair")

        if escolha_material == "7":

            print("Progama finalizado")
            quit()

    elif escolha_inicial == "2":

        print("Escolha 2")

    elif escolha_inicial == "3":

        print(linha())
        print('''[ 1 ] - CEP
[ 2 ] - Endereço
                ''')

        escolha = str(input("Como deseja inserir sua localização? "))

        while escolha != "1" and escolha != "2":
            escolha = str(input("Escolha inexistente, por favor insira um número referente ao menu acima "))
        else:
            if escolha == "1":
                cep = str(input("Digite seu CEP "))
                while len(cep) != 8:
                    print("CEP Invalido")
                    cep = str(input("Digite um cep valido "))
                else:
                    try:
                        endereco = pycep_correios.get_address_from_cep(cep)
                    except exceptions.InvalidCEP as eic:
                        print("CEP Invalido")
                    except exceptions.CEPNotFound as ecnf:
                        cep = str(input("Cep não encontrado, digite outro "))
                        endereco = pycep_correios.get_address_from_cep(cep)
                    except exceptions.Timeout as errt:
                        print("Erro de conexão, verifique sua conexão com a internet")
                    locator = Nominatim(user_agent="aps")
                    location = locator.geocode(endereco["logradouro"] + "," + endereco["cidade"] + "," + endereco["uf"])
                    p1 = (location.latitude, location.longitude)
            else:
                locator = Nominatim(user_agent="aps")
                location = locator.geocode(str(input("Digite seu endereço (EXEMPLO: Av Padre Guilherme Ary, 81, Campinas - SP) ")))
                while location == None:
                    location = locator.geocode(str(input("Endereço inválido, insira outro (EXEMPLO: Av Padre Guilherme Ary, 81, Campinas - SP):  ")))
                else:
                    p1 = (location.latitude, location.longitude)

        # Localização dos ecopontos

        lista_latitude = [-22.8172754, -22.9096444, -22.9046067, -22.891067, -22.916885, -22.9102275, -22.9617947,
                          -22.9420215, -22.885851, -22.9773029, -22.9486031]
        lista_longitude = [-47.1018107, -47.0685557, -47.1076838, -47.1041653, -47.0368281, -47.0711608, -47.190478,
                           -47.0309465, -47.1281875, -47.177823, -47.0582585]

        # Lista vazia onde sera inserido a distancia do usuário até os ecopontos

        lista_dist = []

        # Lista com o nome dos ecopontos

        lista_ecoponto = ["Ecoponto Barão Geraldo", "Ecoponto Central", "Ecoponto Jardim Pacaembu",
                          "Ecoponto Jardim Eulina", "Ecoponto Jardim Paranapanema",
                          "Cooperativa de Reciclagem São Bernardo", "Ecoponto Parque Itajaí",
                          "Ecoponto Jardim São Gabriel", "Ecoponto Parque Via Norte", "Ecoponto Vida Nova",
                          "Ecoponto Vila Campos Sales"]

        y = 0
        while y <= 10:
            dist_ecoponto = geopy.distance.distance(p1, (lista_latitude[y], lista_longitude[y])).km
            lista_dist.append(dist_ecoponto)
            y = y + 1

        # variavel que recebe a posição do valor a cima na lista de distancia

        posicao = lista_dist.index(min(lista_dist))

        print("O ecoponto mais próximo de você é o :", lista_ecoponto[posicao])

        print("Função executada")
        menu_inicial()
        escolha_inicial = str(input("Qual opção deseja escolher?"))


    elif escolha_inicial == "4":

        raio = int(input("A partir de um raio de quantos quilometros deseja listar os pontos de coleta? "))

        # cria uma lista com todos os valores da lista_dist menores ou igual a 5

        lista_raio = [x for x in lista_dist if x <= raio]

        # verifica cada valor de lista_raio na lista_dist para saber seu indice e compara com o indice da lista_ecoponto para pegar o nome dos locais

        x = 0

        if lista_raio == []:
            print("Não possuem ecopontos dentro de um raio de 5 km do seu endereço")
        else:
            print(f"O(s) ecopontos dentro de um raio de {raio} km são :")
            while x < len(lista_raio):
                posicao1 = lista_dist.index(lista_raio[x])
                print(lista_ecoponto[posicao1])
                x = x + 1
        print("Função executada")
        menu_inicial()
        escolha_inicial = str(input("Qual opção deseja escolher?"))

    else:
        print("escolha 5")
        break

if escolha_inicial == "6":
    titulo("PROGRAMA FINALIZADO")
    quit()









