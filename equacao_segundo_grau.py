# Programa para resolver uma equação do segundo grau 
A = int(input("Digite o valor de A: ")) # valor de A
B = int(input("Digite o valor de B: ")) # valor de B
C = int(input("Digite o valor de C: ")) # valor de C

if A == 0:  # se A for igual a 0, então não é uma equação do segundo grau 
    print("Não é uma equação do segundo grau!.")
    
else:  #  se não a equação é do segundo grau 
    delta = B**2 - 4 * A * C  # cálculo do delta 

    if delta < 0:  # se delta for menor que 0, não existem raízes reais 
        print("Não existem raízes reais.")

    else:  # se delta for maior que 0, existem duas raízes reais 
        x1 = (-B + delta**0.5) / (2 * A)  
        x2 = (-B - delta**0.5) / (2 * A)  
        print(f"As duas raízes reais são: {x1} e {x2}")
