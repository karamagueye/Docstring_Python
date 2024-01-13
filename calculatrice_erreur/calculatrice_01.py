a = input("Entrer un premier nombre: ")
b = input("Entrer un deuxieme nombre: ")

if not a.isdigit() or not b.isdigit():
     print("Veuillez entrer deux nombres valides")
else:
    a =  int(a)
b =  int(b)
print(f"Le resultat de l'addition de {a} avec {b} est egal a {a + b}")

