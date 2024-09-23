from database import Database
from motoristaDAO import MotoristaDAO
from motoristaCLI import MotoristaCLI

def main():
    db = Database(database="atlas-cluster", collection="usuarios")  
    motorista_dao = MotoristaDAO(db)

    motorista_cli = MotoristaCLI(motorista_dao)
    motorista_cli.menu()

if __name__ == "__main__":
    main()
