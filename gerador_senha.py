# Gerador de senhas

# Importação das bibliotecas da aplicação.

import random
from time import sleep

# Variáveis (todas tratadas como strings).

letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
letras_maiusculas = letras_minusculas.upper()
numeros = '0123456789'
caracteres = '[]{}()*#;/,-_%'

# Perguntando ao usuário o tamanho da senha.

# Qualquer valor considerado inválido é recusado, permitindo ao usuário
# tentar inserir outro valor.

# Valores inválidos são valores não numéricos ou menores que 8, que é
# considerado um ótimo tamanho mínimo para senhas fortes.

while (True):
    try:
        tamanho = int(input('Digite qual o tamanho da senha: '))
        if tamanho < 8:
            raise Exception
        break
    except:
        print('Por favor, insira um valor inteiro maior ou igual a 8.')

# Gerando a senha com todos os caracteres

todos_caracteres = letras_minusculas + letras_maiusculas + numeros + caracteres
senha = ''.join(random.sample(todos_caracteres, tamanho))
print('Gerando sua senha...')
sleep(2)
print(f'A sua senha é: {senha}.')

