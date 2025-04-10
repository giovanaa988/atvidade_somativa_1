#Aluna: Giovana Marquette Bellisario // Curso: Análise e Desenvolvimento de Sistemas.

lista_estudante = []

#Primeira estrutura de repetição.
while True:

    #Mostrando o menu
    print(" ")
    print("***************** MENU PRINCIPAL! *****************")
    print("(1) Gerenciar estudantes.")
    print("(2) Gerenciar disciplina.")
    print("(3) Gerenciar professores.")
    print("(4) Gerenciar turmas.")
    print("(5) Gerenciar matrículas.")
    print("(0) Sair.")
    print(" ")

    #Pedindo ao usuário uma opção.
    opcao = input("Informe a opção desejada: ")

    #Opções válidas: 1.
    #Para finalizar o programa: 0.
    if opcao == '1':
        print(" ")

        #Segunda estrutura de repetição.
        while True:

            #Mostrando o menu secundário.
            #Opções válidas: 1, 2, 3 e 4.
            #Para voltar: 5.
            print(f"----------------- [{opcao}] MENU DE OPERAÇÕES! -----------------")
            print(" ")
            print("(1) Incluir.")
            print("(2) Listar.")
            print("(3) Atualizar.")
            print("(4) Excluir.")
            print("(5) Voltar ao menu principal.")
            print(" ")

            #Solicitando ao usuário, novamente, a escolha de uma opção.
            print("Escolha a próxima opção!")
            print(" ")
            opcao_secundaria = input("Informe a ação desejada: ")
            print(" ")

            #Inclusão de nomes para serem armazenados na lista de estudantes.
            if opcao_secundaria == '1':
                print("==================== INCLUSÃO DE ESTUDANTES ====================")
                print(" ")
                #Solicitando a entrada do nome.
                nome = input(str("Digite o nome do(a) Estudante: "))
                print(" ")
                #Incluindo o nome na lista.
                lista_estudante.append(nome)
                #Organizando a lista em ordem alfabética.
                lista_estudante.sort()
                #E por fim, sinalizando a usuário que o nome foi incluído na lista.
                print("Estudante inluído com sucesso!")
                print(" ")

            #Opção de listagem.
            elif opcao_secundaria == '2':
                #Caso o usuário não inclua nenhum valor a lista, aparecerá uma mensagem indicando que a lista está vazia.
                if not lista_estudante:
                    print("Não há estudantes cadastrados!")
                    print(" ")

                #Quando houver estudantes incluidos, aparecerá a lista em ordem alfabética.
                else:
                    print("==================== LISTA DE ESTUDANTES ====================")
                    for i, nome in enumerate(lista_estudante, 1):
                        print(f"- {nome}")
                    print(" ")

            #As opções 3 e 4 não possuem funcionalidade até o momento, quando selecionadas apareceram como "Em desenvolvimento".
            elif opcao_secundaria == '3' or opcao_secundaria == '4':
                print("**************************** EM DESENVOLVIMENTO! ****************************")
                print("Essa aba encontra-se em desenvolvimento, aguarde.")
                print(" ")

            #A opção 5 realiza a quebra da segunda estrutura de repetição e faz com que o usuário retorne para o menu principal.
            elif opcao_secundaria == '5':
                print("Você voltou ao menu principal!")
                break

            #Esta mensagem aparecerá quando o usuário solicitar por qualquer número ou caractere diferente de 1, 2, 3, 4 e 5.
            else:
                print("Você escolheu uma opção inválida, tente novamente!")
                print(" ")

    #As opções 2, 3, 4 e 5 não possuem funcionalidade até o momento, quando selecionadas apareceram como "Em desenvolvimento".
    elif opcao in ['2', '3', '4', '5']:
        print(" ")
        print("**************************** EM DESENVOLVIMENTO! ****************************")
        print("Essa aba encontra-se em desenvolvimento, aguarde.")

    #A opção 0 realiza a quebra da segunda estrutura de repetição e faz com que o programa seja encerrado.
    elif opcao == '0':
        print(" ")
        print("Você pediu para sair!")
        break

    #Esta mensagem aparecerá quando o usuário solicitar por qualquer número ou caractere diferente de 1, 2, 3, 4, 5 e 0.
    else:
        print(" ")
        print("Você escolheu uma opção inválida, tente novamente!")

print(" ")