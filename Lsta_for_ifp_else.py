compras = []
resp= 's'
while resp == "s":
  compras.append(input("Digite o item da lista"))
  resp = input('Deseja continuar - s para sim ou  n para não')
#e
for x in compras:
  if x == "banana":
    print("Encontrei a Banana!!!")
  else:
    print('Não encontrei a Banana!!!')
  #print(x)
#print(compras)
