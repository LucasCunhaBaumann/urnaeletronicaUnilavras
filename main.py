from Votos import Votos


CANDIDATOS_GOV=['GAY','PRETO','MAÇOM']
CANDIDATOS_PRES=['PUTO','GAY','ESQUESITO']



def Listar():
	print("    Lista de Candidatos a Governador")
	print("\n")
	for i,candidato in enumerate (CANDIDATOS_GOV):
		print(f"Candidato(a) {i+1}: {candidato}")
	print("\n")
	print("    Lista de Candidatos a Presidente")
	print("\n")
	for i,candidato in enumerate (CANDIDATOS_PRES):
		print(f"Candidato(a) {i+1}: {candidato}")
	print("\n")



def votarG(voto,votos_gov):
	print("Candidato a governador escolhido: %s" % CANDIDATOS_GOV[voto])
	print("Confirma o voto? (S ou N) :")
	Confirmação = input()
	if Confirmação == "S":
	votos_gov[voto] += 1
	
	print("Voto confirmado")
	else:
	print("Reiniciando votação")
	voto = int(input("Digite o número do candidato a GOVERNADOR ou '0' para voto em BRANCO: "))
	votarG(voto,votos_gov)
	


def votarP(voto,votos_pres):
	print("Candidato a Presidente escolhido: %s" % CANDIDATOS_PRES[voto])
	print("Confirma o voto? (S ou N) :")
	Confirmação = input()
	if Confirmação == "S":
	votos_pres[voto] += 1
	
	print("Voto confirmado")
	else:
	print("Reiniciando votação")
	voto = int(input("Digite o número do candidato a PRESIDENTE ou '0' para voto em BRANCO: "))
	votarP(voto,votos_pres)



def votação(votos):
	voto = int(input("Digite o número do candidato a GOVERNADOR ou '0' para voto em BRANCO: "))
	votarG(voto,votos.votos_gov)
	voto = int(input("Digite o número do candidato a PRESIDENTE ou '0' para voto em BRANCO: "))
	votarP(voto,votos.votos_pres)

def apuração(votos):
	for i,candidato in enumerate (CANDIDATOS_GOV):
		print(f"Votos do(a) candidato(a) a Governador {candidato} : {votos.votos_gov[i+1]}" )
		
	for i,candidato in enumerate (CANDIDATOS_PRES):
		print(f"Votos do(a) candidato(a) a Presidente {candidato} : {votos.votos_pres[i+1]}" )
		
	



def main():
	votos_class = Votos()
	while True :  #repetição da votação
		# menu
		print("\n--------------- Urna Eletrônica 1.0 ---------------")
		print("1: Listar candidatos")
		print("2: Iniciar votação")
		print("3: Apurar votos")
		print("4: Desligar urna")
		print("\n")
		escolha = int(input("Digite sua opção: "))

		if escolha == 1:          #escolha para mostrar candidatos
			Listar()
			
		elif escolha == 2:      #escolha para fazer a votação
			votação(votos_class)

		elif escolha == 3:    #escolha para a apuração de votos
			apuração(votos_class)

		elif escolha == 4:      #escolha para desligar a urna

			print("Obrigado por Utilizar a urna eletronica")
			break

		else:   #else caso a opção escolhida seja invalida
			print("Opçao invalida")

main()





