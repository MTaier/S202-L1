from database import Database
from query import Query
from teacher_crud import TeacherCrud

db = Database("bolt://184.72.195.27:7687", "neo4j", "modes-rust-ray")
db.drop_all()  

Query.inicializar_dados(db)

teacher_crud = TeacherCrud(db)

# Questão 1
resultados_renzo = Query.buscar_professor_renzo(db)
for resultado in resultados_renzo:
    print(resultado)

resultados_professores_m = Query.buscar_professores_com_m(db)
for resultado in resultados_professores_m:
    print(resultado)

resultados_cidades = Query.buscar_todas_cidades(db)
for resultado in resultados_cidades:
    print(resultado)

resultados_escolas = Query.buscar_escolas_intervalo(db)
for resultado in resultados_escolas:
    print(resultado)

# Questão 2
resultados_idade = Query.buscar_idade_professores(db)
for resultado in resultados_idade:
    print(resultado)

resultado_media = Query.calcular_media_habitantes(db)
for resultado in resultado_media:
    print(resultado)

resultado_cidade_cep = Query.buscar_cidade_por_cep(db)
for resultado in resultado_cidade_cep:
   print(resultado)

resultado_caractere_professores = Query.buscar_caractere_professores(db)
for resultado in resultado_caractere_professores:
    print(resultado)

# Questão 3
teacher_crud.create("Chris Lima", 1956, "189.052.396-66")

resultado = teacher_crud.read("Chris Lima")
for record in resultado:
    print(record)

teacher_crud.update("Chris Lima", "162.052.777-77")

resultado = teacher_crud.read("Chris Lima")
for record in resultado:
    print(record)

db.close()