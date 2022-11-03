chutes = ["c","a","m","i","n","h","o"]
palavra = "caminho"

# função que escreve palavra
def escrever_palavra(chutes,palavra):
  for letra in palavra:
    if letra in chutes:
      print(letra, end=" ")
    else:
      print("_",end=" ")

escrever_palavra(chutes,palavra)


#função que desenha o boneco
def desenhar_boneco(n):
  linhas = [
      "o"
     "/|\\\"
     "/ \\\"
  ]
  if n > 0:
    linhas[0] = "0"

  if n > 1:
    linhas[1] = '|'
    
  if n == 2:
    linhas[2] = '/'

  if n >= 3:
    linhas[3] = '\'

  if n
    
  forca = """
    
    |_______
    |      |
    |     { }
    |     { }
    |     { }
    |
  -----------
  //////////////
  \\\\\\\\\\\\\\
  """.format(linhas[0],linhas[1],linhas[1],linhas[2],linhas[3])
  print(forca)
  
