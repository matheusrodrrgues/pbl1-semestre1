#******************************************************************************************
# Autor: Matheus Silva Rodrigues
# Componente Curricular: Algoritmos I
# Concluido em: 17 de Setembro de 2024
# Declaro que este código foi elaborado por mim de forma individual e não contém nenhum
# trecho de código de outro colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da Internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação para o autor e a fonte
# do código, e estou ciente que estes trechos não serão considerados para fins de avaliação.
# Sistema Operacional: Windows 10
#******************************************************************************************/

# De início, o código solicita os dados das 5 equipes para o processamento e cálculo necessário.
# Como são 5 equipes, é necessário que são 5 variáveis.

Menu = 0
while Menu != 4:
  print("\nMenu:")
  print("1. Opção 1 - Peso das Questões")
  print("2. Opção 2 - Processamento dos dados das equipes")
  print("3. Opção 3 - Classificação final do ranking")
  print("4. Sair")

  opcao = input("Escolha uma opção para o ranking: ")

  if opcao == "1":
    print("Você escolheu a Opção 1")
    # Nesta seção, as três variáveis são implementadas para gerar os pesos (onde o usuário insere) das questões respondidas.
    peso_facil = float(input("Digite o valor do problema fácil: "))
    peso_medio = float(input("Digite o valor do problema médio: "))
    peso_dificil = float(input("Digite o valor do problema difícil: "))
    print('')

  elif opcao == "2":
    print("Você escolheu a Opção 2")

    # Sequência de códigos de entrada da Equipe. Nessa seção, o usuário insere as 5 variáveis padrão da equipe. Nome, quantidade de questões respondidas (por divisão)
    # E o tempo em minutos. A pontuação1 gera o calculo dos valores das questões.
    # Essa sequência se repete pelo código, mudando de "1" e indo até "5"
    nome_equipe1 = input("EQUIPE 1: Digite o nome: ")
    equipe1_qf = int(input("EQUIPE 1: Digite a quantidade de questões fáceis respondida: "))
    equipe1_qm = int(input("EQUIPE 1: Digite a quantidade de questões médias respondidka: "))
    equipe1_qd = int(input("EQUIPE 1: Digite a quantidade de questões difíceis respondida: "))
    tempo1 = float(input("EQUIPE 1: Digite o tempo levado para responder (em seg): "))
    pontuacao1 = (equipe1_qf * peso_facil) + (equipe1_qm * peso_medio) + (equipe1_qd * peso_dificil)

    # Seção para o primeiro ranking, onde, como só tem a primeira equipe, é gerado o ranking pra ela mesmo.
    ranking1 = nome_equipe1
    rank1_qf = equipe1_qf
    rank1_qm = equipe1_qm
    rank1_qd = equipe1_qd
    rank1_tem = tempo1
    rank1_pon = pontuacao1

    print('')

    # 1° Ranking de processamento de dados;
    print('------------------------------------------')
    print ('O ranking atual está com a equipe: ', ranking1) 
    print('------------------------------------------')

    # Sequência de códigos de entrada da Equipe. Nessa seção, o usuário insere as 5 variáveis padrão da equipe. Nome, quantidade de questões respondidas (por divisão)
    # E o tempo em minutos. A pontuação1 gera o calculo dos valores das questões.
    # Essa sequência se repete pelo código, mudando de "1" e indo até "5"
    print('')
    nome_equipe2 = input("EQUIPE 2: Digite o nome: ")
    equipe2_qf = int(input("EQUIPE 2: Digite a quantidade de questões fáceis respondida: "))
    equipe2_qm = int(input("EQUIPE 2: Digite a quantidade de questões médias respondida: "))
    equipe2_qd = int(input("EQUIPE 2: Digite a quantidade de questões difíceis respondida: "))
    tempo2 = float(input("EQUIPE 2: Digite o tempo levado para responder (em seg): "))
    pontuacao2 = (equipe2_qf * peso_facil) + (equipe2_qm * peso_medio) + (equipe2_qd * peso_dificil)
    print('')

    # Já neste ranking, começa as comparações entre Equipe 1 e Equipe 2, onde, nos próximos, irão ocorrer por sequência. Nesse "if", encontra-se a comparação entre 
    # pontuação 1 e pontuação 2, tendo como critério de desempate o tempo e a quantidade de questões dificéis.
    if pontuacao2 > rank1_pon or pontuacao2 == rank1_pon and (equipe2_qd > rank1_qd or (equipe2_qd == rank1_qd and tempo2 < rank1_tem)):
        ranking2 = ranking1
        rank2_qf = rank1_qf
        rank2_qm = rank1_qm
        rank2_qd = rank1_qd
        rank2_tem = rank1_tem
        rank2_pon = rank1_pon

        ranking1 = nome_equipe2
        rank1_qf = equipe2_qf
        rank1_qm = equipe2_qm
        rank1_qd = equipe2_qd
        rank1_tem = tempo2
        rank1_pon = pontuacao2

    else:
        ranking2 = nome_equipe2
        rank2_qf = equipe2_qf
        rank2_qm = equipe2_qm
        rank2_qd = equipe2_qd
        rank2_tem = tempo2
        rank2_pon = pontuacao2

    # 2° Ranking de processamento de dados
    print('------------------------------------------')
    print ('O ranking atual está com a equipe: ', ranking1) 
    print ('O segundo lugar está com a equipe: ', ranking2) 
    print('------------------------------------------')

    # Sequência de códigos de entrada da Equipe. Nessa seção, o usuário insere as 5 variáveis padrão da equipe. Nome, quantidade de questões respondidas (por divisão)
    # E o tempo em minutos. A pontuação1 gera o calculo dos valores das questões.
    # Essa sequência se repete pelo código, mudando de "1" e indo até "5"
    print('')
    nome_equipe3 = input("EQUIPE 3: Digite o nome: ")
    equipe3_qf = int(input("EQUIPE 3: Digite a quantidade de questões fáceis respondida: "))
    equipe3_qm = int(input("EQUIPE 3: Digite a quantidade de questões médias respondida: "))
    equipe3_qd = int(input("EQUIPE 3: Digite a quantidade de questões difíceis respondida: "))
    tempo3 = float(input("EQUIPE 3: Digite o tempo levado para responder (em seg): "))
    pontuacao3 = (equipe3_qf * peso_facil) + (equipe3_qm * peso_medio) + (equipe3_qd * peso_dificil)
    print('')

    # Já neste ranking, começa as comparações entre Equipe 1, 2 e Equipe 3, onde, nos próximos, irão ocorrer por sequência. Nesse "if", encontra-se a comparação entre 
    # pontuação 3, 2 e 1, tendo como critério de desempate o tempo e a quantidade de questões dificéis.
    if pontuacao3 > rank1_pon or pontuacao3 == rank1_pon and (equipe3_qd > rank1_qd or (equipe3_qd == rank1_qd and tempo3 < rank1_tem)):
        ranking3 = ranking2
        rank3_qf = rank2_qf
        rank3_qm = rank2_qm
        rank3_qd = rank2_qd
        rank3_tem = rank2_tem
        rank3_pon = rank2_pon

        ranking2 = ranking1
        rank2_qf = rank1_qf
        rank2_qm = rank1_qm
        rank2_qd = rank1_qd
        rank2_tem = rank1_tem
        rank2_pon = rank1_pon

        ranking1 = nome_equipe3
        rank1_qf = equipe3_qf
        rank1_qm = equipe3_qm
        rank1_qd = equipe3_qd
        rank1_tem = tempo3
        rank1_pon = pontuacao3

    elif pontuacao3 > rank2_pon or pontuacao3 == rank2_pon and (equipe3_qd > rank2_qd or (equipe3_qd == rank2_qd and tempo3 < rank2_tem)):
        ranking3 = ranking2
        rank3_qf = rank2_qf
        rank3_qm = rank2_qm
        rank3_qd = rank2_qd
        rank3_tem = rank2_tem
        rank3_pon = rank2_pon

        ranking2 = nome_equipe3
        rank2_qf = equipe3_qf
        rank2_qm = equipe3_qm
        rank2_qd = equipe3_qd
        rank2_tem = tempo3
        rank2_pon = pontuacao3

    else:
        ranking3 = nome_equipe3
        rank3_qf = equipe3_qf
        rank3_qm = equipe3_qm
        rank3_qd = equipe3_qd
        rank3_tem = tempo3
        rank3_pon = pontuacao3

    # 3° Ranking de processamento de dados
    print('------------------------------------------')
    print ('O ranking atual está com a equipe: ', ranking1) 
    print ('O segundo lugar está com a equipe: ', ranking2) 
    print ('O terceiro lugar está com a equipe: ', ranking3) 
    print('------------------------------------------')

    # Sequência de códigos de entrada da Equipe. Nessa seção, o usuário insere as 5 variáveis padrão da equipe. Nome, quantidade de questões respondidas (por divisão)
    # E o tempo em minutos. A pontuação1 gera o calculo dos valores das questões.
    # Essa sequência se repete pelo código, mudando de "1" e indo até "5"
    print('')
    nome_equipe4 = input("EQUIPE 4: Digite o nome: ")
    equipe4_qf = int(input("EQUIPE 4: Digite a quantidade de questões fáceis respondida: "))
    equipe4_qm = int(input("EQUIPE 4: Digite a quantidade de questões médias respondida: "))
    equipe4_qd = int(input("EQUIPE 4: Digite a quantidade de questões difíceis respondida: "))
    tempo4 = float(input("EQUIPE 4: Digite o tempo levado para responder (em seg): "))
    pontuacao4 = (equipe4_qf * peso_facil) + (equipe4_qm * peso_medio) + (equipe4_qd * peso_dificil)
    print('')

    # Já neste ranking, começa as comparações entre Equipe 1, 2, 3 e Equipe 4, onde, nos próximos, irão ocorrer por sequência. Nesse "if", encontra-se a comparação entre 
    # pontuação 4, 3, 2 e 1, tendo como critério de desempate o tempo e a quantidade de questões dificéis.
    if pontuacao4 > rank1_pon or pontuacao4 == rank1_pon and (equipe4_qd > rank1_qd or (equipe4_qd == rank1_qd and tempo4 < rank1_tem)):
        ranking4 = ranking3
        rank4_qf = rank3_qf
        rank4_qm = rank3_qm
        rank4_qd = rank3_qd
        rank4_tem = rank3_tem
        rank4_pon = rank3_pon

        ranking3 = ranking2
        rank3_qf = rank2_qf
        rank3_qm = rank2_qm
        rank3_qd = rank2_qd
        rank3_tem = rank2_tem
        rank3_pon = rank2_pon

        ranking2 = ranking1
        rank2_qf = rank1_qf
        rank2_qm = rank1_qm
        rank2_qd = rank1_qd
        rank2_tem = rank1_tem
        rank2_pon = rank1_pon

        ranking1 = nome_equipe4
        rank1_qf = equipe4_qf
        rank1_qm = equipe4_qm
        rank1_qd = equipe4_qd
        rank1_tem = tempo4
        rank1_pon = pontuacao4

    elif pontuacao4 > rank2_pon or  pontuacao4 == rank2_pon and (equipe4_qd > rank2_qd or (equipe4_qd == rank2_qd and tempo4 < rank2_tem)):
        ranking4 = ranking3
        rank4_qf = rank3_qf
        rank4_qm = rank3_qm
        rank4_qd = rank3_qd
        rank4_tem = rank3_tem
        rank4_pon = rank3_pon

        ranking3 = ranking2
        rank3_qf = rank2_qf
        rank3_qm = rank2_qm
        rank3_qd = rank2_qd
        rank3_tem = rank2_tem
        rank3_pon = rank2_pon

        ranking2 = nome_equipe4
        rank2_qf = equipe4_qf
        rank2_qm = equipe4_qm
        rank2_qd = equipe4_qd
        rank2_tem = tempo4
        rank2_pon = pontuacao4

    elif pontuacao4 > rank3_pon or pontuacao4 == rank3_pon and (equipe4_qd > rank3_qd or (equipe4_qd == rank3_qd and tempo4 < rank3_tem)):
        ranking4 = ranking3
        rank4_qf = rank3_qf
        rank4_qm = rank3_qm
        rank4_qd = rank3_qd
        rank4_tem = rank3_tem
        rank4_pon = rank3_pon

        ranking3 = nome_equipe4
        rank3_qf = equipe4_qf
        rank3_qm = equipe4_qm
        rank3_qd = equipe4_qd
        rank3_tem = tempo4
        rank3_pon = pontuacao4

    else:
        ranking4 = nome_equipe4
        rank4_qf = equipe4_qf
        rank4_qm = equipe4_qm
        rank4_qd = equipe4_qd
        rank4_tem = tempo4
        rank4_pon = pontuacao4

    # 4° Ranking de processamento de dados
    print('------------------------------------------')
    print ('O ranking atual está com a equipe: ', ranking1) 
    print ('O segundo lugar está com a equipe: ', ranking2) 
    print ('O terceiro lugar está com a equipe: ', ranking3) 
    print ('O quarto lugar está com a equipe: ', ranking4) 
    print('------------------------------------------')

    # Sequência de códigos de entrada da Equipe. Nessa seção, o usuário insere as 5 variáveis padrão da equipe. Nome, quantidade de questões respondidas (por divisão)
    # E o tempo em minutos. A pontuação1 gera o calculo dos valores das questões.
    # Essa sequência se repete pelo código, mudando de "1" e indo até "5"
    print('')
    nome_equipe5 = input("EQUIPE 5: Digite o nome: ")
    equipe5_qf = int(input("EQUIPE 5: Digite a quantidade de questões fáceis respondida: "))
    equipe5_qm = int(input("EQUIPE 5: Digite a quantidade de questões médias respondida: "))
    equipe5_qd = int(input("EQUIPE 5: Digite a quantidade de questões difíceis respondida: "))
    tempo5 = float(input("EQUIPE 5: Digite o tempo levado para responder (em seg): "))
    pontuacao5 = (equipe5_qf * peso_facil) + (equipe5_qm * peso_medio) + (equipe5_qd * peso_dificil)
    print('')

    # Já neste ranking, começa as comparações entre Equipe 1, 2, 3, 4 e Equipe 5, onde, nos próximos, irão ocorrer por sequência. Nesse "if", encontra-se a comparação entre 
    # pontuação 5, 4, 3, 2 e 1, tendo como critério de desempate o tempo e a quantidade de questões dificéis.
    if pontuacao5 > rank1_pon or pontuacao5 == rank1_pon and (equipe5_qd > rank1_qd or (equipe5_qd == rank1_qd and tempo5 < rank1_tem)):
        ranking5 = ranking4
        rank5_qf = rank4_qf
        rank5_qm = rank4_qm
        rank5_qd = rank4_qd
        rank5_tem = rank4_tem
        rank5_pon = rank4_pon

        ranking4 = ranking3
        rank4_qf = rank3_qf
        rank4_qm = rank3_qm
        rank4_qd = rank3_qd
        rank4_tem = rank3_tem
        rank4_pon = rank3_pon

        ranking3 = ranking2
        rank3_qf = rank2_qf
        rank3_qm = rank2_qm
        rank3_qd = rank2_qd
        rank3_tem = rank2_tem
        rank3_pon = rank2_pon

        ranking2 = ranking1
        rank2_qf = rank1_qf
        rank2_qm = rank1_qm
        rank2_qd = rank1_qd
        rank2_tem = rank1_tem
        rank2_pon = rank1_pon

        ranking1 = nome_equipe5
        rank1_qf = equipe5_qf
        rank1_qm = equipe5_qm
        rank1_qd = equipe5_qd
        rank1_tem = tempo5
        rank1_pon = pontuacao5

    elif pontuacao5 > rank2_pon or  pontuacao5 == rank2_pon and (equipe5_qd > rank2_qd or (equipe5_qd == rank2_qd and tempo5 < rank2_tem)):
        ranking5 = ranking4
        rank5_qf = rank4_qf
        rank5_qm = rank4_qm
        rank5_qd = rank4_qd
        rank5_tem = rank4_tem
        rank5_pon = rank4_pon

        ranking4 = ranking3
        rank4_qf = rank3_qf
        rank4_qm = rank3_qm
        rank4_qd = rank3_qd
        rank4_tem = rank3_tem
        rank4_pon = rank3_pon

        ranking3 = ranking2
        rank3_qf = rank2_qf
        rank3_qm = rank2_qm
        rank3_qd = rank2_qd
        rank3_tem = rank2_tem
        rank3_pon = rank2_pon

        ranking2 = nome_equipe5
        rank2_qf = equipe5_qf
        rank2_qm = equipe5_qm
        rank2_qd = equipe5_qd
        rank2_tem = tempo5
        rank2_pon = pontuacao5

    elif pontuacao5 > rank3_pon or  pontuacao5 == rank3_pon and (equipe5_qd > rank3_qd or (equipe5_qd == rank3_qd and tempo5 < rank3_tem)):
        ranking5 = ranking4
        rank5_qf = rank4_qf
        rank5_qm = rank4_qm
        rank5_qd = rank4_qd
        rank5_tem = rank4_tem
        rank5_pon = rank4_pon

        ranking4 = ranking3
        rank4_qf = rank3_qf
        rank4_qm = rank3_qm
        rank4_qd = rank3_qd
        rank4_tem = rank3_tem
        rank4_pon = rank3_pon

        ranking3 = nome_equipe5
        rank3_qf = equipe5_qf
        rank3_qm = equipe5_qm
        rank3_qd = equipe5_qd
        rank3_tem = tempo5
        rank3_pon = pontuacao5

    elif pontuacao5 > rank4_pon or  pontuacao5 == rank4_pon and (equipe5_qd > rank4_qd or (equipe5_qd > rank4_qd and tempo5 < rank4_tem)):
        ranking5 = ranking4
        rank5_qf = rank4_qf
        rank5_qm = rank4_qm
        rank5_qd = rank4_qd
        rank5_tem = rank4_tem
        rank5_pon = rank4_pon

        ranking4 = nome_equipe5
        rank4_qf = equipe5_qf
        rank4_qm = equipe5_qm
        rank4_qd = equipe5_qd
        rank4_tem = tempo5
        rank4_pon = pontuacao5

    else:
        ranking5 = nome_equipe5
        rank5_qf = equipe5_qf
        rank5_qm = equipe5_qm
        rank5_qd = equipe5_qd
        rank5_tem = tempo5
        rank5_pon = pontuacao5
  elif opcao == "3":
    print("Você escolheu a Opção 3")
    
    print('')

    # Apresentar ranking, onde, após o processamento dos 4º primeiros rankings, é gerada a classificação final, já incluindo o critério de desempate
    # gerado nos rankings anteriores.
    print('-----------------CLASSIFICAÇÃO DAS EQUIPES------------------------')
    print(f"1º lugar: {ranking1} | Pontuação: {rank1_pon:.2f} | Quantidade de questõe dificeis: {rank1_qd}")
    print(f"2º lugar: {ranking2} | Pontuação: {rank2_pon:.2f} | Quantidade de questõe dificeis: {rank2_qd}")
    print(f"3º lugar: {ranking3} | Pontuação: {rank3_pon:.2f} | Quantidade de questõe dificeis: {rank3_qd}")
    print(f"4º lugar: {ranking4} | Pontuação: {rank4_pon:.2f} | Quantidade de questõe dificeis: {rank4_qd}")
    print(f"5º lugar: {ranking5} | Pontuação: {rank5_pon:.2f} | Quantidade de questõe dificeis: {rank5_qd}")
    print('------------------------------------------------------------------')
    # Média de pontuação de todas as equipes;
    media = (rank1_pon + rank2_pon + rank3_pon + rank4_pon + rank5_pon)/5
    print(f"\nParabéns! A equipe vencedora é a {ranking1} e resolveu com o tempo de {rank1_tem} minutos.")
    print(f"A média de todas as equipes juntas somaram: {media}")

  elif opcao == "4":
    print("Saindo...")
    break
  else:
    print("Olá, não existe essa opção!")
# Fim do código! =)
