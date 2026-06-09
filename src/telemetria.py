def coletar_telemetria():

    energia = float(input("Energia (%): "))
    temperatura = float(input("Sensor térmico (°C): "))
    buffer = float(input("Buffer de imagens (%): "))
    gps = float(input("Precisão de geolocalização (m): "))

    return {
        "energia": energia,
        "sensor_termico": temperatura,
        "buffer_imagens": buffer,
        "precisao_geolocalizacao": gps
    }
