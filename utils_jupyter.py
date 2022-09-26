import json

def open_notebook(filename):
    with open(filename, 'r') as f:
        notebook = json.load(f)
    return notebook

def get_headers(cells):
    headers = []
    for cell in cells:
        if cell['cell_type'] == 'markdown' and cell['source'][0].startswith('#'):
            headers.append(cell['source'][0])
    return headers