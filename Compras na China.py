celular = 299.99
gnomo = 66.66
chaleira = 23.87
unicornio = 1.42*6
dolar = 3.25
frete = 12.34
valor_compra_dolar = celular+gnomo+frete+chaleira+unicornio
valor_compra_real = valor_compra_dolar * 3.25
IOF_real = (6.38*valor_compra_real)/100
IOF_dolar = (6.38*valor_compra_dolar)/100

print("O valor de IOF em real é de: ", IOF_real)
print("O valor de IOF em dolar é de: ", IOF_dolar)
print("O valor da compra em dolar é de: ", valor_compra_dolar)
print("O valor da compra em real é de: ", valor_compra_real)