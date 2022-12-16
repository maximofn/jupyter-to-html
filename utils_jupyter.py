import json

def open_notebook(filename):
    try:
        with open(filename, 'r') as f:
            notebook = json.load(f)
    except FileNotFoundError:
        print(f"El archivo {filename} no se encontró")
        return None
    except PermissionError:
        print(f"No se tienen permisos de lectura para el archivo {filename}")
        return None
    except json.JSONDecodeError:
        print(f"El archivo {filename} no tiene el formato JSON correcto")
        return None
    return notebook

def get_headers(cells):
    headers = []
    for cell in cells:
        try:
            if cell['cell_type'] == 'markdown' and cell['source'][0].startswith('#'):
                headers.append(cell['source'][0])
        except TypeError:
            print(f"El elemento {cell} de la lista cells no es un diccionario")
        except KeyError:
            print(f"El diccionario {cell} no tiene la clave 'cell_type' o 'source'")
    return headers
