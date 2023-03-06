n = float(input("Digite a primeira nota -> "))
n2 = float(input("Digite a segunda  nota ->  "))
m = (n+n2)/2

if m >= 7 :
    print("Aprovado media = %.1f" %m)
elif m > 3 and m < 5 :
    print("Prova Final media = %.1f" %m)
else:
    print("REPROVADO")

