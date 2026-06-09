from src.alertas import avaliar_alertas
from src.engine import classificar_severidade, resposta_mission_ai

historico = []


def analisar_missao(dados):

    historico.append(dados.copy())

    if len(historico) > 5:
        historico.pop(0)

    print("\n" + "=" * 60)
    print("MISSION CONTROL AI - ENVIROSAT")
    print("=" * 60)

    print("\nSEVERIDADE:")
    print(classificar_severidade(dados))

    print("\nTELEMETRIA:")

    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

    print("\nALERTAS:")

    for alerta in avaliar_alertas(dados):
        print(alerta)

    print("\nHISTÓRICO DOS ÚLTIMOS CICLOS:")

    for i, ciclo in enumerate(historico, start=1):
        print(
            f"Ciclo {i}: "
            f"Energia={ciclo['energia']}% | "
            f"Térmico={ciclo['sensor_termico']}°C"
        )

    print("\nANÁLISE DA IA:")
    print(resposta_mission_ai(dados))
