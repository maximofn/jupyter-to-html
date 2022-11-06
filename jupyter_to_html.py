#!/usr/bin/env python3

import argparse
import re
import sys
import os
import utils_jupyter as uj
import uilts_html as uh
import format_text as ft


def path_name_ext_from_file(file):
    path, name = os.path.split(file)
    name, extension = os.path.splitext(name)
    simplex_name = name[11:].replace("-", " ")
    return path, name, extension, simplex_name


def parse_arguments():
    parser = argparse.ArgumentParser(description='Jupyter notebook to HTML Help')
    parser.add_argument('-f', '--file', help='The notebook to convert', required=True)
    
    args = parser.parse_args()
    if args.file:
        path, name, extension, _ = path_name_ext_from_file(args.file)
        if extension == '.ipynb':
            print(f"Convert {name}{extension} to {name}.html")
        else:
            print(f"File {args.file} is not a Jupyter notebook")
            sys.exit(1)
    else:
        print('No file specified')
        sys.exit(1)
    
    return parser.parse_args()



def main():
    args = parse_arguments()
    
    # Open notebook and get cells and headers
    notebook = uj.open_notebook(args.file)  # Open the notebook as a dictionary
    cells = notebook['cells']   # Get only with the cells
    headers = uj.get_headers(cells) # Get the headers

    # Get name and simple name of the notebook
    _, name, _, simplex_name = path_name_ext_from_file(args.file)

    # Create the HTML file
    # html = uh.open_html(f"{path}/{name}.html")
    html = uh.open_html(f"_{name}.html")

    # Add the first part of the HTML file
    uh.first_paragraph(html)    # Write the first paragraph
    
    # Add the first two divs
    indentation = 0
    uh.open_div_notebook(indentation, html)
    indentation += 1
    uh.open_div_notebook_container(indentation, html)
    
    # Add the index head
    indentation += 1
    indentation = uh.print_index_head(indentation, simplex_name, html)
    uh.print_blank_line(html)

    # Add the index body
    indentation = uh.print_index_body(indentation, headers, html)
    uh.print_blank_line(html)

    # Add the content of the notebook
    indentation = uh.print_content(indentation, cells, html)
    uh.print_blank_line(html)
    
    # Close the two first divs
    indentation -= 1
    uh.close_div_notebook_container(indentation, html)
    indentation -= 1
    uh.close_div_notebook(indentation, html)
    uh.close_html(html)  # Close the HTML file

    # Post format the HTML file
    ft.post_format_html(f"_{name}.html")

    # Change separates unordered lists to ordered lists
    ft.merge_unordered_list(f"_{name}.html")

    # Format tables
    ft.format_tables(f"_{name}.html")



if __name__ == '__main__':
    main()