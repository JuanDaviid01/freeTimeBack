from DataBase.connection import getConnection
from Models.taskModel import Task

def list_task():
    connection = getConnection()
    cursor = connection.cursor()

    query = """
        SELECT task_id, task_title, task_stimed_time_hours, task_offer_suggested FROM task;

    """

    try:
        # Ejecutar la query
        cursor.execute(query)
        # Obtener todos los resultados
        tasks = cursor.fetchall()
        
        # Formatear los resultados en una lista de diccionarios
        task_list = []
        for task in tasks:
            task_list.append({
                'task_id': task[0],                     # Incluye el task_id como el primer campo
                'task_title': task[1],                  # Ajusta los índices según el orden en la query
                'task_stimed_time_hours': task[2],
                'task_offer_suggested': task[3]
            })

        return task_list
    except Exception as e: 
        print(f"Error al listar las tareas {e}")
        return None
    finally: 
        cursor.close()
        connection.close()