valor1 = input('Digite um valor: ')
while True:
  try:
    print('-'*25)
    valor1 = float(valor1)
    print(f'O valor de {valor1} foi convertido com sucesso!')
    break
  except ValueError as erro:
    print(f'Não foi possivel converter "{valor1}" em número')
    print(erro)
    print('-'*25)
    valor1 = input('Digite o valor novamente: ')
