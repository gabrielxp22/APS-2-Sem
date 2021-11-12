import geopy.distance
from geopy.geocoders import Nominatim
import pycep_correios
from pycep_correios import exceptions


def titulo_menu2(txt):
    print(linha_menu2())
    print(txt.center(180))


def linha_menu2():
    return "-" * 180


def titulo(txt):
    print(linha())
    print(txt.center(57))
    print(linha())


def sub_titulo(txt):
    print(linha_subtitulo())
    print(txt.center(105))
    print(linha_subtitulo())


def linha_subtitulo():
    return "-" * 105


def linha():
    return "-" * 57


def menu_inicial():
    titulo("MENU PRINCIPAL")
    print('''⎪ [1] - Informações a respeito dos materiais recicláveis ⎪ 
⎪ [2] - Informações a respeito dos pontos de coleta      ⎪
⎪ [3] - Localização dos pontos de coleta                 ⎪
⎪ [4] - Calculadora                                      ⎪
⎪ [5] - Sair                                             ⎪
⎪________________________________________________________⎪
     ''')


def menu_material():
    print('''                __________________________
                ⎪ [1] - Plástico          ⎪  
                ⎪ [2] - Vidro             ⎪                
                ⎪ [3] - Metal             ⎪
                ⎪ [4] - Papel             ⎪
                ⎪ [5] - Pilhas e baterias ⎪
                ⎪ [6] - Voltar            ⎪ 
                ⎪ [7] - Sair              ⎪
                ⎪_________________________⎪               
     ''')


def menu_material2():
    print('''               __________________________
               ⎪ [1] - Plástico          ⎪  
               ⎪ [2] - Vidro             ⎪           
               ⎪ [3] - Metal             ⎪
               ⎪ [4] - Papel             ⎪
               ⎪ [5] - Pilhas e baterias ⎪
               ⎪ [6] - Oleo vegetal      ⎪
               ⎪ [7] - Voltar            ⎪
               ⎪ [8] - Sair              ⎪
               ⎪_________________________⎪              
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

        while escolha_material != "7": #WHILE RESPONSAVEL POR MOSTRAR AS INFORMAÇÕES DOS MATERIAIS

            if escolha_material == "1": #TEXTO PLÁSTICO
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

            elif escolha_material == "2": #TEXTO VIDRO
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

            elif escolha_material == "3": #TEXTO METAL
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

            elif escolha_material == "4": #TEXTO PAPEL
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
                sub_titulo("A RECICLAGEM DAS PILHAS E BATERIAS NO BRASIL")
                print(''' Pilhas:
                
a pilha é basicamente um envoltório de zinco um tipo de metal constituído por uma barra de grafita ou carvão inserida 
em um tubo poroso que contém carvão esmagado e dióxido de manganês. Envolvida por uma pasta úmida, uma solução que 
possibilita a condução de carga elétrica no interior da pilha, existem diversos tipos de pilhas diferentes desde 
as de Zinco, as alcalinas (constituídas de metais do tipo alcalino terroso), as de lítio (constituída de íons de 
lítio o que a torna uma pilha recarregável).

Baterias:

Agora falando sobre as baterias, elas são formadas por várias pilhas ligadas entre si. as baterias podem fornecer 
diferentes voltagens e níveis de corrente. Uma pilha comum geralmente possui voltagem igual a 1,5 V, sendo que seis 
pilhas ligadas em série originam uma bateria de 9 V. Um exemplo é a bateria de chumbo usada nos automóveis. 
Ela é formada por seis pilhas de 2 V cada, possuindo uma potência de 12 V no total. 
Ela é formada por várias placas de chumbo todas essas placas ficam imersas em uma solução de ácido sulfúrico (H2SO4) e 
são intercaladas e separadas por papelão ou plástico, alguns tipos de baterias incluem, baterias de níquel ou cádmio, 
bateria de íons de lítio (por não usarem lítio metálico, mas sim íons de lítio elas são recarregáveis).

Cuidados a serem tomados:

Pilhas:

Use sempre o tamanho e o tipo corretos de pilha, especificados pelo fabricante do aparelho. 
Mantenha as superfícies de contato da pilha limpos, passando neles uma borracha de lápis limpa ou um pano áspero 
cada vez que você as trocar. Temperaturas extremas reduzem o desempenho das pilhas. Armazene-as em um local seco em 
temperatura ambiente normal. Não as refrigere, pois isso não fará com que durem mais tempo, e evite colocar dispositivos 
com pilhas em locais muito quentes.

Baterias:

As baterias automotivas possuem componentes que podem ser prejudiciais ao meio ambiente, um bom exemplo são as baterias 
de chumbo elas possuem vários componentes tóxicos que podem contaminar o solo. Por isso, você não deve jogá-las em lixos 
convencionais ou na natureza, pois em uma bateria de chumbo-ácido encontram-se elementos químicos extremamente 
prejudiciais para os seres vivos. A peça é composta de chumbo e outros materiais tóxicos. Quando mal descartada pode 
causar disfunções no sistema nervoso, problemas ósseos, circulatórios etc.

Formas de reutilização Pilhas e Baterias:

Após passar pela etapa de trituração as pilhas e baterias são submetidas a mais dois processos antes de serem 
reaproveitadas No processo químico as baterias são submetidas a um processo que recupera sais e óxidos metálicos que 
são posteriormente utilizados na indústria como matéria prima  em corantes e pigmentos, no processo térmico elas são 
levadas ao forno do tipo industrial onde são submetidas a alta temperatura para a separação do zinco, assim podendo ser 
reutilizado novamente na confecção de novas pilhas ou baterias, O processo de reciclagem de pilhas e baterias 
reaproveita os metais e componentes químicos. Além disso, todos eventuais resíduos do processo são também tratados e 
reaproveitados, exemplo:  na produção de cimento, ou são enviados para uma destinação ambientalmente correta.
                ''')  #TEXTO PILHAS E BATERIAS
                break

            elif escolha_material == "6": #ELIF RESPOSAVEL PELA FUNÇÃO "VOLTAR" DO MENU, RETORNA O MENU INICIAL
                menu_inicial()
                escolha_inicial = str(input("Qual opção deseja escolher do menu acima? "))
                break

            elif escolha_material == "7": #ELIF RESPOSAVEL POR FECHAR O PROGRAMA
                print("Sair")

            else:
                escolha_material = input("Escolha inválida, digite novamente ")

        if escolha_material == "7":

            titulo("PROGRAMA FINALIZADO")
            quit()

    elif escolha_inicial == "2":

        titulo("MATERIAIS EM PONTOS DE COLETA")
        menu_material2()

        escolha_material2 = str(input("Deseja obter informações dos ecopontos que recolhem qual tipo de material? "))

        while escolha_material2 != "8":

            if escolha_material2 != "1" and escolha_material2 != "2" and escolha_material2 != "3" \
                    and escolha_material2 != "4" and escolha_material2 != "5" and escolha_material2 != "6" \
                    and escolha_material2 != "7":

                escolha_material2 = str(input("Opção inválida, digite novamente "))

            elif escolha_material2 == "1" or escolha_material2 == "2" or escolha_material2 == "3" or \
                    escolha_material2 == "4":

                print('''
⎪--------------------------------------------------------------------------------------------------------------------------------------------------------⎪
⎪                                      OS PONTOS DE COLETA DO MATERIAL ESCOLHIDO NA REGIÃO DE CAMPINAS SÃO:                                              ⎪
⎪-----------------------------------------⎪---------------------------------------------------------------⎪-----------------------------------------------⎪            
⎪                  NOME                   ⎪                           ENDEREÇO                            ⎪            HORÁRIO DE FUNCIONAMENTO           ⎪
⎪-----------------------------------------⎪---------------------------------------------------------------⎪-----------------------------------------------⎪
⎪ Ecoponto / Ponto Verde Barão Geraldo    ⎪ Av. Santa Isabel, s/nº, Barão Geraldo                         ⎪ Das 7h às 18h, todos os dias, exceto feriados ⎪ 
⎪-----------------------------------------⎪---------------------------------------------------------------⎪-----------------------------------------------⎪
⎪ Ecoponto central                        ⎪ Rua Francisco Theodoro, 1050, Vila Industrial, Região Central ⎪ Das 7h às 18h, todos os dias, exceto feriados ⎪ 
⎪-----------------------------------------⎪---------------------------------------------------------------⎪-----------------------------------------------⎪
⎪ Ecoponto Jardim Pacaembu                ⎪ Rua Dante Suriane, Jardim Pacaembu                            ⎪ Das 7h às 18h, todos os dias                  ⎪ 
⎪-----------------------------------------⎪---------------------------------------------------------------⎪-----------------------------------------------⎪
⎪ Ecoponto Jardim Eulina                  ⎪ Avenida Marechal Rondon, Jardim Eulina                        ⎪ Das 7h às 18h, todos os dias                  ⎪ 
⎪-----------------------------------------⎪---------------------------------------------------------------⎪-----------------------------------------------⎪
⎪ Ecoponto Jardim Paranapanema            ⎪ Rua Serra D água, Jardim Paranapanema                         ⎪ Das 7h às 18h, todos os dias                  ⎪
⎪-----------------------------------------⎪---------------------------------------------------------------⎪-----------------------------------------------⎪
⎪ Cooperativa de Reciclagem São Bernanrdo ⎪ Av. Prefeito Faria Lima, 630, Parque Itália                   ⎪ Das 7h às 16h12, de segunda a sexta-feira     ⎪
⎪-----------------------------------------⎪---------------------------------------------------------------⎪-----------------------------------------------⎪ 
⎪ Ecoponto Parque Itajaí                  ⎪ Rua Celso Soares Couto, s/n, Parque Itajaí                    ⎪ Das 7h às 18h, todos os dias, exceto feriados ⎪
⎪-----------------------------------------⎪---------------------------------------------------------------⎪-----------------------------------------------⎪ 
⎪ Ecoponto Jardim São Gabriel             ⎪ Rua Jose Martins Lourenço, Jardim São Gabriel                 ⎪ Das 7h às 18h, todos os dias, exceto feriados ⎪
⎪-----------------------------------------⎪---------------------------------------------------------------⎪-----------------------------------------------⎪ 
⎪ Ecoponto Parque Via Norte               ⎪ Rua dos Cambarás, 200, Parque Via Norte                       ⎪ Das 7h às 18h, todos os dias, exceto feriados ⎪
⎪-----------------------------------------⎪---------------------------------------------------------------⎪-----------------------------------------------⎪ 
⎪ Ecoponto Vida Nova                      ⎪ Rua Góia Jr, s/n                                              ⎪ Das 7h às 18h, todos os dias, exceto feriados ⎪
⎪-----------------------------------------⎪---------------------------------------------------------------⎪-----------------------------------------------⎪ 
⎪ Ecoponto Vila Campos Sales              ⎪ Avenida São Jose dos Campos, s/n, Vila Campos Sales           ⎪ Das 7h às 18h, todos os dias                  ⎪
⎪-----------------------------------------⎪---------------------------------------------------------------⎪-----------------------------------------------⎪ 
⎪ Ecoponto Vila União                     ⎪ Rua Manoel Gomes Ferreira                                     ⎪ Das 7h às 18h, todos os dias                  ⎪
⎪-----------------------------------------⎪---------------------------------------------------------------⎪-----------------------------------------------⎪
⎪ Ecoponto Sousas                         ⎪ Rua Dom Pedro, 464                                            ⎪ Das 7h às 18h, todos os dias, exceto feriados ⎪
⎪--------------------------------------------------------------------------------------------------------------------------------------------------------⎪
''')
                break

            elif escolha_material2 == "5" or escolha_material2 == "6":

                print('''
⎪---------------------------------------------------------------------------------------------------------------------------------------------------------------⎪
⎪                                               OS PONTOS DE COLETA DO MATERIAL ESCOLHIDO NA REGIÃO DE CAMPINAS SÃO:                                            ⎪
⎪---------------------⎪--------------------------------------------------------------------⎪---------------------------------------------------------------------⎪            
⎪         NOME        ⎪                              ENDEREÇO                              ⎪                       HORÁRIO DE FUNCIONAMENTO                      ⎪
⎪---------------------⎪--------------------------------------------------------------------⎪---------------------------------------------------------------------⎪
⎪ Tenda Atacado       ⎪ Rua João Felipe Xavier da Silva, 190 - São Bernardo                ⎪ das 7h às 22h, de segunda a sábado. Das 8h as 18h aos domingos      ⎪ 
⎪---------------------⎪--------------------------------------------------------------------⎪---------------------------------------------------------------------⎪
⎪ Carrefour Cambuí    ⎪ Rua Santa Cruz, 281 - Cambuí                                       ⎪ das 7h às 22h, de segunda a sábado. Das 8h as 20h aos domingos.     ⎪ 
⎪---------------------⎪--------------------------------------------------------------------⎪---------------------------------------------------------------------⎪
⎪ Carrefour Iguatemi  ⎪ Carrefour Iguatemi, 140 - Vila Brandina                            ⎪ Horário de funcionamento: das 7h às 18h, todos os dias              ⎪ 
⎪---------------------⎪--------------------------------------------------------------------⎪---------------------------------------------------------------------⎪
⎪ Carrefour Von Zuben ⎪ Av. Eng. Antonio Francisco de Paula Souza, 3900 - Jardim Von Zubem ⎪ Horário de funcionamento: das 7h às 18h, todos os dias              ⎪
⎪---------------------⎪--------------------------------------------------------------------⎪---------------------------------------------------------------------⎪
⎪ Tenda Dom Pedro     ⎪ Rodovia Dom Pedro I, 140 - Santa Monica                            ⎪ das 7h às 22h, de segunda a sábado. Das 8h as 18h aos domingos      ⎪
⎪---------------------⎪--------------------------------------------------------------------⎪---------------------------------------------------------------------⎪
⎪ Carrefour Dom Pedro ⎪ Rodovia Dom Pedro I, 127 - Jardim Nilópolis                        ⎪ Horário de funcionamento: das 7h às 16h12, de segunda a sexta-feira ⎪
⎪---------------------------------------------------------------------------------------------------------------------------------------------------------------⎪ 
''')
                break

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

        print('''__________________________
⎪ [1] - Plástico          ⎪  
⎪ [2] - Vidro             ⎪                
⎪ [3] - Metal             ⎪ 
⎪ [4] - Papel             ⎪
⎪ [5] - Pilhas e baterias ⎪
⎪ [6] - Óleo Vegetal      ⎪
⎪_________________________⎪
''')

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

                        print("O ecoponto mais próximo de você para o material escolhido é o :", lista_ecoponto[posicao])

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

                        print("O ecoponto mais próximo de você para o material escolhido é o :", lista_oleovegetal[posicao])

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
                    scolha_inicial = str(input("Qual opção deseja escolher? "))

    elif escolha_inicial == "4":

        print('''__________________________
⎪ [1] - Plástico          ⎪  
⎪ [2] - Vidro             ⎪                
⎪ [3] - Metal             ⎪
⎪ [4] - Papel             ⎪
⎪ [5] - Voltar            ⎪
⎪ [6] - Sair              ⎪
⎪_________________________⎪               
             ''')

        material = input('Qual opção você deseja? ')


        while material != "6":


            while material != "1" and material != "2" and material != "3" and material != "4" and material != "5" and material != "6":
                material = input("Escolha inválida, digite um número referente ao menu acima ")

            else:

                if material == "1":

                    kilo = float(input(f'Quantos quilos você tem: '))

                    print('''__________________________
⎪    TIPOS DE PLÁSTICO    ⎪
⎪                         ⎪
⎪ [1] - Garrafa PET       ⎪
⎪ [2] - Plástico diversos ⎪
⎪ [3] - Voltar            ⎪
⎪_________________________⎪
''')

                    plastico = input("Qual tipo de plástico voce possuí? ")

                    while plastico != "3":

                        if plastico != "1" and plastico != "2":
                            plastico = input("Escolha inválida, digite um número referente ao menu acima ")

                        elif plastico == "1":
                            valor = kilo * 0.8
                            print(f"Você receberá por {kilo} quilos de garrafa PET R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menua acima? ")
                            break


                        else:
                            valor = kilo * 0.5
                            print(f"Você receberá por {kilo} de plásticos diversos  R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menua acima? ")
                            break

                    else:
                        break

                elif material == "2":

                    kilo = float(input(f'Quantos quilos você tem: '))

                    print('''_______________________
⎪    TIPOS DE VIDRO    ⎪
⎪                      ⎪
⎪ [1] - Branco         ⎪
⎪ [2] - Verde / Marrom ⎪
⎪ [3] - Voltar         ⎪
⎪______________________⎪
''')

                    vidro = input("Qual tipo de vidro voce possuí? ")

                    while vidro != "3":

                        if vidro != "1" and vidro != "2":
                            vidro = input("Escolha inválida, digite um número referente ao menu acima ")

                        elif vidro == "1":
                            valor = kilo * 0.38
                            print(f"Você receberá por {kilo} quilos de vidro branco R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menua acima? ")
                            break

                        else:
                            valor = kilo * 0.35
                            print(f"Você receberá por {kilo} quilos de vidro verde / marrom  R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menua acima? ")
                            break

                    else:
                        break

                elif material == "3":

                    kilo = float(input(f'Quantos quilos você tem: '))

                    print('''__________________________
⎪      TIPOS DE METAL     ⎪
⎪                         ⎪
⎪ [1] - Metal             ⎪   
⎪ [2] - Inox              ⎪
⎪ [3] - Alumínio          ⎪
⎪ [4] - Sucata de latinha ⎪
⎪ [5] - Ferro misto       ⎪
⎪ [6] - Voltar            ⎪
⎪_________________________⎪
''')

                    metal = input("Qual tipo de metal você possuí? ")

                    while metal != "6":

                        if metal != "1" and metal != "2" and metal != "3" and metal != "4" and metal != "5":
                            metal = input("Escolha inválida, digite um número referente ao menu acima ")

                        elif metal == "1":
                            valor = kilo * 12
                            print(f"Você receberá por {kilo} quilos de metal R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menua acima? ")
                            break

                        elif metal == "2":
                            valor = kilo * 3.5
                            print(f"Você receberá por {kilo} quilos de inox R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menua acima? ")
                            break

                        elif metal == "3":
                            valor = kilo * 3.6
                            print(f"Você receberá por {kilo} quilos de alumínio R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menua acima? ")
                            break

                        elif metal == "4":
                            valor = kilo * 4.5
                            print(f"Você receberá por {kilo} quilos de sucata de latinha R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menua acima? ")
                            break

                        else:
                            valor = kilo * 0.75
                            print(f"Você receberá por {kilo} quilos de ferro misto R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menua acima? ")
                            break

                    else:
                        break

                elif material == "4":

                    kilo = float(input(f'Quantos quilos você tem: '))

                    print('''_________________
⎪ TIPOS DE PAPEL ⎪
⎪                ⎪
⎪ [1] - Branco   ⎪
⎪ [2] - Mista    ⎪
⎪ [3] - Papelão  ⎪
⎪ [4] - Voltar   ⎪
⎪________________⎪
 ''')

                    papel = input("Qual tipo de papel voce possuí? ")

                    while papel != "4":

                        if papel != "1" and papel != "2" and papel != "3":
                            papel = input("Escolha inválida, digite um número referente ao menu acima ")

                        elif papel == "1":
                            valor = kilo * 0.45
                            print(f"Você receberá por {kilo} quilos de papel branco R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menu acima? ")
                            break

                        elif papel == "2":
                            valor = kilo * 0.2
                            print(f"Você receberá por {kilo} quilos de asparas mista R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menu acima? ")
                            break

                        else:
                            valor = kilo * 0.15
                            print(f"Você receberá por {kilo} quilos de papelão  R$ {valor}")

                            menu_inicial()
                            escolha_inicial = input("Qual opção deseja escolher do menu acima? ")
                            break

                    else:
                        break

                else:

                    menu_inicial()
                    escolha_inicial = input("Escolha uma opção do menu acima ")

                break

        else:
            titulo("PROGRAMA FINALIZADO")
            quit()

    else:
        titulo("PROGRAMA FINALIZADO")
        quit()

else:
    titulo("PROGRAMA FINALIZADO")
    quit()



