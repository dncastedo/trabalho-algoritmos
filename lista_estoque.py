#Algoritmo criado para organizar uma lista de estoque e inserir novos produtos.

#Criada lista vazia para receber os valores que serão armazenados.

lista = []

#Criada uma função que recebe e armazena os novos produtos na lista dicio-nário.
def entrada_produto(cadastrar_produto: dict):
    lista.append(cadastrar_produto)
    return

#Programa exibe tela de escolha para cadastro de produtos, sendo o número 1 para cadastrar e o 0 para passar diretamente para lista, caso haja produtos cadastrados.
escolha = int(input('Deseja cadastrar um novo produto? 0 - Não     1 - Sim '))

#Enquanto a opção for de cadastro de produtos, o programa continua armaze-nando os dados digitados.
while escolha == 1:
    novo_produto = {}

#Tela de cadastro de códigos
    novo_produto['codigo'] = int(input('Digite o código do produto: '))

# Verificação criada para que o programa interrompa sua execução caso o có-digo do produto seja zero
    if novo_produto['codigo'] == 0:
        print('Código 0, encerrando cadastro de produtos.')
        break

#Tela de cadastro de novos produtos e estoque
    novo_produto['estoque'] = int(input('Digite a quantidade em estoque: '))
    novo_produto['minimo'] = int(input('Digite a quantidade mínima do esto-que: '))

    entrada_produto(novo_produto)
    escolha = int(input('Cadastrar produto? 0 - Não     1 - Sim '))

#Verifica se há algum produto cadastrado na lista e a exibe para o usuário de forma ordenada e com espaçamento entre os itens.
if len(lista) > 0:
    print('Lista de produtos por código em ordem crescente:')
    print("Código".center(10), end='')
    print("Estoque".center(10), end='')
    print("Mínimo".center(10))

    for produto in sorted(lista, key=lambda item: item['codigo']):
        print(str(produto['codigo']).center(10), end='')
        print(str(produto['estoque']).center(10), end='')
        print(str(produto['minimo']).center(10))

#Caso não haja produtos cadastrados exibe a mensagem de lista vazia.
else:
    print('Lista vazia.')


