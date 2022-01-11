# PEDIR O NOME E SAUDAÇÃO
nome = str(input('Olá,Qual é o seu nome? '))
print('Prazer em te conhecer {:-^20} !'.format(nome))
# O CÓDIGO {:} VAI FAZER O LINK ENTRE A SENTENÇA E O NOME
print('Olha que interessante,{:}:'.format(nome))
# VARIÁVEIS
n1: int = float(input('Digite um valor:'))
n2: int = float(input('Digite outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
# APLICAR OPERAÇÕES DE SOMA, SUBTRAÇÃO, DIVISÃO, POTÊNCIA...ETC
print ('Vamos ver as operações:')
print ('A soma vale: {}, o produto vale: {} e a divisão é: {:.4f}'.format(s,m,d),end = '>>>>')
print (' A divisão inteira vale: {} e a potência vale: {}'.format(di,e))
