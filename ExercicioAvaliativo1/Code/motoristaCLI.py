from motoristaDAO import MotoristaDAO
from motorista import Motorista
from corrida import Corrida
from passageiro import Passageiro

class MotoristaCLI:
    def __init__(self, motorista_dao: MotoristaDAO):
        self.motorista_dao = motorista_dao

    def menu(self):
        while True:
            print("\nMenu de Gerenciamento de Motoristas")
            print("1. Criar Motorista")
            print("2. Ler Motorista")
            print("3. Atualizar Motorista")
            print("4. Deletar Motorista")
            print("5. Sair")
            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                self.create_motorista()
            elif opcao == '2':
                self.read_motorista()
            elif opcao == '3':
                self.update_motorista()
            elif opcao == '4':
                self.delete_motorista()
            elif opcao == '5':
                print("Saindo...")
                break
            else:
                print("Opção inválida! Tente novamente.")

    def create_motorista(self):
        nota_motorista = int(input("Nota do Motorista: "))
        corridas = []

        while True:
            nome_passageiro = input("Nome do Passageiro: ")
            documento_passageiro = input("Documento do Passageiro: ")
            passageiro = Passageiro(nome=nome_passageiro, documento=documento_passageiro)

            nota_corrida = int(input("Nota da Corrida: "))
            distancia_corrida = float(input("Distância da Corrida (em km): "))
            valor_corrida = float(input("Valor da Corrida (em R$): "))
            corrida = Corrida(nota=nota_corrida, distancia=distancia_corrida, valor=valor_corrida, passageiro=passageiro)
            corridas.append(corrida)

            mais_corridas = input("Deseja adicionar outra corrida? (s/n): ")
            if mais_corridas.lower() != 's':
                break

        motorista = Motorista(nota=nota_motorista, corridas=corridas)

        self.motorista_dao.create(motorista)
        print("Motorista criado com sucesso!")

    def read_motorista(self):
        motorista_id = input("Digite o ID do motorista: ")
        motorista = self.motorista_dao.read(motorista_id)
        if motorista:
            print(f"\nMotorista encontrado:")
            print(f"ID: {motorista['_id']}")
            print(f"Nota: {motorista['nota']}")
            print("Corridas:")
            for i, corrida in enumerate(motorista['corridas'], start=1):
                print(f"  Corrida {i}:")
                print(f"    Nota: {corrida['nota']}")
                print(f"    Distância: {corrida['distancia']} km")
                print(f"    Valor: R$ {corrida['valor']}")
                print(f"    Passageiro: {corrida['passageiro']['nome']} - Documento: {corrida['passageiro']['documento']}")
        else:
            print("Motorista não encontrado.")

    def update_motorista(self):
        motorista_id = input("Digite o ID do motorista a ser atualizado: ")
        campo = input("Qual campo deseja atualizar? (nota): ")
        valor = input(f"Novo valor para {campo}: ")

        try:
            if campo == 'nota':
                valor = int(valor)
            self.motorista_dao.update(motorista_id, {campo: valor})
            print("Motorista atualizado com sucesso!")
        except ValueError:
            print("Valor inválido para o campo nota.")

    def delete_motorista(self):
        motorista_id = input("Digite o ID do motorista a ser deletado: ")
        self.motorista_dao.delete(motorista_id)
        print("Motorista deletado com sucesso!")
