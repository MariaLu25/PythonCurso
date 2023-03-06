q = 0
s = 0
m = 0 
v = float(input("Digite um valor "))

while ( v > 0.0):
    s = s + v 
    q = q + 1
    v = float (input("Digite um valor "))
    m = s /q 
    print("Soma",s)
    print("quantidade de valores digitados ",q)
    print("Media",m)