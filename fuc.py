def lernotas():
    n = float(input("Digite uma nota para o aluno: "))
    return n
def resultado (n,n1):
    m = n+n1/2
    print("nota 1" ,n)
    print("nota 2" ,n1)
    print("media: ",m, "resultado",end="")
    if m >= 7:
        print("Aprovado")
    else:
        print("Reprovado")

        a = lernotas()
        b = lernotas()
        resultado(a, b)