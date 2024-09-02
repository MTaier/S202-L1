from pymongo import MongoClient

class ProductAnalyzer:
    def __init__(self, uri, database_name, collection_name):
            self.client = MongoClient(uri)
            self.db = self.client[database_name]
            self.collection = self.db[collection_name]

    def totalVendasDia(self):
        pipeline = [
                {"$unwind": "$produtos"},
                {"$group": {
                    "_id": "$data_compra",
                    "total_sales": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}
                }},
                {"$sort": {"_id": 1}} 
            ]
        return list(self.collection.aggregate(pipeline))

    def produtoMaisVendido(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$produtos.descricao",
                "total_quantity": {"$sum": "$produtos.quantidade"}
            }},
            {"$sort": {"total_quantity": -1}},  
            {"$limit": 1}  
        ]
        result = list(self.collection.aggregate(pipeline))
        return result[0] if result else None

    def clienteQueMaisGastou(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": {"cliente_id": "$cliente_id", "data_compra": "$data_compra"},
                "total_amount": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}
            }},
            {"$sort": {"total_amount": -1}},  
            {"$limit": 1} 
        ]
        result = list(self.collection.aggregate(pipeline))
        return result[0] if result else None

    def produtosQueVenderamMaisDeUmaVez(self):
        pipeline = [
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$produtos.descricao",
                "total_quantity": {"$sum": "$produtos.quantidade"}
            }},
            {"$match": {"total_quantity": {"$gt": 1}}},  
            {"$project": {
                "_id": 0,
                "produto": "$_id"
            }}
        ]
        return list(self.collection.aggregate(pipeline))
