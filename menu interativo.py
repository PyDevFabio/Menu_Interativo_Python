

def dois_soma(n1=0, n2=0):
	n1 = int(input('1 Número:'))
	n2 = int(input('2 Número: ')) 
	soma = n1 + n2
	print(soma)
	

def dois_subtração(n1=0, n2=0):
	n1 = int(input('1 Número:'))
	n2 = int(input('2 Número: ')) 
	sub = n1 - n2 
	print(sub)


def dois_dividir(n1=0, n2=0):
	n1 = int(input('1 Número:'))
	n2 = int(input('2 Número: ')) 
	div = n1 / n2 
	print(div)


def dois_multiplicar(n1=0, n2=0):
	n1 = int(input('1 Número:'))
	n2 = int(input('2 Número: ')) 
	mult = n1 * n2 
	print(mult)
	

def main():
	while True:
		print('-' * 20)
		print('Menu Interativo')
		print('-' * 20)
		print()
		print('Opções: ')
		print('[1] - Somar')
		print('[2] - Subtrair')
		print('[3] - Dividir')
		print('[4] - Multiplicar')
		print('[5] - Encerrar Programa')
		
		resp = int(input('Sua Opção:')) 
		if resp == 1:
			dois_soma()
		elif resp == 2:
			dois_subtração()
		elif resp == 3:
			dois_dividir()
		elif resp == 4:
			dois_multiplicar()
		elif resp == 5:
			break 
		else:
			print('Opção Inválida')
			main()
			
#Função Principal
main()

	
