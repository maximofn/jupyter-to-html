from cgitb import text


def format_text(text):
    text_clean = text.replace("`", "")
    # Replace ` character for <code> tag
    while "`" in text:
        pos_init = text.find("`")
        pos_end = text.find("`", pos_init+1)
        if pos_end == -1:
            break
        text = text[:pos_init] + f'<code>{text[pos_init+1:pos_end]}</code>' + text[pos_end+1:]
    # Replace ** for <b> tag
    while "**" in text:
        pos_init = text.find("**")
        pos_end = text.find("**", pos_init+1)
        if pos_end == -1:
            break
        text = text[:pos_init] + f'<b>{text[pos_init+2:pos_end]}</b>' + text[pos_end+2:]
    # Replace * character for <em> tag
    while "*" in text:
        pos_init = text.find("*")
        pos_end = text.find("*", pos_init+1)
        if pos_end == -1:
            break
        text = text[:pos_init] + f'<em>{text[pos_init+1:pos_end]}</em>' + text[pos_end+1:]
    # Replace "* " for <ul> tag
    while "* " in text:
        text = text.replace("* ", "<ul><li>", 1)
        text = text[0:-1] + "</li></ul>" + text[-1]
    text_formated = text
    return text_clean, text_formated

def get_level_index(text):
    level = 0
    while text[level] == "#":
        level += 1
    return level, text[level+1:]

def open_html(filename):
    return open(f"{filename}", 'w')

def close_html(file):
    file.close()

def print_blank_line(file):
    string = "\n"
    file.write(string)

def first_paragraph(file):
    file.write("<p>")
    file.write("\n\t<!-- Custom stylesheet, it must be in the same directory as the html file -->")
    file.write("\n\t<!-- Loading mathjax macro --><!-- Load mathjax --><!-- MathJax configuration -->")
    file.write("\n<p>")
    file.write("\n")

def open_div_notebook(indentation, file):
    string = "\n"+("\t"*indentation)+'<!-- Open div notebook -->'
    file.write(string)
    string = "\n"+("\t"*indentation)+'<div id="notebook" class="border-box-sizing" tabindex="-1">'
    file.write(string)

def close_div_notebook(indentation, file):
    string = "\n"+("\t"*indentation)+'<!-- Close div notebook -->'
    file.write(string)
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)

def open_div_notebook_container(indentation, file):
    string = "\n"+("\t"*indentation)+'<!-- Open div notebook container -->'
    file.write(string)
    string = "\n"+("\t"*indentation)+'<div id="notebook-container" class="container">'
    file.write(string)

def close_div_notebook_container(indentation, file):
    string = "\n"+("\t"*indentation)+'<!-- Close div notebook container -->'
    file.write(string)
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)

def print_index_head(indentation, text, file):
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
    string = "\n"+("\t"*indentation)+f'<p style="margin-left: {(header_level-2)*40}px">'+f'{text_formated}'+'</p>'
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
    string = "\n"+("\t"*indentation)+f'<p style="margin-left: {(header_level-2)*40}px">'+f'{text_formated}'+'</p>'
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

def print_text(indentation, text, file):
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
    string = "\n"+("\t"*indentation)+f'<p>{text}'
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

def print_index_body(indentation, headers, file):
    string = "\n"+("\t"*indentation)+'<!-- Index body -->'
    file.write(string)
    for header in headers[1:]:
        level, text = get_level_index(header)
        text_clean, text_formated = format_text(text)
        indentation = print_header_index(indentation, level, text_clean, text_formated, file)
    print_blank_line(file)
    return indentation

def print_content(indentation, cells, file):
    string = "\n"+("\t"*indentation)+'<!-- Content -->'
    file.write(string)
    for cell in cells:
        if cell['cell_type'] == 'markdown':
            if cell['source'][0].startswith('#'):
                level, text = get_level_index(cell['source'][0])
                text_clean, text_formated = format_text(text)
                indentation = print_header(indentation, level, text_clean, text_formated, file)
            else:
                for i in range(len(cell['source'])):
                    _, text_formated = format_text(cell['source'][i])
                    indentation = print_text(indentation, text_formated, file)
    print_blank_line(file)
    return indentation