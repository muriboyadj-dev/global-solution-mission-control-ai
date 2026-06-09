from src.alertas import avaliar_alertas


def classificar_severidade(dados):

    pontos = 0

    if dados["energia"] < 60:
        pontos += 1

    if dados["energia"] < 30:
        pontos += 2

    if dados["sensor_termico"] > 50:
        pontos += 1

    if dados["sensor_termico"] > 80:
        pontos += 2

    if dados["buffer_imagens"] > 60:
        pontos += 1

    if dados["buffer_imagens"] > 90:
        pontos += 2

    if dados["precisao_geolocalizacao"] > 3:
        pontos += 1

    if dados["precisao_geolocalizacao"] > 7:
        pontos += 2

    if pontos == 0:
        return "NORMAL"

    elif pontos <= 4:
        return "MODERADO"

    return "CRÍTICO"


def resposta_mission_ai(dados):

    severidade = classificar_severidade(dados)

    if severidade == "NORMAL":
        return """
DIAGNÓSTICO:
Todos os sistemas operam dentro dos parâmetros esperados.

IMPACTO TERRESTRE:
Monitoramento ambiental funcionando normalmente.

AÇÃO RECOMENDADA:
Manter operação nominal.

RESUMO EXECUTIVO:
Missão estável.
"""

    elif severidade == "MODERADO":
        return """
DIAGNÓSTICO:
Foram detectadas degradações operacionais.

IMPACTO TERRESTRE:
Possível atraso na identificação de queimadas e eventos ambientais.

AÇÃO RECOMENDADA:
Monitorar sistemas afetados.

RESUMO EXECUTIVO:
Missão funcional com riscos moderados.
"""

    return """
DIAGNÓSTICO:
Foram detectadas anomalias críticas.

IMPACTO TERRESTRE:
Risco de perda parcial do monitoramento ambiental.

AÇÃO RECOMENDADA:
Ativar protocolos de contingência.

RESUMO EXECUTIVO:
Missão em estado crítico.
"""
