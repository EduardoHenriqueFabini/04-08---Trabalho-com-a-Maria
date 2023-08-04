p1 = float(input("Digite a primeira nota por favor\n"))
p2 = float(input("Digite a segunda nota por favor\n"))
p3 = float(input("Digite a terceira nota por favor\n"))
p4 = float(input("Digite a quarta nota por favor\n"))
notas = int(input("Digite a quantia de notas qu o aluno tem\n"))

M_A = (p1+p2+p3+p4)/notas

multi = p1*p2*p3*p4
M_G = multi ** (1/notas)

M_H = notas/((1/p1)+(1/p2)+(1/p3)+(1/p4))

baixa = min(M_A,M_G,M_H)
alta = max(M_A,M_G,M_H)

if M_A is alta:
    print(f"A maior média é a Média Aritimética: {alta:.2f}")
elif M_G is alta:
    print(f"A maior média é a Média Geométrica: {alta:.2f}")
elif M_H is alta:
    print(f"A maior média é a Média Harmonica: {alta:.2f}")


if M_A is baixa:
    print(f"A menor média é a Média Aritimética: {baixa:.2f}")
elif M_G is baixa:
    print(f"A menor média é a Média Geométrica: {baixa:.2f}")
elif M_H is baixa:
    print(f"A menor média é a Média Harmonica: {baixa:.2f}")