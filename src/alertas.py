def avaliar_alertas(dados):

    alertas = []

    if dados["energia"] < 60:
        alertas.append(" ENERGIA BAIXA")

    if dados["energia"] < 30:
        alertas.append(" ENERGIA CRÍTICA")

    if dados["sensor_termico"] > 50:
        alertas.append(" TEMPERATURA ELEVADA")

    if dados["sensor_termico"] > 80:
        alertas.append(" TEMPERATURA CRÍTICA")

    if dados["buffer_imagens"] > 60:
        alertas.append(" BUFFER PRÓXIMO DO LIMITE")

    if dados["buffer_imagens"] > 90:
        alertas.append(" BUFFER LOTADO")

    if dados["precisao_geolocalizacao"] > 3:
        alertas.append(" IMPRECISÃO DE GEOLOCALIZAÇÃO")

    if dados["precisao_geolocalizacao"] > 7:
        alertas.append(" ERRO CRÍTICO DE GEOLOCALIZAÇÃO")

    if not alertas:
        alertas.append(" OPERAÇÃO NORMAL")

    return alertas
