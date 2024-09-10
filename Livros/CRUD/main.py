from database import Database
from helper.writeAJson import writeAJson
from livrosModel import LivroModel

db = Database(database="Livros", collection="Livros")

livro_model = LivroModel(db)

novo_id = livro_model.create_livro("Clean Code", "Robert C. Martin", 2008, 31.0)
livro_model.read_livro_by_id(str(novo_id))
livro_model.update_livro(str(novo_id), "Clean Code", "Robert C. Martin", 2008, 35.0)
livro_model.delete_livro(str(novo_id))