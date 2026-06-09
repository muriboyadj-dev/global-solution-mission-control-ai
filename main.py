from banner_ascii import exibir_banner
from src.telemetria import coletar_telemetria
from src.ui import analisar_missao


def main():

    exibir_banner()

    while True:

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
