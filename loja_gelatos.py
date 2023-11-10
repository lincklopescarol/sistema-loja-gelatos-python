# mensagem de boas vindas com identificação
print('Bem-vindo a Loja de Gelados da Carolina Vitória Linck Lopes')
print('--------------------- Cardápio --------------------')
print('------| Tamanho | Cupuaçu (CP) | Açaí (AC) | ------')
print('------|    P    |   R$ 10,00   | R$ 12,00  | ------')
print('------|    M    |   R$ 15,00   | R$ 17,00  | ------')
print('------|    G    |   R$ 19,00   | R$ 21,00  | ------')
print('---------------------------------------------------')

acumulador = 0 # vai acumulando os valores
while True:
    sabor = input('Entre com o sabor desejado (CP/AC): ')
    if sabor != 'CP' and sabor != 'AC':
        print('Sabor inválido. Tente novamente')
        continue

    tamanho = input('Entre com o tamanho desejado (P/M/G): ')
    if tamanho != 'P' and tamanho != 'M'  and tamanho != 'G':
        print('Tamanho inválido. Tente novamente')
        continue  # volta ao início do loop

    if sabor == 'CP' and tamanho == 'P':
        acumulador = acumulador + 10
        print('Você pediu CUPUAÇU no tamanho P: RS$ 10,00')
    elif sabor == 'AC' and tamanho == 'P':
        acumulador = acumulador + 12
        print('Você pediu AÇAÍ no tamanho P: RS$ 12,00')
    elif sabor == 'CP' and tamanho == 'M':
        acumulador = acumulador + 15
        print('Você pediu CUPUAÇU no tamanho M: RS$ 15,00')
    elif sabor == 'AC' and tamanho == 'M':
        acumulador = acumulador + 17
        print('Você pediu AÇAÍ no tamanho M: RS$ 17,00')
    elif sabor == 'CP' and tamanho == 'G':
        acumulador = acumulador + 19
        print('Você pediu CUPUAÇU no tamanho G: RS$ 19,00')
    elif sabor == 'AC' and tamanho == 'G':
        acumulador = acumulador + 21
        print('Você pediu AÇAÍ no tamanho G: RS$ 21,00')

    mais_alguma_coisa = input('Deseja pedir mais algum Açaí ou Cupuaçu? (S/N)? ')
    if mais_alguma_coisa == 'S':
      continue # volta pro início do programa
    else:
      print('O valor total a ser pago: R${:.2f}'.format(acumulador))
      break # encerra o programa