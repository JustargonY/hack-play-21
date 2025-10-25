from src.models import EmergencySignal


def get_cell_rk_coordinates(cell_rk:int, connection):
    try:
        cursor = connection.cursor()
        query = ("SELECT cell_lat, cell_lon FROM hackplay_cells"
                 f"where cell_rk = {cell_rk};")
        cursor.execute(query)
    except Exception as error:
        print(error)


def get_users_to_send_message(signal: EmergencySignal, connection):
    cell_rk = signal.cell_rk
    try:
        cursor = connection.cursor()
        query = (f"""
                 SELECT user_id FROM user_locations_hackplay_sample where cell_rk = {cell_rk};
                 """)
        cursor.execute(query)
        results = cursor.fetchall()
        out = [x[0] for x in results]
        return out
    except Exception as error:
        print(error)
