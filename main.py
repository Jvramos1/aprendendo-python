# primeiro projeto
'''
print("hello world!")

'''

#laços de repetição
'''
for palavra in range(1,4):
    print('carregando')

    for item in range(1,20):
        print(item)

        for item in range(1,20,2): # pulo de casas
            print(item)
'''

# coleçoes(listas)
'''
preco_1 = 20
preco_2 = 50
preco_3 = 200

precos = [20,50,200]
# indice  0  1   2  <= importante

print(precos[2])
'''

'''
some os valores dados uma coleçao de dados "idades" [15,46,75,34,23], 
imprima na tela a soma destes valores
'''
'''
idades = [15,46,75,34,23]
total = 0
for idade in idades:
    total = total + idade
    print(total)    
    '''

# aprendendo python
'''
nome = 'joao'
idade = 17

print(nome , idade)
'''
'''
nome = input('qual e seu nome?')

print('ola',nome, 'prazer em te conhecer!')
'''

'''
d = input('qual dia voce nasceu:')
m = input('e qual mes voce nasceu:')
a = input('e em qual ano:')
print('voce nasceu',d,'de',m,'de',a,'correto?')
'''

'''
n1 = input('primeiro numero ')
n2 = input('segundo numero ')

soma = int (n1) + int(n2)
print('a soma é ' + str(soma))
'''

'''
n1 = int (input('digite um numero '))
n2 = int (input('digite outro '))
s = n1 + n2
# print('a soma entre' ,n1, 'e' ,n2,'é' ,s)
print('a soma entre {} e {} vale {}'.format(n1,n2,s)) # <== mais pratico 
'''
'''
n1 = int(input("um valor " ))
n2 = int(input("outro valor "))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print('a soma e {} \n a multiplicacao e {} \n e a divisao e {:.3f}'.format(s,m,d), end =' ')
                #   ^                                                               ^
                # quebrar linha                                               nao quebrar linha

print('divisao inteira {} e potencia {}'.format(di, e))
'''

'''
n1 = int(input('digite um numero '))
sucessor = (n1 + 1)
antecessor = (n1 - 1)

print (f'o seu sucessor e {sucessor} \n e o seu antecessor e {antecessor}' )
'''
'''
n = int(input('digite um numero '))

m = n * 2
t = n * 3
r = n ** (1/2)

print ('seu dobro e {} \n seu triplo e {} \n e sua raiz quadrada e {:.3f}'.format(m,t,r))
'''
'''
m = float(input("digite um valor em metros: "))

km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000

print('{} metros tem:\n{} kilometros \n{} hectometros\n{} decametros \n{} centimetros e \n{} milimetros. \n'.format(m,km,hm,dam,dm,cm,mm))
'''
'''
n = int(input("digite um numero inteiro para ver sua tabuada: "))
print('=' * 12)

for i in range(1,11):
    print(f" {n} x {i} = {n * i}")

print('=' * 12)
'''
'''
real = float(input("quanto dinheiro voce tem? R$"))

dolar = real / 5.16
euro = real / 5.56

print('com R${:.2f} voce consegue comprar: \n U${:.2f} e \n {:.2f} euros '.format(real,dolar,euro))
'''
'''
n1 = float(input("primeira nota "))
n2 = float(input("segunda nota" ))
c = n1 + n2
d = c / 2

print(f"a soma das nota e {c} \n e a media das nota e {d}")
'''
'''
n1 = float(input("primeira nota: "))
n2 = float(input("segunda nota: "))

s = n1 + n2
m = s / 2

print('a soma das notas é {} e a media é {}'.format(s,m))
'''
'''
n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))

m = (n1 + n2) /2

print('a media entre {} e {} da {:.2f}'.format(n1,n2,m))
'''
'''
salario = float(input('qual seu salario: '))

sbonus = (0.15 * salario)
ns = sbonus + salario

print('seu salario com o aumento de 15% é: R${:.3f}'.format(ns))
'''
'''
preco = float(input('preço do produto: '))

spreco = (0.05 * preco)
np = preco - spreco
#porcentagem(alternativo)
# np = preco - (preco * 5 / 100)<<<<<<<<<<<<<

print('o preço do produto com 5% de desconto é de R${:.2f}'.format(np))
'''
'''
lar = float(input('qual a largura da parede em metros? '))
alt = float(input('e qual a altura em metros? ' ))

a = lar * alt
tinta = a / 2 

print('a quantitade de tinta necessaria para voce pintar a parede de {} m² é de {} litros'.format(a,tinta))
'''
# escreva um programa que pergunte a quantidade de km percorridos por um carro
# alugado e quantidade de dias ele foi alugado,calcule o preço a pagar sabendo 
# que o carro custa 60 R$ por dia e 0.15 por km rodados.
'''
dias = int(input('quantos dias o carro foi alugado? '))
km = float(input('quantos km rodados? '))

p = dias * 60
km = km * 0.15
s = p + km

print('o total a pagar sera de {:.2f} R$'.format(s))
'''
# importar a biblioteca inteira >>>>> # import math
# importar apenas um item da biblioteca >>>> from math import (item)
'''
import math

num = float(input('digite um numero '))
print('{} tem a parte inteira {}'.format(num,math.trunc(num)))
'''
#20
'''
import random

a = str(input('digite o nome do primeiro aluno '))
b = str(input('digite o nome do segundo aluno '))
c = str(input('digite o nome do terceiro aluno '))
d = str(input('digite o nome do quarto aluno '))

ordem = [a,b,c,d]
random.shuffle(ordem)
print('A ordem será ')
print(ordem)
'''
#19
'''
import random

a1 = str(input('primeiro aluno '))
a2 = str(input('segundo aluno '))
a3 = str(input('terceiro aluno '))
a4 = str(input('quarto aluno '))

lista = [a1,a2,a3,a4]
x = random.choice(lista)
print('O aluno(a) escolhido é {}'.format(x))
'''
#17
'''
cato = float(input('comprimento do cateto oposto '))
cata = float(input('comprimento do cateto adjacente '))
c = (cato**2) + (cata**2)
hipo = c ** (1/2)

print('a hipotenusa tem {:.2f} de comprimento '.format(hipo))
'''
'''
import math

an = float(input('digite um angulo '))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print('O angulo de {} tem\n o seno de {:.2f}\n o cosseno de {:.2f}\n e a tangente de {:.2f}'.format(an,seno,cosseno,tangente))
'''
#22
'''
nome = (input('digite seu nome completo ')).strip()
print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome contém {} caracteres ao todo.'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome contém {} caracteres.'.format(len(nome.split()[0])))
'''
#23
'''
num = int(input('digite um numero de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade:{}'.format(u))
print('Dezena:{}'.format(d))
print('Centena:{}'.format(c))
print('Milhar:{}'.format(m))
'''
#24
'''
nome = (input('digite o nome de uma cidade: ')).strip()

if nome.lower() == 'santo':
    print('Opa sua cidade começa com santo ')

else:
    print('Ei sua cidade não começa com santo ')
'''
#25
'''
nome = (input('digite seu nome: ')).strip()

if 'silva' in nome.lower(): 
    print('Seu nome tem silva. ')

else:
     print('Seu nome não tem silva. ')
'''
#26
'''
frase = (input('digite algo: ')).lower().strip()

a = frase.count('a')
p1 = frase.find('a')
p2 = frase.rfind('a')

print('a letra A aparece {} vezes. '.format(a))
print('a posição que ela aparece pela primeira vez é no {} digito. '.format(p1 + 1))
print('a posição que ela aparece pela ultima vez é no {} digito. '.format(p2 + 1))
'''
#27
'''
nome = (input('digite seu nome completo: '))

n = nome.split()

pnome = n [0]
unome = n [-1]
print('primeiro nome: {} '.format(pnome))
print('ultimo nome: {} '.format(unome))
'''
#bonus
'''
nota1 = float(input('digite uma nota sua: '))
nota2 = float(input('digite outra nota sua: '))

s = (nota1 + nota2) / 2

print('sua media foi de {}'.format(s))
      
if s >= 6:
    print('parabéns voce foi aprovado.')
else:
    print('infelismente voce foi reprovado.')
'''
#28
'''
import random
import time
a = random.randint(0,10)
e = int(input('Chuta um numero de 0 a 10: '))

print('-=-'*5)
print('PROCESSANDO... ')
print('-=-'*5)

time.sleep(1)

if e == a:
    print('AAAFF dessa vez voce ganhou :/  ')
else:
    print('ERROOOOU!! :) o numero era {} e voce chutou {} '.format(a,e))
'''
#29
'''
vel = float(input('velocidade do carro: '))

if vel >= 80:
    print('voce ultrapassou o limite de velocidade por isso ')
else:
    print('voce esta dentro do limite de velocidade permitida. ')

n1 = vel - 80
n2 = n1 * 7
print('Voce foi multado em {} reais. '.format(n2))
'''
#30
'''
num = int(input('Digite um numero inteiro: '))

if num % 2 == 0:
    print('o numero {} é par. '.format(num))
else:
    print('o numero {} é impar. '.format(num))
'''
#31
'''
dis = float(input('quantos km voce vai percorrer? '))

if  dis < 200:
    print('sua viagem ficou em R$ {} '.format(dis * 0.50))
else:
    dis > 200
    print('sua viagem ficou em R$ {} '.format(dis * 0.45))
'''
#32
'''
from calendar import isleap

ano = int(input('digite um ano qualquer: '))

if isleap(ano):
    print('O ano é bissexto ')
else:
    print('O ano não é bissexto ')
'''
#33
'''
lista = []
for i in range(3):
    lista.append(int(input(f"Digite o {i+1}º numero: ")))


max = -999999
min = 999999

for i in lista:
    if i < min: min = i
    if i > max: max = i

print(f'Maior: {max}, menor: {min}')
'''
'''
a = int(input('Digite o primeiro numero ' ))
b = int(input('Digite o segundo numero ' ))
c = int(input('Digite o terceiro numero ' ))

if a > b and a > c:
    print('{} é o maior. '.format(a))
if b > a and b > c:
    print('{} é o maior. '.format(b))
if c > a and c > b:
    print('{} é o maior. '.format(c))

if a < b and a < c:
    print('{} é o menor. '.format(a))
if b < a and b < c:
    print('{} é o menor. '.format(b))
if c < a and c < b:
    print('{} é o menor. '.format(c))
'''
#34
'''
sal = float(input('Qual seu salario? '))
if sal >= 1250:
    valor1 = (10/100 * sal) + sal
    print('seu salario novo é {} '.format(valor1))
else:
    valor2 = (15/100 * sal) + sal
    print('seu novo salario é {:.2f} '.format(valor2))
'''
#35
'''
r1 = float(input('primeiro segmento. '))
r2 = float(input('segundo segmento. '))
r3 = float(input('terceiro segmento. '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r2:
    print('Eles podem formar um triangulo. ')
else:
    print('Eles não podem formar um triangulo. ')
'''
#36

'''
casa = float(input('Qual o valor da casa? '))
sal = float(input('Qual seu salario? '))
anos = int(input('Em quantos anos voce pretende pagar? '))

mensal = anos * 12
prestacao = casa / mensal

if prestacao <= sal * 0.30:
    print('O valor mensal ficou em {:.2f} R$ em {} anos.'.format(prestacao,anos))
else:
    print('O emprestimo foi negado. ')
'''
#37
'''
num = int(input('digite um numero inteiro '))

print('escolha uma das bases de coversão:
[1] converter para binario
[2] coverter para octal
[3]coverter para hexadecimal')

opcao = int(input('sua opção: '))

if opcao == 1:
    print('{} convertido para binario é igual a {}. '.format(num,bin(num)))
elif opcao == 2:
    print('{} covertido para octal é igual a {}. '.format(num,oct(num)))
elif opcao == 3:
    print('{} convertido para hexadecimal é igual a {}. '.format(num,hex(num)))
else:
    print('Opção invalida.')
'''
#38
'''
n1 = int(input('Digite um numero inteiro. '))
n2 = int(input('Digite outro numero inteiro. '))

if n1 > n2:
    print('{} é o maior. '.format(n1))

elif n2 > n1:
    print('{} é o maior. '.format(n2))

else:
    n1 == n2 
    print('{} e {} sao iguais. '.format(n1,n2))
'''
#39
'''
from datetime import date

ano = int(input('Em qual ano voce nasceu soldado? '))

idade = date.today().year - ano

if idade < 18:
    print('Ainda não chegou seu momento soldado! faltam {} anos para o alistamento.'.format(18 - idade))

elif idade == 18:                                                                                               
    print('Ta na hora de se alistar soldado! ')

else:                                                                                                   
    idade > 18
    print('Passou da hora de se alistar soldado! passaram {} anos. '.format(idade - 18))
'''
##40
'''
n1 = float(input('primeira nota: '))
n2 = float(input('segunda nota: '))

m = (n1 + n2) /2

if m < 5.0:
    print('Sua media foi {} por isso, REPROVADO! '.format(m))

elif m >= 5.0 and m < 6.9:
    print('Sua media foi {} por isso, RECUPERAÇÃO '.format(m))

else: 
    m > 7.0
    print(' Sua media foi {} por isso, APROVADO! '.format(m))
'''
##41

'''
from datetime import date

ano = int(input('Qual ano voce nasceu? '))

i = date.today().year - ano

if i >= 0 and i < 9:
    print('MIRIM ')

elif i >= 9 and i <= 14:
    print('INFANTIL ')

elif i >= 14 and i <= 19:
    print('JUNIOR ')
elif i == 20:
    print('SENIOR ')
else:
    i > 20
    print('MASTER ')
'''
#42
'''
r1 = float(input('primeiro segmento. '))
r2 = float(input('segundo segmento. '))
r3 = float(input('terceiro segmento. '))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r2:
    print('Eles podem formar um triangulo ',end='')
    if r1 == r2 == r3:
        print('EQUILATERO.')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO.')
    else:
        print('ISOSCELES.')
else:
    print('Os segmentos acima não podem formar um triangulo.')
'''
#43

'''
peso = float(input('Qual seu peso? '))
altura = float(input('Qual sua altura em metros? '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Seu imc deu {:.2f} por isso, Abaixo do peso '.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu imc deu {:.2f} por isso, Peso ideal '.format(imc))
elif imc > 25 and imc <= 30:
    print('Seu imc deu {:.2f} por isso, Sobrepeso '.format(imc))
elif imc > 30 and imc < 40:
    print('Seu imc deu {:.2f} por isso, Obesidade '.format(imc))
else:
    imc > 40
    print('Seu imc deu {:.2f} por isso, Obesidade morbida '.format(imc))
'''

#44

'''
preco = float(input('Qual o preço do produto? '))
pagamento = int(input('escolha uma das opcoes de pagamento abaixo:\n'
                      '(1) A vista, dinheiro ou cheque 10% de desconto\n'
                      '(2) A vista no cartão 5% de desconto\n'
                      '(3) Em 2x no cartão preço normal\n'
                      '(4) Em 3x ou mais no cartão 20% de juros\n'
                      'digite uma das opçoes acima: '))

if pagamento == 1:
    print('O valor ficou em R$ {:.2f} com o desconto. '.format(preco - preco * 10/100 ))
elif pagamento == 2:
    print('O valor ficou em R$ {:.2f} com o desconto. '.format(preco - preco*0.05))
elif pagamento == 3:
    print('o valor ficou em R$ {:.2f}. '.format(preco))
if pagamento == 4:
        total = preco + (preco * 20 / 100)
        totalParc = int(input('Quantas parcelas deseja? '))
        parcela = total / totalParc

        print('Sua compra sera parcelada em {}x de R$ {:.2f} COM JUROS. '.format(totalParc,parcela))
        print('Sua compra de R$ {} vai custar R$ {} no final'.format(preco,total))
'''
#45
'''
from time import sleep
import random
print('-=-='*5)
print('VAMOS JOGAR JOKENPO!! ')
print('-=-='*5)

pc = random.choice(['pedra','papel','tesoura'])
eu = str(input('digite sua escolha aqui: ')).lower().strip()

print('-=-='*4)
print('PROCESSANDO... ')
print('-=-='*4)
sleep(1.5)

if pc == 'pedra' and eu == 'tesoura':
    print('A maquina escolheu {} e voce {} por isso, DERROTA! '.format(pc,eu))

elif pc == 'pedra'and eu == 'papel':
    print('A maquina escolheu {} e voce {} por isso, VITORIA! '.format(pc,eu))

elif pc == 'tesoura' and eu == 'pedra':
    print('A maquina escolheu {} e voce {} por isso, VITORIA! '.format(pc,eu))

elif pc == 'tesoura' and eu == 'papel':
    print('A maquina escolheu {} e voce {} por isso, DERROTA! '.format(pc,eu))

elif pc == 'papel' and eu == 'pedra':
    print('A maquina escolheu {} e voce {} por isso, DERROTA! '.format(pc,eu))

elif pc == 'papel'and eu == 'tesoura':
    print('A maquina escolheu {} e voce {} por isso, VITORIA! '.format(pc,eu))

elif pc == eu:
    print('A maquina escolheu {} e voce {} por isso, EMPATE! '.format(pc,eu))

else:
    print('Não entendi o que voce digitou tente pedra , papel ou tesoura. ')
'''
##46

'''
from time import sleep

print('='*21)
print('O ANO NOVO COMEÇA EM')
print('='*21)
for c in range(10,0,-1):
    print(c),sleep(1)
print('PAPAPAPAPAPAPAAAPAAPAAAAFIIIIIIIILLLLLLLL POOOOOOWWWW')
'''
##47
'''
for c in range(0,51):
   if c % 2 == 0:
    print(c)
'''
#48
'''
soma = 0 
cont = 0 
for c in range(1,501,2):
        
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1

print('A soma entre todos os {} valores é {}.'.format(cont,soma))
'''
#49
'''
n = int(input("digite um numero inteiro para ver sua tabuada: "))
print('=' * 12)

for i in range(1,11):
    print(f" {n} x {i} = {n * i}")

print('=' * 12)
'''
#50
'''
soma = 0
for c in range(0,6):
    n = int(input('digite um numero '))
    if n % 2 == 0:
        soma = soma + n
print('A soma dos valores pares são {}.'.format(soma))
'''
#51
'''
primeiro = int(input('digite um numero para saber a pa dele: '))
razao = int(input('digite a razao dele: '))
decimo = primeiro + (10-1) * razao

for c in range(primeiro,decimo + razao,razao):
    print(c)
'''

#52

'''
cont = 0
num = int(input('Digite um numero inteiro: '))

for c in range(1,num + 1):
    if num % c == 0:
        cont = cont + 1
print('O numero {} foi divisivel {} vezes. '.format(num,cont))
 
if cont == 2:
    print('O NUMERO {} É PRIMO!! '.format(num))
else:
    print('O NUMERO {} NÃO É PRIMO. '.format(num))
'''

#53

'''
frase = str(input('digite uma frase qualquer: ')).lower().replace(" ","")

if frase == frase[::-1]:

    print('{}, É UM PALINDROMO. '.format(frase))
else:

    print('{}, NÃO É UM PALINDROMO. '.format(frase))
'''
#54
'''
totmaior = 0
totmenor = 0

from datetime import date

for n in range(1,8):
    ano = int(input('Em qual ano a {}ª pessoa nasceu? '.format(n)))
    atual = date.today().year
    idade = atual - ano

    if idade >= 21:
        totmaior += 1
        
    else:
        idade < 21
        totmenor += 1

print('Ao todo {} são de maior e {} são de menor.'.format(totmaior,totmenor))
'''
#55
'''
m = 0
mn = 99999999999

for c in range(1,6):

    p = float(input('peso da {}ª pessoa: '.format(c)))
    if  p > m:
        m = p

    if p < mn:
        mn = p

print('O maior peso foi kg {} e o menor foi kg {}. '.format(m,mn))
'''

#56
'''
somaidade = 0
mediaidade = 0
maioridadeh = 0
nomevelho = ''
totmulher20 = 0

for p in range(1,5):
    print('------- {}ª pessoa -------'.format(p))

    n = str(input('Seu nome: ')).strip()
    i = int(input('Sua idade: '))
    s = str(input('Seu sexo M/F: ')).strip()
                  
    somaidade += i
    if p == 1 and s in 'Mm':
        nomevelho = n
    if s in 'Mm' and i > maioridadeh:
        maioridadeh = i
        nomevelho = n
    if s in 'Ff' and i < 20:
        totmulher20 += 1

mediaidade = somaidade / 4

print('A media de idade do grupo é de {} anos. '.format(mediaidade))
print('O homem mais velho tem {} anos e se chama {}'.format(maioridadeh,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos. '.format(totmulher20))
'''

#57
'''
s = str(input('Informe seu sexo, [M/F]: ')).upper()[0].strip()
while s not in 'MmFf':
    s = str(input('dados invalidos digite seu sexo corretamente: ')).upper()[0].strip()
print('sexo {} registrado.'.format(s))
'''

#58
'''
import random
import time
a = random.randint(0,10)

print('Escolhi um numero entre 0 a 10 tente adivinhar!! ')

acertou = False
tentativas = 0

while not acertou:
    e = int(input('chute um numero de 0 a 10: '))

    print('-=-'*5)
    print('PROCESSANDO... ')
    print('-=-'*5)

    time.sleep(1)

    tentativas += 1

    if e == a:
        acertou = True
    else:
        if e < a:
            print('mais... tente mais uma vez. ')
        elif e > a:
            print('menos... tente mais uma vez. ')

print('AAAFF dessa vez voce ganhou :/ depois de {} tentativas.'.format(tentativas))
'''
    
#59(minha resolução)
'''
n1 = int(input('primeiro numero: '))
n2 = int(input('segundo numero: '))
mn = int(input('escolha uma das opções abaixo:\n'
               '[1] somar\n'
               '[2] multiplicar\n'
               '[3] maior\n'
               '[4] novos numeros\n'
               '[5] sair do programa\n'))
if mn == 1:
    s = n1 + n2
    print('A soma dos dois numeros é {} '.format(s))

if mn == 2:
    m = n1 * n2
    print('A multiplicação dos numeros é {} '.format(m))

if mn == 3:
    if n1 > n2:
        print('{} é o maior'.format(n1))
    elif n2 > n1:
        print('{} é o maior '.format(n2))

if mn == 4:
    n3 = int(input('Digite seu outro primeiro numero: '))
    n4 = int(input('Digite seu outro segundo numero: '))
    mn2 = int(input('O que voce quer fazer com esses numeros?\n'
                    '[1] somar\n'
                    '[2] multiplicar\n'
                    '[3] maior\n'
                    '[5] sair do programa\n'))
    if mn2 == 1:
        s = n3 + n4
        print('A soma dos dois numeros é {} '.format(s))

    if mn2 == 2:
        m = n3 * n4
        print('A multiplicação dos numeros é {} '.format(m))

    if mn2 == 3:
        if n3 > n4:
            print('{} é o maior'.format(n3))
        elif n4 > n3:
            print('{} é o maior '.format(n4))

    if mn2 == 5:
        print('ok, programa finalizado. ')
        exit()


if mn == 5:
    print('ok, programa finalizado. ')
    exit()

else:
    print('Opção invalida tente uma das opções acima. ')
'''
#59(resolução guanabara)
'''
from time import sleep

n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
opcao = 0
while opcao != 5:
    print('[1] somar\n'
          '[2] multiplicar\n'
          '[3]maior\n'
          '[4] novos numeros\n'
          '[5] sair do programa\n')
    opcao = int(input('>>>>qual sua opção? '))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {} '.format(n1,n2,soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {} '.format(n1,n2,produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {} '.format(n1,n2,maior))
    elif opcao == 4:
        print('Informe os numeros novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('finalizando... ')
    else:
        print('Opção invalida, tente novamente.')
    print('=-=' *9)
    sleep(1)

print('fim do programa!!')
'''
#60 
'''
n = int(input('fatorial de: '))
c = n
f = 1
print('Calculando {}!\n'.format(n), end = '')
while c > 0:
    print('{} '.format(c), end = '')
    print(' x ' if c > 1 else ' = ', end = '')
    f *= c
    c -= 1
print('{}'.format(f))
'''
#61
'''
primeiro = int(input('digite um numero para saber a pa dele: '))
razao = int(input('digite a razao dele: '))
decimo = primeiro + (10-1) * razao

for c in range(primeiro,decimo + razao,razao):
    print(c)
'''
# refazendo exercicios para a pratica.
'''
from time import sleep

for c in range(10,0,-1):
    sleep(1)
    print(c)
print('POWWW PAA ')
'''
'''
for c in range(1,51):
    if c % 2 == 0:
        print(c)
'''
#jokempo completamente sozinho
'''
import random
from time import sleep

print('=-=' * 7)
print('VAMOS JOGAR JOKEMPO!!')
print('=-=' * 7)
sleep(0.5)

pc = random.choice(['pedra', 'papel', 'tesoura'])

eu = str(input('Sua escolha: ')).lower().strip().replace(' ','')


print('='*26)
print('ANALISANDO SUA RESPOSTA...')
print('='*26)

sleep(1)

if eu == 'pedra' and pc == 'papel':
    print('Não foi dessa vez jogador, Boa sorte na proxima!')
    print('Eu escolhi {} ja voce {} por isso ganhei :) '.format(pc,eu))
elif eu == 'pedra' and pc == 'tesoura':
    print('Parabéns dessa vez voce ganhou!!')
    print('Eu escolhi {} e voce {} por isso perdi :('.format(pc,eu))
elif eu == 'pedra' and pc ==  'pedra':
    print('Empatamos jogador, eu escolhi {} tambem! '.format(pc))

elif eu == 'tesoura' and pc == 'pedra':
    print('Não foi dessa vez jogador, Boa sorte na proxima!')
    print('Eu escolhi {} ja voce {} por isso ganhei :) '.format(pc,eu))
elif eu == 'tesoura' and pc == 'papel':
    print('Parabéns dessa vez voce ganhou!!')
    print('Eu escolhi {} e voce {} por isso perdi :('.format(pc,eu))
elif eu == 'tesoura' and pc ==  'tesoura':
    print('Empatamos jogador, eu escolhi {} tambem! '.format(pc))

elif eu == 'papel' and pc == 'tesoura':
    print('Não foi dessa vez jogador, Boa sorte na proxima!')
    print('Eu escolhi {} ja voce {} por isso ganhei :) '.format(pc,eu))
elif eu == 'papel' and pc == 'pedra':
    print('Parabéns dessa vez voce ganhou!!')
    print('Eu escolhi {} e voce {} por isso perdi :('.format(pc,eu))
elif eu == 'papel' and pc ==  'papel':
    print('Empatamos jogador, eu escolhi {} tambem! '.format(pc))
else:
    print('Não entendi o que voce digitou desculpa:(')
'''
'''
soma = 0

for c in range(1,7):
    n = int(input('digite o {}º numero '.format(c)))
    if n % 2 == 0:
        soma += n
print('A soma dos numeros pares é {}'.format(soma))
'''
'''
from time import sleep

n = int(input('Digite um número para saber sua tabuada: '))

print('='*14)
print('PROCESSANDO...')
print('='*14)

sleep(0.7)

print('A tabuada do {} é:'.format(n))

for c in range(0,11):

    print('{} x {} = {}'.format(n,c,n*c))
print('='*21)
print('Espero ter ajudado ;)')
print('='*21)
''' 
print('hello world')










