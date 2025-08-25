# Imprime o menu de opções para o usuário
print('Café Padrão --> R$10,00 \nCafé Expresso --> R$20,00')

# Inicia um loop infinito que só será quebrado com uma entrada válida
while True:
    # Pede a entrada, remove espaços extras e formata para a primeira letra maiúscula
    cof = str(input('\nQual café você deseja encomendar (Padrão/Expresso): ')).strip().capitalize()

    # Verifica se a escolha é uma das opções válidas
    if cof == 'Padrão':
        print('\nCafé "PADRÃO" a caminho...')
        break  # Sai do loop, pois a escolha foi válida
    elif cof == 'Expresso':
        print('\nCafé "EXPRESSO" a caminho...')
        break  # Sai do loop, pois a escolha foi válida
    else:
        # Informa ao usuário que a opção é inválida e o loop continua
        print('\nProduto inválido, por favor tente novamente.')