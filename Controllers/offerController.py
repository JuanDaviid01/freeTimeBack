
from DataBase.connection import getConnection
from datetime import datetime

# Método para crear una nueva oferta
from datetime import datetime
from DataBase.connection import getConnection

def add_offer(offer_date, offer_inicial_price, address, task_id, 
              user_id_fulltimer, offer_start_date, offer_end_date, 
              offer_state_id, user_id_freetimer=None, offer_freetimer_calification=None, 
              offer_fulltimer_calification=None, offer_final_price=None):
    connection = getConnection()
    cursor = connection.cursor()

    # Validar y convertir las fechas al formato esperado (YYYY-MM-DD)
    try:
        offer_date = datetime.strptime(offer_date, '%Y-%m-%d').date() if offer_date else None
        offer_start_date = datetime.strptime(offer_start_date, '%Y-%m-%d').date() if offer_start_date else None
        offer_end_date = datetime.strptime(offer_end_date, '%Y-%m-%d').date() if offer_end_date else None
    except ValueError as e:
        print(f"Error en el formato de las fechas: {e}")
        return False

    query = """
        INSERT INTO offer (
            offer_date, 
            offer_inicial_price, 
            address, 
            task_id, 
            user_id_fulltimer, 
            offer_start_date, 
            offer_end_date, 
            offer_state_id, 
            user_id_freetimer, 
            offer_freetimer_calification, 
            offer_fulltimer_calification, 
            offer_final_price
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    try:
        # Ejecutar la query con los parámetros
        cursor.execute(query, (
            offer_date, 
            offer_inicial_price, 
            address, 
            task_id, 
            user_id_fulltimer, 
            offer_start_date, 
            offer_end_date, 
            offer_state_id, 
            user_id_freetimer, 
            offer_freetimer_calification, 
            offer_fulltimer_calification, 
            offer_final_price
        ))
        connection.commit()
        print(f"Oferta creada exitosamente.")
        return True
    except Exception as e:
        print(f"Error al crear la oferta: {e}")
        connection.rollback()
        return False
    finally:
        cursor.close()
        connection.close()

# Método para listar todas las ofertas
def list_offers():
    connection = getConnection()
    cursor = connection.cursor()

    query = """
        SELECT 
            offer_id, 
            offer_date, 
            offer_inicial_price, 
            address, 
            task_id, 
            user_id_fulltimer, 
            offer_start_date, 
            offer_end_date, 
            offer_state_id, 
            user_id_freetimer, 
            offer_freetimer_calification, 
            offer_fulltimer_calification, 
            offer_final_price
        FROM offer
    """

    try:
        cursor.execute(query)
        results = cursor.fetchall()
        offers = [
            {
                "offer_id": row[0],
                "offer_date": row[1].strftime('%Y-%m-%d') if row[1] else None,
                "offer_inicial_price": row[2],
                "address": row[3],
                "task_id": row[4],
                "user_id_fulltimer": row[5],
                "offer_start_date": row[6].strftime('%Y-%m-%d') if row[6] else None,
                "offer_end_date": row[7].strftime('%Y-%m-%d') if row[7] else None,
                "offer_state_id": row[8],
                "user_id_freetimer": row[9],
                "offer_freetimer_calification": row[10],
                "offer_fulltimer_calification": row[11],
                "offer_final_price": row[12]
            }
            for row in results
        ]
        return offers
    except Exception as e:
        print(f"Error al listar las ofertas: {e}")
        return None
    finally:
        cursor.close()
        connection.close()




def list_offers():
    connection = getConnection()
    cursor = connection.cursor()

    query = """
        SELECT 
            offer_id, 
            offer_date, 
            offer_inicial_price, 
            address, 
            task_id, 
            user_id_fulltimer, 
            offer_start_date, 
            offer_end_date, 
            offer_state_id, 
            user_id_freetimer, 
            offer_freetimer_calification, 
            offer_fulltimer_calification, 
            offer_final_price
        FROM offer
    """

    try:
        cursor.execute(query)
        offers = cursor.fetchall()

        offer_list = []
        for offer in offers:
            offer_list.append({
                'offer_id': offer[0],
                'offer_date': offer[1],
                'offer_inicial_price': offer[2],
                'address': offer[3],
                'task_id': offer[4],
                'user_id_fulltimer': offer[5],
                'offer_start_date': offer[6],
                'offer_end_date': offer[7],
                'offer_state_id': offer[8],
                'user_id_freetimer': offer[9],
                'offer_freetimer_calification': offer[10],
                'offer_fulltimer_calification': offer[11],
                'offer_final_price': offer[12]
            })

        return offer_list

    except Exception as e:
        print(f"Error al listar las ofertas: {e}")
        return None
    finally:
        cursor.close()
        connection.close()