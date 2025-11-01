import random

numero_secreto = random.randint(1, 10)
tentativas = 6

while tentativas > 0:
  tentativas -= 1
  print(f"tentativas {tentativas}")
  if tentativas == 0:
      print("que pena você não tem mais tentativas")
      print(f"O número secreto era {numero_secreto}")
  else:
      usuario = int(input("Digite um número de 1 a 10: "))
      if usuario == numero_secreto:
          print(f"Parabéns você acertou o número secreto {numero_secreto}")
          tentativas = 0
      else:
          if usuario < numero_secreto:
              print("Errou")
              print("O número secreto é maior")
          else:
              print("Errou")
              print("O número secreto é menor")
     
