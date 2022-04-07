def media():
    notas = [0, 0, 0, 0, 0]  #Lista com número predeterminado de notas(tem 5 mas serão lidas 4 pois iniciaremos no índice 1)
    soma = 0
    indice = 0  #Variável contadora, referente aos indices da lista
    print('Bem vindo ao sistema de obtenção da média de notas de alunos, para começarmos:')
    opcao = 1
    while opcao == 1: #Torna possível a repetição do processo que poderá ser feito opcionalmente no final do loop para outro aluno, por exemplo
        nome_aluno = input('Digite o nome do aluno:')  # entrada de dados
        for indice in range(1, 5):  #Assim, ignora o indice 0 e range, que deixa de fora o último índice, aqui deixa um índice inexistente
            notas[indice] = input(f'Digite a {indice}° nota do aluno: ')  # entrada de dados para as notas no índice especificado
            soma = soma + float(notas[indice]) #acumulação das notas
            indice += 1 #incrementando 1 para que quando ocorrer a repetição, possa guardar a próxima nota em um próximo índice
        media = soma / (indice - 1)  #A subtração se dá devido ao número de indices, já que ignoramos o indice 0 para melhor estética no client-side
        print(f'A média correspondente às notas de {nome_aluno} é: {media}') #Saída dos dados processados acima
        if media < 5:
            print(f'{nome_aluno} está REPROVADO!')
        elif (media < 7):
            print(f'{nome_aluno} tem direito de realizar uma prova especial')
        else:
            print(f'{nome_aluno} foi APROVADO!')
        opcao=int(input('\n1-Caso deseje obter a média de outro aluno\n2-Caso deseje finalizar o programa\nDigite uma opção:'))
        while (opcao != 1) and (opcao != 2): #Loop até que uma opção válida seja digitada
            print('\n[ERRO]!Opcão inválida!\n1-Obter a média de determinado aluno\n2-Finalizar o programa')
            opcao = int(input('Digite uma opção válida:'))
        if opcao == 2:
            print('\nPrograma finalizado!')
media()