from math import hypot, radians, sin, tan, cos 
co=float(input("Comprimento do cateto oposto: "))
ca=float(input("Comprimento do cateto adjacente: "))
hi=hypot(co, ca)
print(f"A hipotenusa vai medir {hi:.2f}")

ang=float(input("Digite o ângulo: "))
seno=sin(radians(ang))
coss=cos(radians(ang))
tg=tan(radians(ang))
print(f"Seno de {ang} é {seno:.2f}")
print(f"O cosseno de {ang} é {coss:.2f}")
print(f"A tangente de {ang} é {tg:.2f}")
