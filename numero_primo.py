#Verifica se o numero é primo
#PRIMO - numero primo tem apenas dois divisores - divisivel por 1 e por ele mesmo (não tem resto).
#Se o resto da divisão for DIFERENTE de zero ENTÃO o numero é primo
#Se o resto da divisão for IGUAL a zero ENTÂO o numero não é primo

numero = int(input('Digite um numero: '))

if numero == 1:
    print(f'{numero} não é primo')
elif numero%2!=0 or numero == 2:
    print(f'{numero} é primo')
elif numero%2==0:
    print(f'{numero} não é primo')

# def test_retorna_numero_primo():
#     assert primo(2) == "numero primo"



