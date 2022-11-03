from random import choice

vocabulario = ["Acrimonia",'Capcioso','Elucubracoes','Homizio','Idiossincrasia']
palavra = choice(vocabulario)


print("J O G O   D A   F O R C A")
print()

for letra in palavra:
  print("_", end=" ")

alfabeto = ("abcdefghijklmnopqrstuvwxyz")
tentativas = []
chances = 6

while True:
  print(tentativas)
  print()
  print("Chances: ", chances)
  
  for letra in palavra:
    if letra in tentativas:
      print(letra, end=" ")
    else:
      print("_", end= " ")
      
  palpite = input("Digite um palpite. Se desejar sair apenas digite 'SAIR' \n").lower()
  if palpite == 'sair':
    break

  elif palpite not in alfabeto or palpite == '':
    print("Tá maluco?! Isso nem é uma letra\n")
    continue
  elif palpite in tentativas:
    print("Você é desmemoriado ou o quê!? Você já tentou essa letra. Tente outra! :)\n")
    continue

  tentativas.append(palpite)
  if palpite in palavra:
    print("ACERTOU MIZERAVI!\n")
  else:
    print("ERRESTES ERRONIAMENTE\n")
    chances -=1
  if chances == 0:
    print("Perdeu menó. GAME OVER FOR YOU BASTARD")
    break
  elif set(palavra).issubset(set(tentativas)):
    print("Parabéns, você acertou! Weeee are the champions, my frieeeend!")
    break
    


  
  
  
  