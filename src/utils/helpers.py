def get_cell_rk_coordinates(cell_rk:int, connection):
    try:
        cursor = connection.cursor()
        query = ("SELECT cell_lat, cell_lon FROM hackplay_cells"
                 f"where cell_rk = {cell_rk};")
        cursor.execute(query)
    except Exception as error:
        print(error)
