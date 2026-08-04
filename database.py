import psycopg


DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "gps_platform",
    "user": "postgres",
    "password": "l123",
}


def get_connection():
    """
    Crea y devuelve una conexión con PostgreSQL.
    """
    return psycopg.connect(**DB_CONFIG)


def guardar_posicion(datos: dict, trama: str) -> None:
    """
    Guarda una posición GPS en la tabla positions.
    """

    consulta = """
        INSERT INTO positions (
            imei,
            gps_time,
            latitude,
            longitude,
            speed,
            satellites,
            raw_message
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """

    valores = (
        datos["imei"],
        datos["gps_time"],
        datos["latitud"],
        datos["longitud"],
        datos["velocidad"],
        datos["satelites"],
        trama,
    )

    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(consulta, valores)