codigo = int (input("Qual o código do produto?: "))
nome =  (input("Digite o nome do produto: "))
quantidade = int (input("Qual a quantidade comprada?: "))
preco = float (input("Informe o preço: "))
valor = quantidade*preco


print ("O valor de ", quantidade , nome , "é de:", valor , "reais.")
print ("Código do produto: ", codigo)
print ("Valor unitário: ", preco)