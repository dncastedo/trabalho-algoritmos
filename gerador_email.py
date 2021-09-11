#Programa que recebe o nome, sobrenome e matricula do usuário e gera um e-mail utilizando a primeira letra do nome, o sobrenome e os dois últimos dígitos do RU.

#Dados fornecidos pelo usuário
nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
matricula = input('Digite o seu RU com sete dígitos: ')

# Função que recebe como parâmetro os dados fornecidos pelo usário, sendo duas strings (nome e sobrenome) e um número inteiro(matricula)
#Posteriormente será feito o teste das condições para verificar o tamanho das strings e extrair o primeiro caractere do nome para concatenar com o sobrenome e os dois últimos dígitos da matrícula, formando o email com o domínio fornecido.
def gerador_email(nome: str, sobrenome: str, matricula: int):
    if len(nome) > 0 and len(sobrenome) > 0 and len(matricula) > 0:
        email = nome[0].lower() + sobrenome.lower() + matricula[5:] + '@algoritmos.com.br'

#Por último será exibida na tela a frase com os dados concatenados e o email gerado.
        return 'Sra. ' + nome + ' ' + sobrenome + ', seu e-mail é: ' + email
print(gerador_email(nome, sobrenome, matricula))
