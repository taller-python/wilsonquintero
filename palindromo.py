"""Confirmar si una palabra es un palindromo
Wilson Quintero """
# Palindromo
palabra=input("Escriba una palabra:  ")
input
ini=0
fin=len(palabra)-1


while ini < fin:
    if palabra[ini] == palabra[fin]:
        ini+= 1
        fin-= 1
        validacion=palabra + " es Palindromo"
    else: 
        validacion=palabra + " No es Palindromo"
        break

print(validacion)






