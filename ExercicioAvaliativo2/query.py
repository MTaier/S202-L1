class Query:
    def buscar_professor_renzo(database):
        query = """
            MATCH (t:Teacher {name: 'Renzo'})
            RETURN t.ano_nasc AS ano_nasc, t.cpf AS cpf
        """
        return database.execute_query(query)

    def buscar_professores_com_m(database):
        query = """
            MATCH (t:Teacher)
            WHERE t.name STARTS WITH 'M'
            RETURN t.name AS name, t.cpf AS cpf
        """
        return database.execute_query(query)

    def buscar_todas_cidades(database):
        query = """
            MATCH (c:City)
            RETURN c.name AS name
        """
        return database.execute_query(query)

    def buscar_escolas_intervalo(database):
        query = """
            MATCH (s:School)
            WHERE s.number >= 150 AND s.number <= 550
            RETURN s.name AS nome, s.address AS endereco, s.number AS numero
        """
        return database.execute_query(query)

    def buscar_idade_professores(database):
        query = """
            MATCH (t:Teacher)
            RETURN max(t.ano_nasc) AS ano_mais_jovem, min(t.ano_nasc) AS ano_mais_velho
        """
        return database.execute_query(query)

    def calcular_media_habitantes(database):
        query = """
            MATCH (c:City)
            RETURN avg(c.population) AS media_population
        """
        return database.execute_query(query)

    def buscar_cidade_por_cep(database):
        query = """
            MATCH (c:City {cep: '37540-000'})
            RETURN replace(c.name, 'a', 'A') AS nome_modificado
        """
        return database.execute_query(query)

    def buscar_caractere_professores(database):
        query = """
            MATCH (t:Teacher)
            RETURN substring(t.name, 2, 1) AS terceiro_caractere
        """
        return database.execute_query(query)

    def inicializar_dados(database):
        queries = [
            "CREATE(:Teacher{name:'Aline',ano_nasc:1998,cpf:'123.456.789-10'})",
            "CREATE(:Teacher{name:'Marisa',ano_nasc:1950,cpf:'012.345.678-91'})",
            "CREATE(:Teacher{name:'Elza',ano_nasc:1987,cpf:'901.234.567-89'})",
            "CREATE(:Teacher{name:'Marcelo',ano_nasc:1978,cpf:'890.123.456-78'})",
            "CREATE(:Teacher{name:'Renzo',ano_nasc:1956,cpf:'789.012.345-67'})",
            "CREATE(:Teacher{name:'Justino',ano_nasc:1995,cpf:'678.901.234-56'})",
            
            "CREATE(:School{name:'Sanico Teles',address:'R. Olavo Marques',number:181})",
            "CREATE(:School{name:'Sinha Moreira',address:'Av. Dr. Delfim Moreira',number:509})",
            "CREATE(:School{name:'Zenaide',address:'Conj. Hab. Gilberto Rossetti',number:332})",
            "CREATE(:School{name:'Luis Machado Filho',address:'R. Luis Machado',number:100})",
            
            "CREATE(:City{name:'Santa Rita do Sapucai', cep:'37540-000', population:43753})",
            "CREATE(:City{name:'Serra da Saudade', cep:'35617-000', population:776})",
            "CREATE(:City{name:'Cidadezinha', cep:'13737-635', population:68980})",
            "CREATE(:State{name:'Minas Gerais', country:'Brasil'})",

            "MATCH(t:Teacher{name:'Renzo'}),(s:School{name:'Luis Machado Filho'}) CREATE(t)-[:WORKS]->(s)",
            "MATCH(t:Teacher{name:'Justino'}),(s:School{name:'Zenaide'}) CREATE(t)-[:WORKS]->(s)",
            "MATCH(t:Teacher{name:'Aline'}),(s:School{name:'Sinha Moreira'}) CREATE(t)-[:WORKS]->(s)",
            "MATCH(t:Teacher{name:'Marcelo'}),(s:School{name:'Sanico Teles'}) CREATE(t)-[:WORKS]->(s)",
            "MATCH(t:Teacher{name:'Elza'}),(s:School{name:'Sinha Moreira'}) CREATE(t)-[:WORKS]->(s)",
            "MATCH(t:Teacher{name:'Marisa'}),(s:School{name:'Sanico Teles'}) CREATE(t)-[:WORKS]->(s)",
            
            "MATCH(s:School{name:'Sinha Moreira'}),(c:City{name:'Santa Rita do Sapucai'}) CREATE(s)-[:LOCATES]->(c)",
            "MATCH(s:School{name:'Sanico Teles'}),(c:City{name:'Santa Rita do Sapucai'}) CREATE(s)-[:LOCATES]->(c)",
            "MATCH(s:School{name:'Luis Machado Filho'}),(c:City{name:'Serra da Saudade'}) CREATE(s)-[:LOCATES]->(c)",
            "MATCH(s:School{name:'Zenaide'}),(c:City{name:'Cidadezinha'}) CREATE(s)-[:LOCATES]->(c)",
            
            "MATCH(c:City{name:'Santa Rita do Sapucai'}),(st:State{name:'Minas Gerais'}) CREATE(c)-[:BELONGS]->(st)",
            "MATCH(c:City{name:'Serra da Saudade'}),(st:State{name:'Minas Gerais'}) CREATE(c)-[:BELONGS]->(st)",
            "MATCH(c:City{name:'Cidadezinha'}),(st:State{name:'Minas Gerais'}) CREATE(c)-[:BELONGS]->(st)"
        ]
        
        for query in queries:
            database.execute_query(query)