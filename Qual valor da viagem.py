n = float(input(" Qual e a distancia da sua viagem ? : " ))
print(" Voce esta prestes a começa uma viagem de {}km.".format(n))
if n <= 200:
    p = n * 0.50
else:
    p = n * 0.45
print(" Esse e o Preço que voce ira paga {:.2f} ".format(p))