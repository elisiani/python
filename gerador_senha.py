import string
import random
import time

#Gerar senha segura - 12 caracters (3 letras maiúsculas, 3 minusculas, 3 digitos e 3 pontos
#Salvar a senha em um arquivo

# base = string.ascii_letters
# print(base)

#variaveis
maiuscula = random.choices(string.ascii_uppercase,k=3)
minuscula = random.choices(string.ascii_lowercase,k=3)
digitos = random.choices(string.digits,k=3)
ponts = random.choices(string.punctuation,k=3)

senha = random.sample(maiuscula+minuscula+digitos+ponts,12)
senha_segura = ''.join(senha)
#criar o arquivo
horario=time.strftime('%d/%m/%Y %H:%M:%S')
with open('senha.txt','a') as file :
    file.write(f'A senha foi gerada em: {horario}\n')
    file.write(f'Senha: {senha_segura}\n')
print(senha_segura)


