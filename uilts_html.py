from cgitb import text
import re

INDENTATION = 10
INDENTATION_INDEX = 40


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

def format_text(text):
    ###
    # This function change text in markdown format to html format
    # Input:
    #   text: string
    # Output:
    #   text: string
    ###
    text_clean = text
    # Replace link to a image in markdown format to html format
    text = re.sub(r'\!\[(.*?)\]\((.*?)\)', r'<p align="center"><img src="\2" alt="\1"></p>', text_clean)
    # Replace code block in markdown format to code html format
    text = re.sub(r'^```(.+?)```', r'<code>\1</code>', text)
    # Replace `*` for <code><b>*</code></b>
    text = re.sub(r'\`(.+?)\`', r'<code><b>\1</b></code>', text)
    # Replace ** for <b> tag
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # Replace * character for <em> tag
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Replace "* " for <ul> tag
    text = re.sub(r'\s?\*\s+(.+)', r'<ul><li>\1</li></ul>', text)
    # Replace "d " for <ol> tag (TODO: fix this)
    # text = re.sub(r'\s?\d\.\s+(.+)', r'<ol><li>\1</li></ol>', text)
    text_formated = text
    return text_clean, text_formated

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

def open_html(filename):
    ###
    # This function open a html file
    # Input:
    #   filename: string
    # Output:
    #   file: file
    ###
    return open(f"{filename}", 'w')

def close_html(file):
    ###
    # This function close a html file
    # Input:
    #   file: file
    # Output:
    #   None
    ###
    file.close()

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

def print_header_index(indentation, header_level, text_clean, text_formated, file):
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
    string = "\n"+("\t"*indentation)+f'<p style="margin-left: {margin_left}px">{text}'
    file.write(string)
    string = "\n"+("\t"*indentation)+'</p>'
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

def print_code(indentation, code, output, file):
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
    string = "\n"+("\t"*indentation)+'<div class="prompt input_prompt">Code:</div>'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+'<div class="inner_cell">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+'<div class="input_area">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+'<div class=" highlight hl-python">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+'<pre>'
    file.write(string)
    indentation += 1
    for line in code:
        string = "\n"+("\t"*indentation)
        for word in line.split(" "):
            word = word.replace("\n", "")
            string = string+'<span class="n">'+word+'</span> '
        file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</pre>'
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
    string = "\n"+("\t"*indentation)+'<div class="prompt output_prompt">Out:</div>'
    file.write(string)
    # indentation += 1
    string = "\n"+("\t"*indentation)+'<div class="output_text output_subarea output_execute_result">'
    file.write(string)
    indentation += 1
    string = "\n"+("\t"*indentation)+'<pre>'
    file.write(string)
    indentation += 1
    for line in output:
        string = "\n"+("\t"*indentation)
        print(f"line: {line}", type(line), line.keys())
        print(f"text: {line['text']}", type(line['text']))
        for subline in line['text']:
            print(f"subline: {subline}", type(subline))
            for word in subline.split(" "):
                word = word.replace("\n", "")
                string = string+word
        file.write(string)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</pre>'
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
        text_clean, text_formated = format_text(text)
        indentation = print_header_index(indentation, level, text_clean, text_formated, file)
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
        # if c > 12:
        #     break
        if cell['cell_type'] == 'markdown':
            if cell['source'][0].startswith('#'):
                level, text = get_level_index(cell['source'][0])
                text_clean, text_formated = format_text(text)
                indentation = print_header(indentation, level, text_clean, text_formated, file)
            else:
                cell['source'] = find_markdown_code(cell['source'])
                for i in range(len(cell['source'])):
                    _, text_formated = format_text(cell['source'][i])
                    if cell['source'][i].startswith('\n<code>'):
                        margin_left = 80
                    else:
                        margin_left = 0
                    indentation = print_text(indentation, text_formated, file, margin_left)
        elif cell['cell_type'] == 'code':
            print(cell['source'])
            print(cell['outputs'])
            indentation = print_code(indentation, cell['source'], cell['outputs'], file)
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    print_blank_line(file)
    return indentation