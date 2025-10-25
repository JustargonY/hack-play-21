from src.models import ExternalServicesMessage


def get_cell_rk_coordinates(cell_rk:int, connection):
    try:
        cursor = connection.cursor()
        query = ("SELECT cell_lat, cell_lon FROM hackplay_cells"
                 f"where cell_rk = {cell_rk};")
        cursor.execute(query)
    except Exception as error:
        print(error)


def get_users_to_send_message(signal: ExternalServicesMessage, connection):
    cell_rk = signal.cell_id
    try:
        cursor = connection.cursor()
        query = ("SELECT user_id FROM user_locations_hackplay_sample"
                 f"where cell_rk = {cell_rk};")
        cursor.execute(query)
    except Exception as error:
        print(error)
