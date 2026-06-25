# Testando várias condições:
idade1 = 22
idade2 = 18

# and
if idade1 >= 21 and idade2 <= 18:
    # Retornará True
    print(idade1 >= 21 and idade2 <= 18)


if idade1 >= 21 and idade2 <= 17:
    # Retornará False mas não executa
    print(idade1 >= 21 and idade2 <= 17)


# or
if idade1 >= 21 or idade2 <= 17:
    # Retornará False mas não executa
    print(idade1 >= 21 or idade2 <= 17)

