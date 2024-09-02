from database import Database
from helper.writeAJson import writeAJson
from productAnalyzer import ProductAnalyzer

# Conectar ao banco de dados
db = Database(database="mercado", collection="compras")
# db.resetDatabase()

analyzer = ProductAnalyzer(uri="mongodb://localhost:27017/", database_name="mercado", collection_name="compras")

# 1- Total de vendas por dia
result = analyzer.totalVendasDia()  
if result:
    writeAJson(result, "Total de vendas por dia")
else:
    print("Nenhum dado retornado para o total de vendas por dia.")

# 2- Produto mais vendido
result = analyzer.produtoMaisVendido()  
if result:
    writeAJson([result], "Produto mais vendido")
else:
    print("Nenhum dado retornado para o produto mais vendido.")

# 3- Cliente que mais gastou em uma única compra
result = analyzer.clienteQueMaisGastou()  
if result:
    writeAJson([result], "Cliente que mais gastou")
else:
    print("Nenhum dado retornado para o cliente que mais gastou.")

# 4- Produtos vendidos em quantidade acima de 1 unidade
result = analyzer.produtosQueVenderamMaisDeUmaVez()  
if result:
    writeAJson(result, "Produtos que venderam mais de uma vez")
else:
    print("Nenhum dado retornado para produtos vendidos mais de uma vez.")
