from src.telemetria import coletar_telemetria
from src.ui import analisar_missao


def main():

    while True:

        print("\n" + "=" * 60)
        print("MISSION CONTROL AI - ENVIROSAT")
        print("=" * 60)

        print("\n1 - Inserir telemetria")
        print("2 - Encerrar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":

            dados = coletar_telemetria()
            analisar_missao(dados)

        elif opcao == "2":

            print("\nMission Control AI encerrado.")
            break

        else:

            print("\nOpção inválida.")


if __name__ == "__main__":
    main()
