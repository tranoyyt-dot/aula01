mt = str(input(' Informe o método de pagamento (cartao/boleto):'))
if(mt == 'cartao'):
    print('Processo de pagamento no cartão...')
elif(mt == 'boleto'):
    print('Gerando boleto bancário...')
else:
    print('Método de pagamento não reconhecido.')