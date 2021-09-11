
#Programa para inserção de dados: nome do aluno e sua nota final;
#Retorna o conceito no qual o aluno se enquadra de acordo com sua nota.

#Criei um laço de repetição em que o usuário deverá decidir se quer inserir dados (1- SIM) ou não (0 - NÃO)
while True:
    escolha = int(input('Deseja inserir dados? 0 - NÃO    1 - SIM '))
#Caso o usuário opte por não inserir os dados (0), o programa é finalizado sem testar as demais condições
    if escolha == 0:
        break
#Caso o usuário opte por inserir dados (1), o programa mostra dois campos onde deveráo ser informados o nome do aluno e a sua nota, em seguida serão testadas as condições para descobrir em qual conceito se enquadra a nota do aluno.
    nome_aluno = input('Digite o nome do aluno: ')
    nota_final = float(input('Digite a nota final do aluno: '))

#Em seguida é mostrada a mensagem com nome do aluno, sua nota e em qual conceito se enquadra.
    if nota_final >= 0.0 and nota_final >= 2.9:
        conceito = 'E'
        print('O(A) aluno(a) {} tirou nota {} e se enquadra no conceito {}'.format(nome_aluno, nota_final, conceito))
        
    elif nota_final >= 3.0 and nota_final <= 4.9:
        conceito = 'D'
        print('O(A) aluno(a) {} tirou nota {} e se enquadra no conceito {}'.format(nome_aluno, nota_final, conceito))
        
    elif nota_final >= 5.0 and nota_final <= 6.9:
        conceito = 'C'
        print('O(A) aluno(a) {} tirou nota {} e se enquadra no conceito {}'.format(nome_aluno, nota_final, conceito))
        
    elif nota_final >= 7.0 and nota_final <= 8.9:
        conceito = 'B'
        print('O(A) aluno(a) {} tirou nota {} e se enquadra no conceito {}'.format(nome_aluno, nota_final, conceito))
        
    elif nota_final >= 9.0 and nota_final <= 10.0:
        conceito = 'A'
        print('O(A) aluno(a) {} tirou nota {} e se enquadra no conceito {}'.format(nome_aluno, nota_final, conceito))

#Caso o usuário digite um dado diferente do pedido, o programa exibe a mensagem de 'Dado inválido. Encerrando programa'.
    else:
        print('Dados inválidos. Encerrando o programa')
        exit()

#Após, o programa exibe novamente a mensagem para que o usuario decida se quer continuar executando-o ou finalizá-lo.
print('Encerrando o programa')


