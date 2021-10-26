import geopy.distance
from geopy.geocoders import Nominatim
import pycep_correios
from pycep_correios import exceptions


def titulo(txt):
    print(linha())
    print(txt.center(56))
    print(linha())


def sub_titulo(txt):
    print(linha_subtitulo())
    print(txt.center(105))
    print(linha_subtitulo())


def linha_subtitulo():
    return "-" * 105


def linha():
    return "-" * 56


def menu_inicial():
    titulo("MENU PRINCIPAL")
    print(''' [1] - Informações a respeito dos materiais recicláveis
 [2] - Informações a respeito dos pontos de coleta
 [3] - Localização dos pontos de coleta
 [4] - Calculadora
 [5] - Sair
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


def menu_material2():
    print(''' [1] - Plástico  
 [2] - Vidro                
 [3] - Metal 
 [4] - Papel
 [5] - Pilhas e baterias
 [6] - Oleo vegetal
 [7] - Voltar 
 [8] - Sair               
     ''')


menu_inicial()

escolha_inicial = str(input("Qual opção deseja escolher do menu acima? "))

while escolha_inicial != "5":

    if escolha_inicial != "1" and escolha_inicial != "2" and escolha_inicial != "3" and escolha_inicial != "4" and \
            escolha_inicial != "5":

        escolha_inicial = str(input("Escolha inválida, digite novamente "))

    elif escolha_inicial == "1":

        titulo("MENU DOS MATERIAIS RECICLÁVEIS")
        menu_material()
        escolha_material = str(input("Qual opção deseja escolher do menu acima? "))

        while escolha_material != "7":

            if escolha_material == "1":
                sub_titulo("A RECICLAGEM DO PLÁSTICO NO BRASIL")
                print('''Características : 
                
Possuem resistência a altas, temperaturas, são muito versáteis em sua aplicação, 
têm alta capacidade de adequação. O plástico é um material que pode ser reciclado. Somado a isso, é 
extremamente durável, pois pode suportar variações significativas de temperatura e não costuma quebrar 
facilmente. Além disso, o custo de fabricação não é tão elevado. O plástico pode levar até 450 anos para se decompor.

Propriedades :

•    Resistência ao calor / temperatura;
•    Resistência mecânica;
•    Rigidez;
•    Estabilidade química;
•    Auto lubrificação (especialmente usado na fabricação de engrenagens e esquis);
•    Extinguível a chama.

As propriedades dos plásticos superam os materiais que eram comuns na indústria pois, além de possibilitar uma troca 
facilitada de peças em uma manutenção, não são condutores, fator que para determinadas aplicações é essencial.

Cuidados :

Os plásticos afetam o nosso planeta de várias maneiras. Um dos principais problemas é o de geralmente 
serem queimados ao ar livre, o que leva à poluição do ar. Além disso, quando os animais ou os seres humanos 
inalam o ar contaminado, isso pode afetar o seu bem-estar geral e causar distúrbios respiratórios.
Na terra, uma das consequências mais sérias do uso dos plásticos é a de estes filtrarem químicas perigosas, 
formando áreas de reprodução para doenças e contaminando a terra, reduzindo, assim, as áreas produtivas. 
A maioria dos plásticos também acaba em aterros e, como demoram anos a decompor-se, acumulam-se, resultando 
em riscos para a saúde das pessoas, animais e plantas.
Além é claro as imensas praias de lixo no meio do oceano , na qual a maior composição é de plástico.
Se não reciclar e começar a tratar  ,logo viveremos em um grande lixão.
''')

                break

            elif escolha_material == "2":
                sub_titulo("A RECICLAGEM DO VIDRO NO BRASIL")
                print('''O vidro foi uma das maiores descobertas da humanidade, principalmente o vidro em sua versão 
translucida.  Enxergar o conteúdo dentro do recipiente mudou nosso forma de consumir, a divisão de paredes de vidro 
mudou a arquitetura ou até mesmo as telas de celular utilizam o vidro. O vidro é obtido por fusão de 
matérias primeiras, em sua grande maioria mineiros em uma mistura básico de areia de sílica, sódio e cálcio. 
Isso acontece em altas temperaturas (150) para poder dar forma no material e logo em seguida resfriado. 
O vidro é um dos melhores materiais para serem reciclados pois não perdem suas características no processo,
e tem a mesma qualidade.


Porque devemos reciclar o vidro:
 
                
•	Menos acúmulos em aterros;
•	Fácil reaproveitamento;
•	Menos gasto na fabricação (sem produzir mais vidro);


Muito importante separar o vidro, existem 3 cores: verde, marrom e branco (transparente). 
Deve-se fazer uma triagem do material antes do descarte, o vidro também não pode ser descartado no lixo comum,
principalmente se estiver quebrado.''')
                break

            elif escolha_material == "3":

                sub_titulo("A RECICLAGEM DO METAL NO BRASIL")

                print('''- Características


Metal é um dos produtos mais utilizados no dia-a-dia em escala global, seja em utensílios domésticos, 
consumíveis ou industriais. Sendo assim um produto muito utilizado, logo, acaba tornando-se um material 
com alto índice gerador de lixo. Podem ser classificados em dois tipos: ferrosos (ferros e aços) ; 
não-ferrosos (níquel, alumínio, bronze, chumbo, cobre). Os tipos mais procurados no âmbito 
da reciclagem são os não-ferrosos.


- Cuidados


Cuidados a serem tomados:
    
    
- Separar sempre que possível, em momentos de coleta, dos demais tipos de lixo. Ou seja, não deixar metais 
juntos a plásticos, vidros ou materiais orgânicos é de grande importância coleta para o processo de reciclagem.

- Não jogar em locais públicos e inadequados. Apesar de latinhas de alumínio entre outras sucatas não-ferrosos, 
serem muito procuradas por “catadores”, essa ação pode acarretar, por exemplo, em entupimento de bueiros 
(facilitando enchentes). 


- Propriedades


- Formas de utilização e reutilização
- Muitas são as formas de utilização e reutilização dos metais. Seu reaproveitamento pode ser feito 
diversas vezes, sem perder suas principais propriedades. 

- Sua reciclagem auxilia a amenizar o uso de fontes de energias advindas de minérios, por exemplo, 
a bauxita sendo considerada um minério de alta qualidade no Brasil (e provocador de inúmeras danificações no solo).

- De outra forma, a reutilização de metais ajudam também na economia de custos de áreas de lixão e descarte. 
Ou seja, quanto mais material reciclado, menos se gasta para construção de espaços para seu recebimento.''')
                break

            elif escolha_material == "4":

                sub_titulo("A RECICLAGEM DO PAPEL NO BRASIL")

                print('''A industria do papel no Brasil iniciou-se em meados dos anos 1850, com a instalação da primeira
fábrica,  no entanto, só 100 anos depois que o setor recebeu investimento para que pudesse se estruturar. Atualmente,
esse mercado é responsável por mais de 1% do PIB do país. Aliado ao aumento constante de fabricação do papel, 
o setor de reciclagem tem aumento gradativo no país.


A reciclagem de papel foi algo que demorou para ser realmente vista como benéfico e lucrativo no Brasil. 
Antes da Lei 12.305, Política Nacional de Resíduos Sólidos (PNRS) que foi sancionada em 2010, a logística 
por volta da reciclagem do papel era muito fraca, fazendo com que existisse uma falta de estímulo por parte 
das empresas e da população em consumir papel reciclado, o que tinha como consequência o aumento do valor 
do papel reciclado, mesmo que o seu processo de fabricação fosse mais barato em comparação com o papel virgem.

                
Atualmente o Brasil recicla mais de 66,9% (2019) de todo o papel, papelão e papeis de embalagem produzidos, 
número que coloca o páis como um dos principais recicladores de papel do mundo. Essa reciclagem passa por um 
processo de diversas etapas, até que as asparas coletadas virem novos papéis e voltem para o comércio.

               
Processo de reciclagem do papel:
               
O processo pode ser resumido em duas etapas, a primeira etapa, na qual ocorre a separação das asparas 
de papel,pelo seu tipo e cor, e a separação manual para verificar possiveis objetos indesejados ou erros de 
separação. Já na segunda etapa, é onde entra a industria, nessa fase é formada uma polpa marrom com o uso de
diversos produtos químicos, ainda como polpa é removido as impurezas e cores do papel após isso a polpa 
é transformada em papel por uma série de dispositivos e cilindros, posterior a isso é pintado de branco 
os dois lados e armazenado em grandes rolos que podem pesar até 3 toneladas.''')
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

        titulo("MATERIAIS EM PONTOS DE COLETA")
        menu_material2()

        escolha_material2 = str(input("Deseja obter informações dos ecopontos que recolhem qual tipo de material? "))

        while escolha_material2 != "8":

            if escolha_material2 != "1" and escolha_material2 != "2" and escolha_material2 != "3" \
                    and escolha_material2 != "4" and escolha_material2 != "5" and escolha_material2 != "6 " \
                    and escolha_material2 != "7":

                escolha_material2 = str(input("Opção inválida, digite novamente "))

            elif escolha_material2 == "1":

                print("Abaixo está listado os pontos de coleta de plástico e suas informações")

            elif escolha_material2 == "2":

                print("Abaixo está listado os pontos de coleta de vidro e suas informações")

            elif escolha_material2 == "3":

                print("Abaixo está listado os pontos de coleta de metal e suas informações")

            elif escolha_material2 == "4":

                print("Abaixo está listado os pontos de coleta de papel e suas informações")

            elif escolha_material2 == "5":

                print("Abaixo está listado os pontos de coleta de pilhas e baterias  e suas informações")

            elif escolha_material2 == "6":

                print("Abaixo está listado os pontos de coleta de oleo vegetal e suas informações")

            elif escolha_material2 == "7":

                menu_inicial()
                escolha_inicial = str(input("Qual opção deseja escolher do menu acima? "))
                break

        else:

            titulo("PROGAMA FINALIZADO")
            quit()

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
                while len(cep) != 8 or cep == "99999999":
                    print("CEP Invalido")
                    cep = str(input("Digite um cep valido "))

                else:

                    try:
                        endereco = pycep_correios.get_address_from_cep(cep)

                    except exceptions.InvalidCEP as eic:
                        cep = str(input("CEP inválido, digite novamente "))
                        endereco = pycep_correios.get_address_from_cep(cep)

                    except exceptions.CEPNotFound as ecnf:
                        cep = str(input("CEP não encontrado, digite novamente "))
                        endereco = pycep_correios.get_address_from_cep(cep)

                    except exceptions.Timeout as errt:
                        print("Erro de conexão, verifique sua conexão com a internet e execute novamente o programa")
                        quit()

                    else:
                        locator = Nominatim(user_agent="aps")
                        location = locator.geocode(endereco["logradouro"] + "," + endereco["cidade"] + "," +
                                                   endereco["uf"])
                        p1 = (location.latitude, location.longitude)

            else:
                locator = Nominatim(user_agent="aps")
                location = locator.geocode(str(input("Digite seu endereço (EXEMPLO: Av Padre Guilherme Ary, 81,"
                                                     " Campinas - SP) ")))
                while location is None:
                    location = locator.geocode(str(input("Endereço inválido, insira outro (EXEMPLO: Av Padre Guilherme "
                                                         "Ary, 81, Campinas - SP):  ")))
                else:
                    p1 = (location.latitude, location.longitude)

        # Localização dos ecopontos

        lista_latitude = [-22.8172754, -22.9096444, -22.9046067, -22.891067, -22.916885, -22.9102275, -22.9617947,
                          -22.9420215, -22.885851, -22.9773029, -22.9486031, -22.936197]
        lista_longitude = [-47.1018107, -47.0685557, -47.1076838, -47.1041653, -47.0368281, -47.0711608, -47.190478,
                           -47.0309465, -47.1281875, -47.177823, -47.0582585, 47.1207617]

        lista_lat_oleo = [-22.9258933, -22.8942854, -22.89136, -22.9465589, -22.8439297, -22.9051623]

        lista_long_oleo = [-47.08159, -47.0604147, -47.0260114, -47.0314758, -47.1023985, -46.9801448]

        # Lista vazia onde sera inserido a distancia do usuário até os ecopontos

        lista_dist = []

        # Lista com o nome dos ecopontos

        lista_ecoponto = ["Ecoponto Barão Geraldo", "Ecoponto Central", "Ecoponto Jardim Pacaembu",
                          "Ecoponto Jardim Eulina", "Ecoponto Jardim Paranapanema",
                          "Cooperativa de Reciclagem São Bernardo", "Ecoponto Parque Itajaí",
                          "Ecoponto Jardim São Gabriel", "Ecoponto Parque Via Norte", "Ecoponto Vida Nova",
                          "Ecoponto Vila Campos Sales", "Ecoponto Vila União"]

        lista_oleovegetal = ["Tenda Atacado", "Carrefour Cambuí", "Carrefour Iguatemi", "Carrefour Von Zuben",
                             "Tenda Dom Pedro", "Carrefour Dom Pedro"]

        print(linha())
        print('''[1] - Plástico  
[2] - Vidro                
[3] - Metal 
[4] - Papel
[5] - Pilhas e baterias
[6] - Óleo Vegetal ''')

        material = str(input("Deseja obter a informação dos pontos de coleta de qual material? "))

        while material != "1" and material != "2" and material != "3" and material != "4" and material != "5" and \
                material != "6":

            material = str(input("Escolha inválida, digite novamente "))

        else:

            if material == "1" or material == "2" or material == "3" or material == "4":

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

                            menu_inicial()
                            escolha_inicial = str(input("Qual opção deseja escolher? "))

            else:

                lista_dist = []

                y = 0
                while y < len(lista_lat_oleo):
                    dist_ecoponto = geopy.distance.distance(p1, (lista_lat_oleo[y], lista_long_oleo[y])).km
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

                        print("O ecoponto mais próximo de você é o :", lista_oleovegetal[posicao])

                    elif funcao == "2":

                        raio = int(
                            input("A partir de um raio de quantos quilometros deseja listar os pontos de coleta? "))

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
                                print(lista_oleovegetal[posicao1])
                                x = x + 1

                            menu_inicial()
                            escolha_inicial = str(input("Qual opção deseja escolher? "))

    elif escolha_inicial == "4":
        print("Calculadora")
        break
    else:
        titulo("PROGRAMA FINALIZADO")
        quit()

else:
    titulo("PROGRAMA FINALIZADO")
    quit()

if escolha_inicial == "6":
    titulo("PROGRAMA FINALIZADO")
    quit()
