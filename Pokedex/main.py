from database import Database
from pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")
#db.resetDatabase()

pokedex = Pokedex(db)
pokedex.getPokemonByName("Pikachu")
pokedex.getPokemonsByType(['Fire', 'Flying'])
pokedex.getPokemonsWeakAgainst(['Psychic', 'Ice'])
pokedex.getPokemonsBySpawnChance(0.3, 0.6)
pokedex.getPokemonsWithoutMultipliers()