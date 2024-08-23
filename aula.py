weight = float(input("Digite seu peso em kilogramas:\n"))
height = float(input("Digite sua altura em metros:\n"))
imc = weight/height**2
if imc < 18.5:
    print("Abaixo do peso")
elif imc > 29.9:
    print("Obesidade")
elif imc > 24.5:
    print("Sobrepeso")
else:
    print("Peso Normal")
