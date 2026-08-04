from datetime import datetime


def parse_stt(trama: str) -> dict:
    """
    Convierte una trama STT en un diccionario con datos organizados.
    """

    trama = trama.strip()

    if not trama:
        raise ValueError("La trama está vacía")

    campos = trama.split(";")

    if len(campos) < 18:
        raise ValueError(
            f"La trama tiene {len(campos)} campos; se esperaban al menos 18"
        )

    if campos[0] != "STT":
        raise ValueError(f"Tipo de trama no soportado: {campos[0]}")

    try:
        hora = campos[7]

        if ":" in hora:
            gps_time = datetime.strptime(
                f"{campos[6]} {hora}",
                "%Y%m%d %H:%M:%S",
            )
        else:
            gps_time = datetime.strptime(
                campos[6] + hora,
                "%Y%m%d%H%M%S",
            )

        datos = {
            "tipo": campos[0],
            "imei": campos[1],
            "gps_time": gps_time,
            "latitud": float(campos[13]),
            "longitud": float(campos[14]),
            "velocidad": float(campos[15]),
            "satelites": int(campos[17]),
        }

    except ValueError as error:
        raise ValueError(
            f"La trama contiene un dato inválido: {error}"
        ) from error

    return datos