from cgitb import text
import re
from turtle import position
import format_text as ft

INDENTATION = 10
INDENTATION_INDEX = 40


def open_html(filename, type="w"):
    ###
    # This function open a html file
    # Input:
    #   filename: string
    # Output:
    #   file: file
    ###
    return open(f"{filename}", type)

def close_html(file):
    ###
    # This function close a html file
    # Input:
    #   file: file
    # Output:
    #   None
    ###
    file.close()

def find_markdown_code(list_text):
    ###
    # This function find the markdown code in a list of text
    # Input:
    #   list_text: list
    # Output:
    #   list_text: list
    ###
    pos_start = 0
    pos_end = 0
    for i, text in enumerate(list_text):
        if text.startswith("```"):
            if pos_start == 0:
                pos_start = i
                continue
            else:
                pos_end = i
                list_text[pos_start] = "\n<code>\n"
                for j in range(pos_start+1, pos_end):
                    list_text[pos_start] = list_text[pos_start]+list_text[j]+"<br>"
                    list_text[j] = ""
                list_text[pos_start] = list_text[pos_start]+"</code>"
                list_text[pos_end] = ""
                pos_start = 0
                pos_end = 0
                continue
    return list_text

def get_level_index(text):
    ###
    # This function return the level of the header
    # Input:
    #   text: string
    # Output:
    #   level: int
    #   text: string
    ###
    level = 0
    while text[level] == "#":
        level += 1
    return level, text[level+1:]

def print_blank_line(file):
    ###
    # This function print a blank line in html file
    # Input:
    #   file: file
    # Output:
    #   None
    ###
    string = "\n"
    file.write(string)

def first_paragraph(file):
    ###
    # This function print the first paragraph in html file
    # Input:
    #   file: file
    # Output:
    #   None
    ###
    file.write("<p>")
    file.write("\n\t<!-- Custom stylesheet, it must be in the same directory as the html file -->")
    file.write("\n\t<!-- Loading mathjax macro --><!-- Load mathjax --><!-- MathJax configuration -->")
    file.write("\n<p>")
    file.write("\n")

def open_div_notebook(indentation, file):
    ###
    # This function print the open of the first div
    # Input:
    #   Indentation: int
    #   file: file
    # Output:
    #   None
    ###
    string = "\n"+("\t"*indentation)+'<!-- Open div notebook -->'
    file.write(string)
    string = "\n"+("\t"*indentation)+'<div id="notebook" class="border-box-sizing" tabindex="-1">'
    file.write(string)

def close_div_notebook(indentation, file):
    ###
    # This function print the close of the first div
    # Input:
    #   Indentation: int
    #   file: file
    # Output:
    #   None
    ###
    string = "\n"+("\t"*indentation)+'<!-- Close div notebook -->'
    file.write(string)
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)

def open_div_notebook_container(indentation, file):
    ###
    # This function print the open of the second div
    # Input:
    #   Indentation: int
    #   file: file
    # Output:
    #   None
    ###
    string = "\n"+("\t"*indentation)+'<!-- Open div notebook container -->'
    file.write(string)
    string = "\n"+("\t"*indentation)+'<div id="notebook-container" class="container">'
    file.write(string)

def close_div_notebook_container(indentation, file):
    ###
    # This function print the close of the second div
    # Input:
    #   Indentation: int
    #   file: file
    # Output:
    #   None
    ###
    string = "\n"+("\t"*indentation)+'<!-- Close div notebook container -->'
    file.write(string)
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)

def print_index_head(indentation, text, file):
    ###
    # This function print the head of the index
    # Input:
    #   Indentation: int
    #   text: string
    #   file: file
    # Output:
    #   None
    ###
    string = "\n"+("\t"*indentation)+'<!-- Open div index header -->'
    file.write(string)
    string = "\n"+("\t"*indentation)+'<div class="cell border-box-sizing text_cell rendered">'
    file.write(string)

    # indentation += 1
    string = "\n"+("\t"*(indentation+1))+'<h2 class="prompt input_prompt">'
    file.write(string)

    indentation += 1
    string = "\n"+("\t"*(indentation+1))+'<span style="'
    file.write(string)
    string = "\n"+("\t"*(indentation+1))+'color: var(--darkreader-text--heading-color, var(--darkreader-text--heading-2-color,'
    file.write(string)
    string = "\n"+("\t"*(indentation+1))+'var(--darkreader-text--headings-color)));'
    file.write(string)
    string = "\n"+("\t"*(indentation+1))+'font-family: var(--fontFamily); font-size: var(--fontSize);'
    file.write(string)
    string = "\n"+("\t"*(indentation+1))+'font-style: var(--fontStyle, inherit);'
    file.write(string)
    string = "\n"+("\t"*(indentation+1))+'font-weight: var(--fontWeight);'
    file.write(string)
    string = "\n"+("\t"*(indentation+1))+'letter-spacing: var(--letterSpacing);'
    file.write(string)
    string = "\n"+("\t"*(indentation+1))+'text-transform: var(--textTransform);'
    file.write(string)
    string = "\n"+("\t"*(indentation+1))+'background-color: transparent;'
    file.write(string)
    string = "\n"+("\t"*(indentation+1))+'--darkreader-inline-color: var(--darkreader-text--darkreader-text--heading-color,'
    file.write(string)
    string = "\n"+("\t"*(indentation+1))+'var(--darkreader-text--darkreader-text--heading-2-color, var(--darkreader-text--darkreader-text--headings-color)));'
    file.write(string)
    string = "\n"+("\t"*(indentation+1))+'--darkreader-inline-bgcolor: transparent;"'
    file.write(string)
    string = "\n"+("\t"*(indentation+1))+'data-darkreader-inline-color="" data-darkreader-inline-bgcolor="">'
    file.write(string)

    indentation += 1
    string = "\n"+("\t"*(indentation+1))+f'{text}'
    file.write(string)

    indentation -= 1
    string = "\n"+("\t"*(indentation+1))+'</span>'
    file.write(string)

    indentation += 1
    string = "\n"+("\t"*indentation)+'<a class="anchor-link" style="'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*(indentation+1))+'font-family: var(--fontFamily);'
    file.write(string)
    string = "\n"+("\t"*(indentation+1))+'font-size: var(--fontSize);'
    file.write(string)
    string = "\n"+("\t"*(indentation+1))+'font-style: var(--fontStyle, inherit);'
    file.write(string)
    string = "\n"+("\t"*(indentation+1))+'font-weight: var(--fontWeight);'
    file.write(string)
    string = "\n"+("\t"*(indentation+1))+'letter-spacing: var(--letterSpacing);'
    file.write(string)
    string = "\n"+("\t"*(indentation+1))+'text-transform: var(--textTransform);'
    file.write(string)
    string = "\n"+("\t"*(indentation+1))+'background-color: transparent;'
    file.write(string)
    string = "\n"+("\t"*(indentation+1))+'--darkreader-inline-bgcolor: transparent;"'
    file.write(string)
    href = text.replace(" ", "-")
    string = "\n"+("\t"*(indentation+1))+f'href="#{href}" data-darkreader-inline-bgcolor="">'
    file.write(string)
    string = "\n"+("\t"*(indentation+1))+'</a>'
    file.write(string)

    indentation -= 1
    string = "\n"+("\t"*(indentation+1))+'</h2>'
    file.write(string)

    # indentation -= 1
    string = "\n"+("\t"*indentation)+'<!-- Close div index header -->'
    file.write(string)
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    
    return indentation

def print_header_index(indentation, header_level, text_clean, text_formated, file, size=None):
    ###
    # This function print header into the index
    # Input:
    #   Indentation: int
    #   header_level: int
    #   text_clean: string
    #   text_formated: string
    #   file: file
    # Output:
    #   None
    ###
    string = "\n"+("\t"*indentation)+'<!-- Open div header -->'
    file.write(string)
    string = "\n"+("\t"*indentation)+'<div class="cell border-box-sizing text_cell rendered">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+'<div class="prompt input_prompt">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+'<div class="inner_cell">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+'<div class="text_cell_render border-box-sizing rendered_html">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+f'<h{header_level} id="{text_clean.replace(" ", "-")}-index">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+f'<a class="anchor-link" href="#{text_clean.replace(" ", "-")}">'
    file.write(string)
    indentation += 1
    if size is not None:
        string = "\n"+("\t"*indentation)+f'<p style="margin-left: {(header_level-2)*INDENTATION_INDEX}px; font-size: {size}px; line-height: 0%">'+f'{text_formated}'+'</p>'
    else:
        string = "\n"+("\t"*indentation)+f'<p style="margin-left: {(header_level-2)*INDENTATION_INDEX}px">'+f'{text_formated}'+'</p>'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</a>'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+f'</h{header_level}>'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    return indentation

def print_header(indentation, header_level, text_clean, text_formated, file):
    ###
    # This function print header output the index
    # Input:
    #   Indentation: int
    #   header_level: int
    #   text_clean: string
    #   text_formated: string
    #   file: file
    # Output:
    #   None
    ###
    string = "\n"+("\t"*indentation)+'<!-- Open div header -->'
    file.write(string)
    string = "\n"+("\t"*indentation)+'<div class="cell border-box-sizing text_cell rendered">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+'<div class="prompt input_prompt">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+'<div class="inner_cell">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+'<div class="text_cell_render border-box-sizing rendered_html">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+f'<h{header_level} id="{text_clean.replace(" ", "-")}">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+f'<a class="anchor-link" href="#{text_clean.replace(" ", "-")}">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+f'<p style="margin-left: {int(header_level-1)*INDENTATION}px">'+f'{text_formated}'+'</p>'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</a>'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+f'</h{header_level}>'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    return indentation

def print_text(indentation, text, file, margin_left=0):
    ###
    # This function print text of the notebook that is not a header
    # Input:
    #   Indentation: int
    #   text: string
    #   file: file
    # Output:
    #   None
    ###
    string = "\n"+("\t"*indentation)+'<div class="cell border-box-sizing text_cell rendered">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+'<div class="prompt input_prompt">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+'<div class="inner_cell">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+'<div class="text_cell_render border-box-sizing rendered_html">'
    file.write(string)
    indentation += 1
    text = text.replace("\n", "")
    string = "\n"+("\t"*indentation)+f'<p style="margin-left: {margin_left}px;">{text}'
    file.write(string)
    # string = "\n"+("\t"*indentation)+'</p>'
    string = '</p>'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    return indentation

def print_code(indentation, code, output, file, type_code="output_code"):
    ###
    # This function print code of the notebook
    # Input:
    #   Indentation: int
    #   code: string
    #   output: string
    #   file: file
    # Output:
    #   None
    ###
    string = "\n"+("\t"*indentation)+'<div class="cell border-box-sizing code_cell rendered">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+'<div class="input">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+f'<div class="prompt input_prompt" style="margin-left: {2*INDENTATION}px;">Code:</div>'
    file.write(string)
    # indentation += 1
    string = "\n"+("\t"*indentation)+'<div class="inner_cell">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+'<div class="input_area">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+'<div class=" highlight hl-python3">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+f'<pre style="margin-left: {4*INDENTATION}px">'
    file.write(string)
    indentation += 1
    for line in code:
        # print(line)
        string = "<p>"
        # Get spaces before the code
        spaces = re.search(r"^\s*", line)
        if spaces:
            spaces = spaces.group(0)
            string += spaces
        for w, word in enumerate(line.split(" ")):
            if "\n" in word:
                if len(word) > 1:
                    word = word.replace("\n", "")
                else:
                    word = word.replace("\n", " ")
            continue_line = False
            if word == "":
                continue_line = True
            string = string+'<span class="n">'+word
            if w == len(line.split(" "))-1:
                string = string+'</span></p>'
            else:
                string = string+' </span>'
        if continue_line:
            continue
        file.write(string)
    indentation -= 1
    # string = "\n"+("\t"*indentation)+'</pre>'
    string = '</pre>'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    # indentation += 1
    string = "\n"+("\t"*indentation)+'<div class="output_wrapper">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+'<div class="output">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+'<div class="output_area">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+f'<div class="prompt" style="margin-left: {2*INDENTATION}px;">Output:</div>'
    file.write(string)
    # indentation += 1
    if type_code == "output_code":
        string = "\n"+("\t"*indentation)+'<div class="output_subarea output_stream output_stdout output_text">'
        file.write(string)
        indentation += 1
        string = "\n"+("\t"*indentation)+f'<pre style="margin-left: {6*INDENTATION}px;">'
        file.write(string)
        indentation += 1
        for line in output:
            line = line.replace("\n", "")
            if line == "":
                continue
            string = "<p>"+line+"</p>"
            file.write(string)
        indentation -= 1
        # string = "\n"+("\t"*indentation)+'</pre>'
        string = '</pre>'
        file.write(string)
        indentation -= 1
        string = "\n"+("\t"*indentation)+'</div>'
        file.write(string)
        indentation -= 1
    elif type_code == "display_data":
        string = "\n"+("\t"*indentation)+'<div class="output_area">'
        file.write(string)
        indentation += 1
        string = "\n"+("\t"*indentation)+'<div class="prompt"></div>'
        file.write(string)
        # indentation += 1
        string = "\n"+("\t"*indentation)+f'<div class="output_png output_subarea" style="margin-left: {6*INDENTATION}px;"><img src="data:image/png;base64,{output}" /></div>'
        file.write(string)
        indentation -= 1
        string = "\n"+("\t"*indentation)+'</div>'
        file.write(string)
        indentation -= 1
    elif type_code == "error_code":
        string = "\n"+("\t"*indentation)+'<div class="output_subarea output_text output_error">'
        file.write(string)
        indentation += 1
        string = "\n"+("\t"*indentation)+f'<pre style="margin-left: {6*INDENTATION}px;">'
        file.write(string)
        indentation += 1
        for line in output:
            string = "<p>"+line+"</p>"
            file.write(string)
        indentation -= 1
        # string = "\n"+("\t"*indentation)+'</pre>'
        string = '</pre>'
        file.write(string)
        indentation -= 1
        string = "\n"+("\t"*indentation)+'</div>'
        file.write(string)
        indentation -= 1
        string = "\n"+("\t"*indentation)+'</div>'
        file.write(string)
        indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    return indentation

def print_index_body(indentation, headers, file):
    ###
    # This function print the body of the index
    # Input:
    #   Indentation: int
    #   headers: list
    #   file: file
    # Output:
    #   None
    ###
    string = "\n"+("\t"*indentation)+'<!-- Index body -->'
    file.write(string)
    string = "\n"+("\t"*indentation)+'<div>'
    file.write(string)
    indentation += 1
    for header in headers[1:]:
        level, text = get_level_index(header)
        text_clean, text_formated = ft.format_text(text)
        indentation = print_header_index(indentation, level, text_clean, text_formated, file, size=12)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    print_blank_line(file)
    return indentation

def print_content(indentation, cells, file):
    ###
    # This function print the content of the notebook
    # Input:
    #   Indentation: int
    #   cells: list
    #   file: file
    # Output:
    #   None
    ###
    string = "\n"+("\t"*indentation)+'<!-- Content -->'
    file.write(string)
    string = "\n"+("\t"*indentation)+'<div>'
    file.write(string)
    indentation += 1
    for c, cell in enumerate(cells):
        if cell['cell_type'] == 'markdown':
            if cell['source'][0].startswith('#'):
                level, text = get_level_index(cell['source'][0])
                text_clean, text_formated = ft.format_text(text)
                indentation = print_header(indentation, level, text_clean, text_formated, file)
            else:
                cell['source'] = find_markdown_code(cell['source'])
                for i in range(len(cell['source'])):
                    _, text_formated = ft.format_text(cell['source'][i])
                    if cell['source'][i].startswith('\n<code>'):
                        margin_left = 80
                    else:
                        margin_left = 0
                    indentation = print_text(indentation, text_formated, file, margin_left)
        elif cell['cell_type'] == 'code':
            if len(cell['outputs']) == 0:
                indentation = print_code(indentation, cell['source'], [], file, type_code="output_code")
            else:
                if cell['outputs'][0]['output_type'] == 'stream':
                    indentation = print_code(indentation, cell['source'], cell['outputs'][0]['text'], file, type_code="output_code")
                elif cell['outputs'][0]['output_type'] == 'display_data':
                    indentation = print_code(indentation, cell['source'], cell['outputs'][0]['data']['image/png'], file, type_code="display_data")
                elif cell['outputs'][0]['output_type'] == 'execute_result':
                    indentation = print_code(indentation, cell['source'], cell['outputs'][0]['data']['text/plain'], file, type_code="output_code")
                elif cell['outputs'][0]['output_type'] == 'error':
                    list_error_text = ft.pre_format_error_text(cell['outputs'][0]['traceback'])
                    list_error_text = ft.format_error_text(list_error_text)
                    indentation = print_code(indentation, cell['source'], list_error_text, file, type_code="error_code")
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    print_blank_line(file)
    return indentation