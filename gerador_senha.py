#Gerador de senhas

#Importação das bibliotecas da aplicação.
import random
from time import sleep

#Variáveis (Todas tratadas como strings).
letras_minusculas = 'abcdefghijklmnopqrstuvwxyz'
letras_maiusculas = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
caracteres = '[]{}()*#;/,-_%'

# Perguntando ao usuário o tamanho da senha.
tamanho = input('Digite qual o tamanho da senha: ')

#Convertendo para os cálculos
tamanho_int = int(tamanho)
length = tamanho_int

#Gerando a senha com todos os caracteres
todos_caracteres = letras_minusculas + letras_maiusculas + numeros + caracteres
senha = ''.join(random.sample(todos_caracteres,length))
print('Gerando sua senha...')
sleep(2)
print(f'A sua senha é: {senha}')