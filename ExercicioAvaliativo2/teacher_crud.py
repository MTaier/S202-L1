class TeacherCrud:
    def __init__(self, database):
        self.database = database

    def create(self, name, ano_nasc, cpf):
        query = """
        CREATE (:Teacher {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})
        """
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.database.execute_query(query, parameters)
        print(f"Teacher '{name}' criado com sucesso.")

    def read(self, name):
        query = """
        MATCH (t:Teacher {name: $name})
        RETURN t.name AS name, t.ano_nasc AS ano_nasc, t.cpf AS cpf
        """
        parameters = {"name": name}
        result = self.database.execute_query(query, parameters)
        if result:
            return result
        else:
            print(f"Teacher '{name}' não encontrado.")
            return None

    def update(self, name, newCpf):
        query = """
        MATCH (t:Teacher {name: $name})
        SET t.cpf = $newCpf
        RETURN t.name AS name, t.cpf AS cpf
        """
        parameters = {"name": name, "newCpf": newCpf}
        result = self.database.execute_query(query, parameters)
        if result:
            print(f"CPF do Teacher '{name}' atualizado para {newCpf}.")
        else:
            print(f"Teacher '{name}' não encontrado para atualização.")

    def delete(self, name):
        query = """
        MATCH (t:Teacher {name: $name})
        DELETE t
        RETURN t.name AS name
        """
        parameters = {"name": name}
        result = self.database.execute_query(query, parameters)
        if result:
            print(f"Teacher '{name}' excluído com sucesso.")
        else:
            print(f"Teacher '{name}' não encontrado para exclusão.")