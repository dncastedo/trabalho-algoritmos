#Conforme orientação do exercício foi feita a importação da biblioteca ran-dom.
import random
#Criada lista vazia para que sejam inclusos os nomes do doadores.
doadores = []

#Criada função que recebe o nome do doador e multiplica ele a cada dez re-ais doados. Retornando a lista populada com o nome do doador de acordo com a quantia doada.
def nome_doador(nome: str, doacao: float):
    doadores.extend(((nome + ' ') * int(doacao // 10)).split())
    return

# Função realiza o sorteio do nome dos doadores. 
def sorteado():
    random.shuffle(doadores)
    return random.choice(doadores)

#Laço de repetição criado para exibir uma tela com a opção de cadastrar um doador (SIM - 10) ou não (NÃO - 0). 
#Se o usuário optar por não cadastrar novos usuários após o cadastro do primeiro nome, o programa realiza o sorteio. Caso contrário, exibe tela pa-ra que o usuário insira as informações solicitadas.
while True:
    escolha = int(input('Deseja cadastrar doadores? 0 - Não     1 - Sim '))
    if escolha == 0:
        break
    doador = input('Nome do doador: ')
    valor = float(input('Valor da doação: '))

    nome_doador(doador, valor)

# Verifica se a lista de doadores for maior que 0 executa o sorteio e exibe a lista com todos os doadores cadastrados e o ganhador do sorteio.
if len(doadores) > 0:
    print('Lista de doadores cadastrados: {}'.format(doadores))
    print('O(A) ganhador(a) do sorteio foi: {}'.format(sorteado()))

