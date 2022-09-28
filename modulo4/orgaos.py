def Desconto(por,pre):
    porc=(pre*por)/100
    des=pre-porc
    return des
def Aumento(por,pre):
    porc=(pre*por)/100
    aum=pre-porc
    return aum
def linha(tip):
    print(tip *30)
def cabeçalho(msg):
    linha('-=')
    print(f'{msg:^56}')
    linha('-=')
def leiaInt(msg):
    valor=0
    while True:
        try:
            valor=int(input(msg))
        except:
            print('\033[1;31mErro!!!Digite um número inteiro válido\033[m')
        else:
            break
    return valor
def leiaString(msg):
    valor=''
    while True:
        try:
            valor=str(input(msg))
        except:
            print('\033[1;31mErro ao enviar a mensagem')
        else:
            break
    return valor
def NumA(n1,n2):
    from random import randint
    num=randint(n1,n2)
    return num
def leiaResp(msg):
    resp=leiaString(msg).strip().upper()[0]
    while resp not in 'SN':
        resp=leiaString(msg).strip().upper()[0]
    return resp
