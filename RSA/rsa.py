'''
Escreva um programa que implemente o algoritmo RSA e que seja capaz de cifrar e decifrar um texto de mensagem que aceite todos os caracteres da tabela ASCII estendida (de 0 a 255). 
O programa ter� como entradas os valores dos primos p e q, e o valor da chave p�blica e.
O programa dever� calcular o valor de n = p x q, e o valor de phi(n). Em seguida o programa dever� checar a validade da chave p�blica provida e (ela deve ser prima relativamente ao valor de phi(n), isto � mdc(e, phi(n)) = 1). 
Caso a chave p�blica e n�o seja v�lida, o programa deve imprimir uma mensagem de erro e solicitar outra chave p�blica, e continuar fazendo assim at� que uma chave p�blica v�lida seja fornecida. 
Quando a chave p�blica e provida for v�lida, o programa deve calcular a chave privada d. Em seguida o programa dever� solicitar ao usu�rio se a a��o desejada � cifra��o ou decifra��o. 
Finalmente o programa ir� solicitar ao usu�rio o path do arquivo onde se encontra o texto a ser cifrado ou decifrado e prosseguir com a cifra��o (usando o valor de e) ou a decifra��o (usando o valor de d) do texto. 
O texto resultante da cifra��o ou decifra��o dever� ser armazenado em um outro arquivo.
'''
import sys

INVALIDO = '-1'
CIFRACAO = '0'
DECIFRACAO = '1'

def phi(primo1,primo2):
	return (primo1-1)*(primo2-1)

def mdc(val1, val2):
	dividendo = val1
	divisor = val2
	while(divisor != 0):
		resto = dividendo % divisor;
		dividendo = divisor;
		divisor = resto;
	return dividendo;

def euclidesExtendido(divisor, dividendo, sinal):
    r = dividendo % divisor
    if (r == 1):
		if(sinal<0):
			return (sinal+dividendo)/ divisor
		else:
			return (sinal / divisor) % (dividendo / divisor)
    return ((euclidesExtendido(r, divisor, -sinal) * dividendo + sinal) / (divisor%dividendo))


p = int(raw_input("digite p: "))
q = int(raw_input("digite q: "))
chave_publica = int(raw_input("digite a chave publica: "))

n = p*q
phi_n = phi(p,q)

while( mdc(chave_publica, phi_n) != 1):
	chave_publica = int(raw_input("chave publica invalida! digite outra: "))

chave_privada = euclidesExtendido(chave_publica,phi_n,1)

tipo_operacao = INVALIDO
while( tipo_operacao != CIFRACAO and tipo_operacao != DECIFRACAO):
	tipo_operacao = raw_input("digite "+CIFRACAO+" para cifrar ou "+DECIFRACAO+" para decifrar: ")

caminho_arq_original = raw_input("digite o caminho do arquivo a ser lido: ")
arquivo = open(caminho_arq_original, 'r')
texto_original = arquivo.read()

texto_alterado = ""
if(tipo_operacao == CIFRACAO):
	for letra in texto_original:
		texto_alterado +=  str((ord(letra)**chave_publica) % n)+" "
else:
	for letra in texto_original.split():
		texto_alterado +=  chr((int(letra)**chave_privada) % n)
arquivo.close()

caminho_arq_final = raw_input("digite o caminho do arquivo a ser escrito: ")
arquivo = open(caminho_arq_final, 'w')
arquivo.write(texto_alterado)
arquivo.close()
