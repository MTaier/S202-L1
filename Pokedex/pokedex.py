from helper import writeAJson
from database import Database

class Pokedex:
    def __init__(self, database: Database):
        self.database = database

    def getPokemonByName(self, name: str):
        result = list(self.database.collection.find({"name": name}))
        writeAJson(result, name) 
        return result

    def getPokemonsByType(self, types: list):
        result = list(self.database.collection.find({"type": {"$in": types}}))
        writeAJson(result, f"query_types")
        return result
    
    def getPokemonsWeakAgainst(self, types: list):
        result = list(self.database.collection.find({"weaknesses": {"$all": types}}))
        writeAJson(result, f"query_weak_against")
        return result
    
    def getPokemonsBySpawnChance(self, min_chance: float, max_chance: float):
        query = {"spawn_chance": {"$gt": min_chance, "$lt": max_chance}}
        result = list(self.database.collection.find(query))
        writeAJson(result, f"spawn_chance_{min_chance}_to_{max_chance}")
        return result
    
    def getPokemonsWithoutMultipliers(self):
        query = {"multipliers": None}
        result = list(self.database.collection.find(query))
        writeAJson(result, "pokemons_without_multipliers")
        return result