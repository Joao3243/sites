from orgaos import *
cabeçalho('Banco JH')
menor=False
nome_usuario=leiaString('Nome completo: ')
idade_usuario=leiaInt('Idade: ')
if idade_usuario<18:
    menor=True
if menor:
    nome_maior=leiaString('Nome Completo do Maior: ')
    idade_maior=leiaInt('Idade do Maior: ')
    while idade_maior<18:
        idade_maior=leiaInt('Idade do Maior: ')
    print(f'Será cobrado no cartão de {nome_maior}')
print('Seu cartão ficará assim')
parte1=NumA(1000,9999)
parte2=NumA(1000,9999)
parte3=NumA(1000,9999)
parte4=NumA(1000,9999)
cartão=f'{parte1}     {parte2}     {parte3}     {parte4}'
cart_seg_1=NumA(1,9)
cart_seg_2=NumA(1,9)
cart_seg_3=NumA(1,9)
cart_seg=f'{cart_seg_1}{cart_seg_2}{cart_seg_3}'
linha('-=')
print(f'{cartão:^56}')
print(f'{cart_seg:^56}')
linha('-=')
while True:
    if menor:
        cart_resp_1=leiaInt('Primeira parte do cartão do responsável: ')
        cart_resp_2=leiaInt('Segunda parte do cartão do responsável: ')
        cart_resp_3=leiaInt('Terça parte do cartão do responsável: ')
        cart_resp_4=leiaInt('Quarta parte do cartão do responsável: ')
        resp=leiaResp(f'Então será cobrado no cartão |{cart_resp_1}     {cart_resp_2}     {cart_resp_3}     {cart_resp_4}|. Correto? [S/N] ')
        if resp in 'S':
            break
print('Muito Obrigado por escolher nosso banco como banco oficial. Banco JH,você não vai até o banco,o banco vai até você.')



