#Verifica se o numero é primo
#PRIMO - numero primo tem apenas dois divisores - divisivel por 1 e por ele mesmo (não tem resto).
#Se o resto da divisão for DIFERENTE de zero ENTÃO o numero é primo
#Se o resto da divisão for IGUAL a zero ENTÂO o numero não é primo

print('**********************************\n'
      '********* NUMERO PRIMO ***********\n'
      '**********************************\n'
)


numero = int(input('Digite um numero: '))
multiplo = 0

for count in range(2,numero):
    if (numero % count == 0):
        print("Multiplo de", count)
        multiplo += 1
if multiplo == 0:
    print(f'{numero} é primo')
else:
    print(f'{numero} Não é primo')




