from typing import List
from database import Database
from motorista import Motorista
from bson.objectid import ObjectId

class MotoristaDAO:
    def __init__(self, db: Database):
        self.db = db

    def create(self, motorista: Motorista):
        try:
            motorista_data = {
                "nota": motorista.nota,
                "corridas": [
                    {
                        "nota": corrida.nota,
                        "distancia": corrida.distancia,
                        "valor": corrida.valor,
                        "passageiro": {
                            "nome": corrida.passageiro.nome,
                            "documento": corrida.passageiro.documento
                        }
                    }
                    for corrida in motorista.corridas
                ]
            }
            self.db.collection.insert_one(motorista_data)
            print("Motorista criado com sucesso!")
        except Exception as e:
            print(f"Erro ao criar o motorista: {e}")

    def read(self, motorista_id: str):
        try:
            motorista = self.db.collection.find_one({"_id": ObjectId(motorista_id)})
            if motorista:
                return motorista
            else:
                print("Motorista não encontrado.")
                return None
        except Exception as e:
            print(f"Erro ao buscar o motorista: {e}")
            return None

    def update(self, motorista_id: str, update_data: dict):
        try:
            result = self.db.collection.update_one(
                {"_id": ObjectId(motorista_id)},
                {"$set": update_data}
            )
            if result.matched_count > 0:
                print("Motorista atualizado com sucesso!")
            else:
                print("Motorista não encontrado.")
        except Exception as e:
            print(f"Erro ao atualizar o motorista: {e}")

    def delete(self, motorista_id: str):
        try:
            result = self.db.collection.delete_one({"_id": ObjectId(motorista_id)})
            if result.deleted_count > 0:
                print("Motorista deletado com sucesso!")
            else:
                print("Motorista não encontrado.")
        except Exception as e:
            print(f"Erro ao deletar o motorista: {e}")
