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

def format_error_text(list_text):
    ###
    # This function format the error text
    # Input:
    #   list_text: list
    # Output:
    #   list_text: list
    ###
    for i, text in enumerate(list_text):
        # Replace \x1b[0;30mtext\x1b\[0m for <span style="color:black">text</span>
        text = re.sub(r'\x1b\[0;30m(.+?)\x1b\[0m', r'<span style="color:black">\1</span>', text)
        # Replace \x1b[0;31mtext\x1b\[0m for <span style="color:red">text</span>
        text = re.sub(r'\x1b\[0;31m(.+?)\x1b\[0m', r'<span style="color:red">\1</span>', text)
        # Replace \x1b[0;32mtext\x1b\[0m for <span style="color:green">text</span>
        text = re.sub(r'\x1b\[0;32m(.+?)\x1b\[0m', r'<span style="color:green">\1</span>', text)
        # Replace \x1b[0;33mtext\x1b\[0m for <span style="color:yellow">text</span>
        text = re.sub(r'\x1b\[0;33m(.+?)\x1b\[0m', r'<span style="color:yellow">\1</span>', text)
        # Replace \x1b[0;34mtext\x1b\[0m for <span style="color:blue">text</span>
        text = re.sub(r'\x1b\[0;34m(.+?)\x1b\[0m', r'<span style="color:blue">\1</span>', text)
        # Replace \x1b[0;35mtext\x1b\[0m for <span style="color:magenta">text</span>
        text = re.sub(r'\x1b\[0;35m(.+?)\x1b\[0m', r'<span style="color:magenta">\1</span>', text)
        # Replace \x1b[0;36mtext\x1b\[0m for <span style="color:cyan">text</span>
        text = re.sub(r'\x1b\[0;36m(.+?)\x1b\[0m', r'<span style="color:cyan">\1</span>', text)
        # Replace \x1b[0;37mtext\x1b\[0m for <span style="color:white">text</span>
        text = re.sub(r'\x1b\[0;37m(.+?)\x1b\[0m', r'<span style="color:white">\1</span>', text)

        # Replace \x1b[1;30mtext\x1b\[0m for <span style="color:black"><b>text</b></span>
        text = re.sub(r'\x1b\[1;30m(.+?)\x1b\[0m', r'<span style="color:black"><b>\1</b></span>', text)
        # Replace \x1b[1;31mtext\x1b\[0m for <span style="color:red"><b>text</b></span>
        text = re.sub(r'\x1b\[1;31m(.+?)\x1b\[0m', r'<span style="color:red"><b>\1</b></span>', text)
        # Replace \x1b[1;32mtext\x1b\[0m for <span style="color:green"><b>text</b></span>
        text = re.sub(r'\x1b\[1;32m(.+?)\x1b\[0m', r'<span style="color:green"><b>\1</b></span>', text)
        # Replace \x1b[1;33mtext\x1b\[0m for <span style="color:yellow"><b>text</b></span>
        text = re.sub(r'\x1b\[1;33m(.+?)\x1b\[0m', r'<span style="color:yellow"><b>\1</b></span>', text)
        # Replace \x1b[1;34mtext\x1b\[0m for <span style="color:blue"><b>text</b></span>
        text = re.sub(r'\x1b\[1;34m(.+?)\x1b\[0m', r'<span style="color:blue"><b>\1</b></span>', text)
        # Replace \x1b[1;35mtext\x1b\[0m for <span style="color:magenta"><b>text</b></span>
        text = re.sub(r'\x1b\[1;35m(.+?)\x1b\[0m', r'<span style="color:magenta"><b>\1</b></span>', text)
        # Replace \x1b[1;36mtext\x1b\[0m for <span style="color:cyan"><b>text</b></span>
        text = re.sub(r'\x1b\[1;36m(.+?)\x1b\[0m', r'<span style="color:cyan"><b>\1</b></span>', text)
        # Replace \x1b[1;37mtext\x1b\[0m for <span style="color:white"><b>text</b></span>
        text = re.sub(r'\x1b\[1;37m(.+?)\x1b\[0m', r'<span style="color:white"><b>\1</b></span>', text)

        # Replace \x1b[4;30mtext\x1b\[0m for <span style="color:black"><u>text</u></span>
        text = re.sub(r'\x1b\[4;30m(.+?)\x1b\[0m', r'<span style="color:black"><u>\1</u></span>', text)
        # Replace \x1b[4;31mtext\x1b\[0m for <span style="color:red"><u>text</u></span>
        text = re.sub(r'\x1b\[4;31m(.+?)\x1b\[0m', r'<span style="color:red"><u>\1</u></span>', text)
        # Replace \x1b[4;32mtext\x1b\[0m for <span style="color:green"><u>text</u></span>
        text = re.sub(r'\x1b\[4;32m(.+?)\x1b\[0m', r'<span style="color:green"><u>\1</u></span>', text)
        # Replace \x1b[4;33mtext\x1b\[0m for <span style="color:yellow"><u>text</u></span>
        text = re.sub(r'\x1b\[4;33m(.+?)\x1b\[0m', r'<span style="color:yellow"><u>\1</u></span>', text)
        # Replace \x1b[4;34mtext\x1b\[0m for <span style="color:blue"><u>text</u></span>
        text = re.sub(r'\x1b\[4;34m(.+?)\x1b\[0m', r'<span style="color:blue"><u>\1</u></span>', text)
        # Replace \x1b[4;35mtext\x1b\[0m for <span style="color:magenta"><u>text</u></span>
        text = re.sub(r'\x1b\[4;35m(.+?)\x1b\[0m', r'<span style="color:magenta"><u>\1</u></span>', text)
        # Replace \x1b[4;36mtext\x1b\[0m for <span style="color:cyan"><u>text</u></span>
        text = re.sub(r'\x1b\[4;36m(.+?)\x1b\[0m', r'<span style="color:cyan"><u>\1</u></span>', text)
        # Replace \x1b[4;37mtext\x1b\[0m for <span style="color:white"><u>text</u></span>
        text = re.sub(r'\x1b\[4;37m(.+?)\x1b\[0m', r'<span style="color:white"><u>\1</u></span>', text)

        # Replace \x1b[40mtext\x1b\[0m for <span style="background-color:black">text</span>
        text = re.sub(r'\x1b\[40m(.+?)\x1b\[0m', r'<span style="background-color:black">\1</span>', text)
        # Replace \x1b[41mtext\x1b\[0m for <span style="background-color:red">text</span>
        text = re.sub(r'\x1b\[41m(.+?)\x1b\[0m', r'<span style="background-color:red">\1</span>', text)
        # Replace \x1b[42mtext\x1b\[0m for <span style="background-color:green">text</span>
        text = re.sub(r'\x1b\[42m(.+?)\x1b\[0m', r'<span style="background-color:green">\1</span>', text)
        # Replace \x1b[43mtext\x1b\[0m for <span style="background-color:yellow">text</span>
        text = re.sub(r'\x1b\[43m(.+?)\x1b\[0m', r'<span style="background-color:yellow">\1</span>', text)
        # Replace \x1b[44mtext\x1b\[0m for <span style="background-color:blue">text</span>
        text = re.sub(r'\x1b\[44m(.+?)\x1b\[0m', r'<span style="background-color:blue">\1</span>', text)
        # Replace \x1b[45mtext\x1b\[0m for <span style="background-color:magenta">text</span>
        text = re.sub(r'\x1b\[45m(.+?)\x1b\[0m', r'<span style="background-color:magenta">\1</span>', text)
        # Replace \x1b[46mtext\x1b\[0m for <span style="background-color:cyan">text</span>
        text = re.sub(r'\x1b\[46m(.+?)\x1b\[0m', r'<span style="background-color:cyan">\1</span>', text)
        # Replace \x1b[47mtext\x1b\[0m for <span style="background-color:white">text</span>
        text = re.sub(r'\x1b\[47m(.+?)\x1b\[0m', r'<span style="background-color:white">\1</span>', text)

        # Replace \x1b[0;90mtext\x1b\[0m for <span style="color:grey">text</span>
        text = re.sub(r'\x1b\[0;90m(.+?)\x1b\[0m', r'<span style="color:grey">\1</span>', text)
        # Replace \x1b[0;91mtext\x1b\[0m for <span style="color:red">text</span>
        text = re.sub(r'\x1b\[0;91m(.+?)\x1b\[0m', r'<span style="color:red">\1</span>', text)
        # Replace \x1b[0;92mtext\x1b\[0m for <span style="color:green">text</span>
        text = re.sub(r'\x1b\[0;92m(.+?)\x1b\[0m', r'<span style="color:green">\1</span>', text)
        # Replace \x1b[0;93mtext\x1b\[0m for <span style="color:yellow">text</span>
        text = re.sub(r'\x1b\[0;93m(.+?)\x1b\[0m', r'<span style="color:yellow">\1</span>', text)
        # Replace \x1b[0;94mtext\x1b\[0m for <span style="color:blue">text</span>
        text = re.sub(r'\x1b\[0;94m(.+?)\x1b\[0m', r'<span style="color:blue">\1</span>', text)
        # Replace \x1b[0;95mtext\x1b\[0m for <span style="color:magenta">text</span>
        text = re.sub(r'\x1b\[0;95m(.+?)\x1b\[0m', r'<span style="color:magenta">\1</span>', text)
        # Replace \x1b[0;96mtext\x1b\[0m for <span style="color:cyan">text</span>
        text = re.sub(r'\x1b\[0;96m(.+?)\x1b\[0m', r'<span style="color:cyan">\1</span>', text)
        # Replace \x1b[0;97mtext\x1b\[0m for <span style="color:white">text</span>
        text = re.sub(r'\x1b\[0;97m(.+?)\x1b\[0m', r'<span style="color:white">\1</span>', text)

        # Replace \x1b[1;90mtext\x1b\[0m for <span style="color:grey"><b>text</b></span>
        text = re.sub(r'\x1b\[1;90m(.+?)\x1b\[0m', r'<span style="color:grey"><b>\1</b></span>', text)
        # Replace \x1b[1;91mtext\x1b\[0m for <span style="color:red"><b>text</b></span>
        text = re.sub(r'\x1b\[1;91m(.+?)\x1b\[0m', r'<span style="color:red"><b>\1</b></span>', text)
        # Replace \x1b[1;92mtext\x1b\[0m for <span style="color:green"><b>text</b></span>
        text = re.sub(r'\x1b\[1;92m(.+?)\x1b\[0m', r'<span style="color:green"><b>\1</b></span>', text)
        # Replace \x1b[1;93mtext\x1b\[0m for <span style="color:yellow"><b>text</b></span>
        text = re.sub(r'\x1b\[1;93m(.+?)\x1b\[0m', r'<span style="color:yellow"><b>\1</b></span>', text)
        # Replace \x1b[1;94mtext\x1b\[0m for <span style="color:blue"><b>text</b></span>
        text = re.sub(r'\x1b\[1;94m(.+?)\x1b\[0m', r'<span style="color:blue"><b>\1</b></span>', text)
        # Replace \x1b[1;95mtext\x1b\[0m for <span style="color:magenta"><b>text</b></span>
        text = re.sub(r'\x1b\[1;95m(.+?)\x1b\[0m', r'<span style="color:magenta"><b>\1</b></span>', text)
        # Replace \x1b[1;96mtext\x1b\[0m for <span style="color:cyan"><b>text</b></span>
        text = re.sub(r'\x1b\[1;96m(.+?)\x1b\[0m', r'<span style="color:cyan"><b>\1</b></span>', text)
        # Replace \x1b[1;97mtext\x1b\[0m for <span style="color:white"><b>text</b></span>
        text = re.sub(r'\x1b\[1;97m(.+?)\x1b\[0m', r'<span style="color:white"><b>\1</b></span>', text)

        # Replace \x1b[0;100mtext\x1b\[0m for <span style="background-color:grey">text</span>
        text = re.sub(r'\x1b\[0;100m(.+?)\x1b\[0m', r'<span style="background-color:grey">\1</span>', text)
        # Replace \x1b[0;101mtext\x1b\[0m for <span style="background-color:red">text</span>
        text = re.sub(r'\x1b\[0;101m(.+?)\x1b\[0m', r'<span style="background-color:red">\1</span>', text)
        # Replace \x1b[0;102mtext\x1b\[0m for <span style="background-color:green">text</span>
        text = re.sub(r'\x1b\[0;102m(.+?)\x1b\[0m', r'<span style="background-color:green">\1</span>', text)
        # Replace \x1b[0;103mtext\x1b\[0m for <span style="background-color:yellow">text</span>
        text = re.sub(r'\x1b\[0;103m(.+?)\x1b\[0m', r'<span style="background-color:yellow">\1</span>', text)
        # Replace \x1b[0;104mtext\x1b\[0m for <span style="background-color:blue">text</span>
        text = re.sub(r'\x1b\[0;104m(.+?)\x1b\[0m', r'<span style="background-color:blue">\1</span>', text)
        # Replace \x1b[0;105mtext\x1b\[0m for <span style="background-color:magenta">text</span>
        text = re.sub(r'\x1b\[0;105m(.+?)\x1b\[0m', r'<span style="background-color:magenta">\1</span>', text)
        # Replace \x1b[0;106mtext\x1b\[0m for <span style="background-color:cyan">text</span>
        text = re.sub(r'\x1b\[0;106m(.+?)\x1b\[0m', r'<span style="background-color:cyan">\1</span>', text)
        # Replace \x1b[0;107mtext\x1b\[0m for <span style="background-color:white">text</span>
        text = re.sub(r'\x1b\[0;107m(.+?)\x1b\[0m', r'<span style="background-color:white">\1</span>', text)

        # if \n is in text, replace it for <br>
        texts = text.split('\n')
        print(f"texts: {texts}")
        # text = re.sub(r'\n', r'<br>', text)

        list_text[i] = text
    print(list_text)
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
    string = "\n"+("\t"*indentation)+'<div class="prompt input_prompt">Code:</div>'
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
    if type_code == "output_code":
        string = "\n"+("\t"*indentation)+'<div class="output_text output_subarea output_execute_result">'
        file.write(string)
        indentation += 1
        string = "\n"+("\t"*indentation)+'<pre>'
        file.write(string)
        indentation += 1
        for line in output:
            line = line.replace("\n", "")
            string = "\n"+("\t"*indentation)+line
            file.write(string)
        indentation -= 1
        string = "\n"+("\t"*indentation)+'</pre>'
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
        string = "\n"+("\t"*indentation)+f'<div class="output_png output_subarea "><img src="data:image/png;base64,{output}" /></div>'
        file.write(string)
        indentation -= 1
        string = "\n"+("\t"*indentation)+'</div>'
        file.write(string)
        indentation -= 1
    elif type_code == "error_code":
        string = "\n"+("\t"*indentation)+'<div class="output_subarea output_text output_error">'
        file.write(string)
        indentation += 1
        string = "\n"+("\t"*indentation)+'<pre>'
        file.write(string)
        indentation += 1
        for line in output:
            string = "\n"+("\t"*indentation)+line
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
                    print(cell['outputs'][0]['traceback'])
                    list_error_text = format_error_text(cell['outputs'][0]['traceback'])
                    indentation = print_code(indentation, cell['source'], list_error_text, file, type_code="error_code")
                    break
    indentation -= 1
    string = "\n"+("\t"*indentation)+'</div>'
    file.write(string)
    print_blank_line(file)
    return indentation