import re
import numpy as np


def format_text(text, header=False):
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
    # Replace link in markdown format to html format
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" target="_blank">\1</a>', text)
    # Replace code block in markdown format to code html format
    text = re.sub(r'^```(.+?)```', r'<code>\1</code>', text)
    # Replace `*` for <code><b>*</code></b>
    text = re.sub(r'\`(.+?)\`', r'<code><b>\1</b></code>', text)
    # Replace ** for <b> tag
    text = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', text)
    # Replace * character for <em> tag
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)
    # Replace "* " for <ul> tag
    lines = re.findall(r'^\s*\*\s+(.+?)$', text, re.MULTILINE)
    for line in lines:
        pos = text.find('*')+1
        text = re.sub(r'^\s*\*\s+(.+?)$', r'\1', text)
        text = ("<ul>"*pos) + f"<li>{text}</li>" + ("</ul>"*pos)
    # Replace "d " for <ol> tag (TODO: fix this)
    lines = re.findall(r'^\s*\d+.\s+(.+?)$', text, re.MULTILINE)
    for line in lines:
        if not header:
            pos = text.find('.')+1
            text = re.sub(r'^\s*\d+.\s+(.+?)$', r'\1', text)
            text = ("<ol>"*pos) + f"<oli>{text}</oli>" + ("</ol>"*pos)
    # Return the text
    text_formated = text
    return text_clean, text_formated

def pre_format_error_text(list_text):
    ###
    # This function replace < and > for &lt; and &gt; in a list of text
    # Input:
    #   list_text: list
    # Output:
    #   list_text: list
    ###
    for i, text in enumerate(list_text):
        # Replace < and > for &lt; and &gt;
        text = re.sub(r'<', r'&lt;', text)
        text = re.sub(r'>', r'&gt;', text)
        list_text[i] = text
    return list_text

def format_error_text(list_text):
    ###
    # This function format the error text
    # Input:
    #   list_text: list
    # Output:
    #   list_text: list
    ###
    for i, text in enumerate(list_text):
        # Replace \x1b\[0;30mtext\x1b\[0m for <span style="color:black">text</span>
        text = re.sub(r'\x1b\[0;30m(.+?)\x1b\[0m', r'<span style="color:black">\1</span>', text)
        # Replace \x1b\[0;31mtext\x1b\[0m for <span style="color:red">text</span>
        text = re.sub(r'\x1b\[0;31m(.+?)\x1b\[0m', r'<span style="color:red">\1</span>', text)
        # Replace \x1b\[0;32mtext\x1b\[0m for <span style="color:green">text</span>
        text = re.sub(r'\x1b\[0;32m(.+?)\x1b\[0m', r'<span style="color:green">\1</span>', text)
        # Replace \x1b\[0;33mtext\x1b\[0m for <span style="color:yellow">text</span>
        text = re.sub(r'\x1b\[0;33m(.+?)\x1b\[0m', r'<span style="color:yellow">\1</span>', text)
        # Replace \x1b\[0;34mtext\x1b\[0m for <span style="color:blue">text</span>
        text = re.sub(r'\x1b\[0;34m(.+?)\x1b\[0m', r'<span style="color:blue">\1</span>', text)
        # Replace \x1b\[0;35mtext\x1b\[0m for <span style="color:magenta">text</span>
        text = re.sub(r'\x1b\[0;35m(.+?)\x1b\[0m', r'<span style="color:magenta">\1</span>', text)
        # Replace \x1b\[0;36mtext\x1b\[0m for <span style="color:cyan">text</span>
        text = re.sub(r'\x1b\[0;36m(.+?)\x1b\[0m', r'<span style="color:cyan">\1</span>', text)
        # Replace \x1b\[0;37mtext\x1b\[0m for <span style="color:white">text</span>
        text = re.sub(r'\x1b\[0;37m(.+?)\x1b\[0m', r'<span style="color:white">\1</span>', text)

        # Replace \x1b\[1;30mtext\x1b\[0m for <span style="color:black"><b>text</b></span>
        text = re.sub(r'\x1b\[1;30m(.+?)\x1b\[0m', r'<span style="color:black"><b>\1</b></span>', text)
        # Replace \x1b\[1;31mtext\x1b\[0m for <span style="color:red"><b>text</b></span>
        text = re.sub(r'\x1b\[1;31m(.+?)\x1b\[0m', r'<span style="color:red"><b>\1</b></span>', text)
        # Replace \x1b\[1;32mtext\x1b\[0m for <span style="color:green"><b>text</b></span>
        text = re.sub(r'\x1b\[1;32m(.+?)\x1b\[0m', r'<span style="color:green"><b>\1</b></span>', text)
        # Replace \x1b\[1;33mtext\x1b\[0m for <span style="color:yellow"><b>text</b></span>
        text = re.sub(r'\x1b\[1;33m(.+?)\x1b\[0m', r'<span style="color:yellow"><b>\1</b></span>', text)
        # Replace \x1b\[1;34mtext\x1b\[0m for <span style="color:blue"><b>text</b></span>
        text = re.sub(r'\x1b\[1;34m(.+?)\x1b\[0m', r'<span style="color:blue"><b>\1</b></span>', text)
        # Replace \x1b\[1;35mtext\x1b\[0m for <span style="color:magenta"><b>text</b></span>
        text = re.sub(r'\x1b\[1;35m(.+?)\x1b\[0m', r'<span style="color:magenta"><b>\1</b></span>', text)
        # Replace \x1b\[1;36mtext\x1b\[0m for <span style="color:cyan"><b>text</b></span>
        text = re.sub(r'\x1b\[1;36m(.+?)\x1b\[0m', r'<span style="color:cyan"><b>\1</b></span>', text)
        # Replace \x1b\[1;37mtext\x1b\[0m for <span style="color:white"><b>text</b></span>
        text = re.sub(r'\x1b\[1;37m(.+?)\x1b\[0m', r'<span style="color:white"><b>\1</b></span>', text)

        # Replace \x1b\[4;30mtext\x1b\[0m for <span style="color:black"><u>text</u></span>
        text = re.sub(r'\x1b\[4;30m(.+?)\x1b\[0m', r'<span style="color:black"><u>\1</u></span>', text)
        # Replace \x1b\[4;31mtext\x1b\[0m for <span style="color:red"><u>text</u></span>
        text = re.sub(r'\x1b\[4;31m(.+?)\x1b\[0m', r'<span style="color:red"><u>\1</u></span>', text)
        # Replace \x1b\[4;32mtext\x1b\[0m for <span style="color:green"><u>text</u></span>
        text = re.sub(r'\x1b\[4;32m(.+?)\x1b\[0m', r'<span style="color:green"><u>\1</u></span>', text)
        # Replace \x1b\[4;33mtext\x1b\[0m for <span style="color:yellow"><u>text</u></span>
        text = re.sub(r'\x1b\[4;33m(.+?)\x1b\[0m', r'<span style="color:yellow"><u>\1</u></span>', text)
        # Replace \x1b\[4;34mtext\x1b\[0m for <span style="color:blue"><u>text</u></span>
        text = re.sub(r'\x1b\[4;34m(.+?)\x1b\[0m', r'<span style="color:blue"><u>\1</u></span>', text)
        # Replace \x1b\[4;35mtext\x1b\[0m for <span style="color:magenta"><u>text</u></span>
        text = re.sub(r'\x1b\[4;35m(.+?)\x1b\[0m', r'<span style="color:magenta"><u>\1</u></span>', text)
        # Replace \x1b\[4;36mtext\x1b\[0m for <span style="color:cyan"><u>text</u></span>
        text = re.sub(r'\x1b\[4;36m(.+?)\x1b\[0m', r'<span style="color:cyan"><u>\1</u></span>', text)
        # Replace \x1b\[4;37mtext\x1b\[0m for <span style="color:white"><u>text</u></span>
        text = re.sub(r'\x1b\[4;37m(.+?)\x1b\[0m', r'<span style="color:white"><u>\1</u></span>', text)

        # Replace \x1b\[40mtext\x1b\[0m for <span style="background-color:black">text</span>
        text = re.sub(r'\x1b\[40m(.+?)\x1b\[0m', r'<span style="background-color:black">\1</span>', text)
        # Replace \x1b\[41mtext\x1b\[0m for <span style="background-color:red">text</span>
        text = re.sub(r'\x1b\[41m(.+?)\x1b\[0m', r'<span style="background-color:red">\1</span>', text)
        # Replace \x1b\[42mtext\x1b\[0m for <span style="background-color:green">text</span>
        text = re.sub(r'\x1b\[42m(.+?)\x1b\[0m', r'<span style="background-color:green">\1</span>', text)
        # Replace \x1b\[43mtext\x1b\[0m for <span style="background-color:yellow">text</span>
        text = re.sub(r'\x1b\[43m(.+?)\x1b\[0m', r'<span style="background-color:yellow">\1</span>', text)
        # Replace \x1b\[44mtext\x1b\[0m for <span style="background-color:blue">text</span>
        text = re.sub(r'\x1b\[44m(.+?)\x1b\[0m', r'<span style="background-color:blue">\1</span>', text)
        # Replace \x1b\[45mtext\x1b\[0m for <span style="background-color:magenta">text</span>
        text = re.sub(r'\x1b\[45m(.+?)\x1b\[0m', r'<span style="background-color:magenta">\1</span>', text)
        # Replace \x1b\[46mtext\x1b\[0m for <span style="background-color:cyan">text</span>
        text = re.sub(r'\x1b\[46m(.+?)\x1b\[0m', r'<span style="background-color:cyan">\1</span>', text)
        # Replace \x1b\[47mtext\x1b\[0m for <span style="background-color:white">text</span>
        text = re.sub(r'\x1b\[47m(.+?)\x1b\[0m', r'<span style="background-color:white">\1</span>', text)

        # Replace \x1b\[0;90mtext\x1b\[0m for <span style="color:grey">text</span>
        text = re.sub(r'\x1b\[0;90m(.+?)\x1b\[0m', r'<span style="color:grey">\1</span>', text)
        # Replace \x1b\[0;91mtext\x1b\[0m for <span style="color:red">text</span>
        text = re.sub(r'\x1b\[0;91m(.+?)\x1b\[0m', r'<span style="color:red">\1</span>', text)
        # Replace \x1b\[0;92mtext\x1b\[0m for <span style="color:green">text</span>
        text = re.sub(r'\x1b\[0;92m(.+?)\x1b\[0m', r'<span style="color:green">\1</span>', text)
        # Replace \x1b\[0;93mtext\x1b\[0m for <span style="color:yellow">text</span>
        text = re.sub(r'\x1b\[0;93m(.+?)\x1b\[0m', r'<span style="color:yellow">\1</span>', text)
        # Replace \x1b\[0;94mtext\x1b\[0m for <span style="color:blue">text</span>
        text = re.sub(r'\x1b\[0;94m(.+?)\x1b\[0m', r'<span style="color:blue">\1</span>', text)
        # Replace \x1b\[0;95mtext\x1b\[0m for <span style="color:magenta">text</span>
        text = re.sub(r'\x1b\[0;95m(.+?)\x1b\[0m', r'<span style="color:magenta">\1</span>', text)
        # Replace \x1b\[0;96mtext\x1b\[0m for <span style="color:cyan">text</span>
        text = re.sub(r'\x1b\[0;96m(.+?)\x1b\[0m', r'<span style="color:cyan">\1</span>', text)
        # Replace \x1b\[0;97mtext\x1b\[0m for <span style="color:white">text</span>
        text = re.sub(r'\x1b\[0;97m(.+?)\x1b\[0m', r'<span style="color:white">\1</span>', text)

        # Replace \x1b\[1;90mtext\x1b\[0m for <span style="color:grey"><b>text</b></span>
        text = re.sub(r'\x1b\[1;90m(.+?)\x1b\[0m', r'<span style="color:grey"><b>\1</b></span>', text)
        # Replace \x1b\[1;91mtext\x1b\[0m for <span style="color:red"><b>text</b></span>
        text = re.sub(r'\x1b\[1;91m(.+?)\x1b\[0m', r'<span style="color:red"><b>\1</b></span>', text)
        # Replace \x1b\[1;92mtext\x1b\[0m for <span style="color:green"><b>text</b></span>
        text = re.sub(r'\x1b\[1;92m(.+?)\x1b\[0m', r'<span style="color:green"><b>\1</b></span>', text)
        # Replace \x1b\[1;93mtext\x1b\[0m for <span style="color:yellow"><b>text</b></span>
        text = re.sub(r'\x1b\[1;93m(.+?)\x1b\[0m', r'<span style="color:yellow"><b>\1</b></span>', text)
        # Replace \x1b\[1;94mtext\x1b\[0m for <span style="color:blue"><b>text</b></span>
        text = re.sub(r'\x1b\[1;94m(.+?)\x1b\[0m', r'<span style="color:blue"><b>\1</b></span>', text)
        # Replace \x1b\[1;95mtext\x1b\[0m for <span style="color:magenta"><b>text</b></span>
        text = re.sub(r'\x1b\[1;95m(.+?)\x1b\[0m', r'<span style="color:magenta"><b>\1</b></span>', text)
        # Replace \x1b\[1;96mtext\x1b\[0m for <span style="color:cyan"><b>text</b></span>
        text = re.sub(r'\x1b\[1;96m(.+?)\x1b\[0m', r'<span style="color:cyan"><b>\1</b></span>', text)
        # Replace \x1b\[1;97mtext\x1b\[0m for <span style="color:white"><b>text</b></span>
        text = re.sub(r'\x1b\[1;97m(.+?)\x1b\[0m', r'<span style="color:white"><b>\1</b></span>', text)

        # Replace \x1b\[0;100mtext\x1b\[0m for <span style="background-color:grey">text</span>
        text = re.sub(r'\x1b\[0;100m(.+?)\x1b\[0m', r'<span style="background-color:grey">\1</span>', text)
        # Replace \x1b\[0;101mtext\x1b\[0m for <span style="background-color:red">text</span>
        text = re.sub(r'\x1b\[0;101m(.+?)\x1b\[0m', r'<span style="background-color:red">\1</span>', text)
        # Replace \x1b\[0;102mtext\x1b\[0m for <span style="background-color:green">text</span>
        text = re.sub(r'\x1b\[0;102m(.+?)\x1b\[0m', r'<span style="background-color:green">\1</span>', text)
        # Replace \x1b\[0;103mtext\x1b\[0m for <span style="background-color:yellow">text</span>
        text = re.sub(r'\x1b\[0;103m(.+?)\x1b\[0m', r'<span style="background-color:yellow">\1</span>', text)
        # Replace \x1b\[0;104mtext\x1b\[0m for <span style="background-color:blue">text</span>
        text = re.sub(r'\x1b\[0;104m(.+?)\x1b\[0m', r'<span style="background-color:blue">\1</span>', text)
        # Replace \x1b\[0;105mtext\x1b\[0m for <span style="background-color:magenta">text</span>
        text = re.sub(r'\x1b\[0;105m(.+?)\x1b\[0m', r'<span style="background-color:magenta">\1</span>', text)
        # Replace \x1b\[0;106mtext\x1b\[0m for <span style="background-color:cyan">text</span>
        text = re.sub(r'\x1b\[0;106m(.+?)\x1b\[0m', r'<span style="background-color:cyan">\1</span>', text)
        # Replace \x1b\[0;107mtext\x1b\[0m for <span style="background-color:white">text</span>
        text = re.sub(r'\x1b\[0;107m(.+?)\x1b\[0m', r'<span style="background-color:white">\1</span>', text)

        # Remove \x1b\[0;30m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;30m', r'', text)
        # Remove \x1b\[0;31m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;31m', r'', text)
        # Remove \x1b\[0;32m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;32m', r'', text)
        # Remove \x1b\[0;33m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;33m', r'', text)
        # Remove \x1b\[0;34m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;34m', r'', text)
        # Remove \x1b\[0;35m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;35m', r'', text)
        # Remove \x1b\[0;36m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;36m', r'', text)
        # Remove \x1b\[0;37m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;37m', r'', text)

        # Remove \x1b\[1;30m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[1;30m', r'', text)
        # Remove \x1b\[1;31m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[1;31m', r'', text)
        # Remove \x1b\[1;32m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[1;32m', r'', text)
        # Remove \x1b\[1;33m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[1;33m', r'', text)
        # Remove \x1b\[1;34m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[1;34m', r'', text)
        # Remove \x1b\[1;35m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[1;35m', r'', text)
        # Remove \x1b\[1;36m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[1;36m', r'', text)
        # Remove \x1b\[1;37m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[1;37m', r'', text)

        # Remove \x1b\[4;30m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[4;30m', r'', text)
        # Remove \x1b\[4;31m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[4;31m', r'', text)
        # Remove \x1b\[4;32m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[4;32m', r'', text)
        # Remove \x1b\[4;33m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[4;33m', r'', text)
        # Remove \x1b\[4;34m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[4;34m', r'', text)
        # Remove \x1b\[4;35m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[4;35m', r'', text)
        # Remove \x1b\[4;36m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[4;36m', r'', text)
        # Remove \x1b\[4;37m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[4;37m', r'', text)

        # Remove \x1b\[40m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[40m', r'', text)
        # Remove \x1b\[41m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[41m', r'', text)
        # Remove \x1b\[42m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[42m', r'', text)
        # Remove \x1b\[43m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[43m', r'', text)
        # Remove \x1b\[44m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[44m', r'', text)
        # Remove \x1b\[45m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[45m', r'', text)
        # Remove \x1b\[46m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[46m', r'', text)
        # Remove \x1b\[47m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[47m', r'', text)

        # Remove \x1b\[0;90m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;90m', r'', text)
        # Remove \x1b\[0;91m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;91m', r'', text)
        # Remove \x1b\[0;92m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;92m', r'', text)
        # Remove \x1b\[0;93m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;93m', r'', text)
        # Remove \x1b\[0;94m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;94m', r'', text)
        # Remove \x1b\[0;95m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;95m', r'', text)
        # Remove \x1b\[0;96m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;96m', r'', text)
        # Remove \x1b\[0;97m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;97m', r'', text)

        # Remove \x1b\[1;90m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[1;90m', r'', text)
        # Remove \x1b\[1;91m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[1;91m', r'', text)
        # Remove \x1b\[1;92m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[1;92m', r'', text)
        # Remove \x1b\[1;93m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[1;93m', r'', text)
        # Remove \x1b\[1;94m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[1;94m', r'', text)
        # Remove \x1b\[1;95m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[1;95m', r'', text)
        # Remove \x1b\[1;96m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[1;96m', r'', text)
        # Remove \x1b\[1;97m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[1;97m', r'', text)

        # Remove \x1b\[0;100m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;100m', r'', text)
        # Remove \x1b\[0;101m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;101m', r'', text)
        # Remove \x1b\[0;102m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;102m', r'', text)
        # Remove \x1b\[0;103m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;103m', r'', text)
        # Remove \x1b\[0;104m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;104m', r'', text)
        # Remove \x1b\[0;105m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;105m', r'', text)
        # Remove \x1b\[0;106m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;106m', r'', text)
        # Remove \x1b\[0;107m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0;107m', r'', text)

        # Remove \x1b\[0m if it is not removed by the previous regex
        text = re.sub(r'\x1b\[0m', r'', text)

        # if \n is in text, replace it for <br>
        texts = text.split('\n')
        if len(texts) > 1:
            list_text[i] = texts[0]
            for j in range(1, len(texts)):
                list_text.insert(i+j, texts[j])
        else:
            list_text[i] = text
        
    return list_text

def post_format_html(file):
    ###
    # This function formats the html file
    # Input:
    #   file: html file
    # Output:
    #   file: html file
    ###
    # open file and read get the text
    with open(file, 'r') as f:
        text = f.read()
    # close file
    f.close()
    # Change <span class="n"> </span> for <span class="n"></span> in text
    text = re.sub(r'<span class="n"> </span>', r'<span class="n"></span>', text)
    # Remove blanck blocks
    text = re.sub(\
        r'		<div class="cell border-box-sizing text_cell rendered">\
				<div class="prompt input_prompt">\
					<div class="inner_cell">\
						<div class="text_cell_render border-box-sizing rendered_html">\
							<p style="margin-left: 0px;"></p>\
						</div>\
					</div>\
				</div>\
			</div>', r'', text)
    # Remove blanck outputs
    text = re.sub(\
        r'			<div class="output_wrapper">\
				<div class="output">\
					<div class="output_area">\
						<div class="prompt" style="margin-left: 20px;">Output:</div>\
						<div class="output_subarea output_stream output_stdout output_text">\
							<pre style="margin-left: 60px;"></pre>\
						</div>\
					</div>\
				</div>\
			</div>', r'', text)
    # Get the list of lines
    list_text = text.split('\n')
    list_text = [x for x in list_text if x != '']
    # Write the text in the file
    with open(file, 'w') as f:
        for text in list_text:
            f.write(text + '\n')
    # close file
    f.close()

def merge_unordered_list(file):
    ###
    # This function find unordered list in a html file
    # Input:
    #   file: html file
    # Output:
    #   unordered_list: string
    ###
    # open file and read get the text
    with open(file, 'r') as f:
        text = f.read()
    list_text = text.split('\n')    # split text by \n
    f.close()   # close file
    # Get all the lines that have <li>
    positions = []
    for i in range(len(list_text)): # find the positions of <li>
        li = re.findall(r'<li>', list_text[i])
        if len(li) > 0:
            positions.append(i)
    positions = np.array(positions) # convert positions to numpy array
    # If there is <li>
    if len(positions) > 0:  # if there is <li>
        # Calculate the median of the differences between positions. If the difference is greater than the median, it is an unordered list
        diffs = np.diff(positions)  # find the difference between positions with <li>
        median = np.median(diffs)   # find the median of the differences
        # Find the start and end of the unordered list
        start_unordered_list = []
        end_unordered_list = []
        start_unordered_list.append(positions[0])
        for i in range(len(diffs)): # find the start and end of the unordered list
            # If the difference is greater than the median, it is an unordered list
            if diffs[i] > median:
                start_unordered_list.append(positions[i+1])
                end_unordered_list.append(positions[i])
        end_unordered_list.append(positions[-1])
        # Now, we have the start and end of the all unordered list, merge the unordered list
        for i in range(len(start_unordered_list)):
            # Start and end of the unordered list
            start = start_unordered_list[i]
            end = end_unordered_list[i]
            # Find the position of the first <
            num_indentations = re.search(r'<', list_text[start])
            num_indentations = num_indentations.start()
            # Get the number of <ul> and </ul> into list_text[start]
            num_ul_level0 = len(re.findall(r'<ul>', list_text[start]))
            num_ul_end_level0 = len(re.findall(r'</ul>', list_text[start]))
            level = 0
            ul_start_position = re.search(r'<ul>', list_text[start])
            ul_start_position = ul_start_position.start()
            # Find the position of the first </ul>
            ul_end_position = re.search(r'</ul>', list_text[start])
            ul_end_position = ul_end_position.start()
            # Find the position of the first <li>
            li_start_position = re.search(r'<li>', list_text[start])
            li_start_position = li_start_position.start()
            # Find the position of the first </li>
            li_end_position = re.search(r'</li>', list_text[start])
            li_end_position = li_end_position.start()
            # Create the unordered list
            unordered_list = list_text[start][:ul_start_position]
            unordered_list += "\n" + "\t"*(num_indentations+1) + "<ul>"
            num_ul_old = num_ul_level0
            # num_ul_end_old = num_ul_end_level0
            for j, pos in enumerate(positions):
                if pos >= start and pos <= end:
                    # Get the number of <ul> and </ul> into list_text[start]
                    num_ul = len(re.findall(r'<ul>', list_text[pos]))
                    num_ul_end = len(re.findall(r'</ul>', list_text[pos]))
                    if num_ul > num_ul_old: 
                        level += 1
                        num_ul_old = num_ul
                    if num_ul < num_ul_old: 
                        level -= 1
                        num_ul_old = num_ul
                    li_start = re.search(r'<li>', list_text[pos])
                    li_start = li_start.start()
                    ul_end = re.search(r'</ul>', list_text[pos])
                    ul_end = ul_end.start()
                    unordered_list += "\n" + "\t"*(num_indentations+2) + ("<ul>"*level) + list_text[pos][li_start:ul_end] + ("</ul>"*level)
                    list_text[pos] = ""
            unordered_list += "\n" + "\t"*(num_indentations+1) + "</ul>"
            unordered_list += "\n" + "\t"*(num_indentations) + "</p>"
            list_text[start] = unordered_list
        # Write the text in the file
        with open(file, 'w') as f:
            for line in list_text:
                f.write(line + "\n")
        f.close()   # close file

def merge_ordered_list(file):
    ###
    # This function find unordered list in a html file
    # Input:
    #   file: html file
    # Output:
    #   unordered_list: string
    ###
    # open file and read get the text
    with open(file, 'r') as f:
        text = f.read()
    list_text = text.split('\n')    # split text by \n
    f.close()   # close file
    # Get all the lines that have <li>
    positions = []
    for i in range(len(list_text)): # find the positions of <oli>
        li = re.findall(r'<oli>', list_text[i])
        if len(li) > 0:
            positions.append(i)
    positions = np.array(positions) # convert positions to numpy array
    # If there is <oli>
    if len(positions) > 0:  # if there is <oli>
        # Calculate the median of the differences between positions. If the difference is greater than the median, it is an unordered list
        diffs = np.diff(positions)  # find the difference between positions with <oli>
        median = np.median(diffs)   # find the median of the differences
        # Find the start and end of the unordered list
        start_ordered_list = []
        end_ordered_list = []
        start_ordered_list.append(positions[0])
        for i in range(len(diffs)): # find the start and end of the unordered list
            # If the difference is greater than the median, it is an unordered list
            if diffs[i] > median:
                start_ordered_list.append(positions[i+1])
                end_ordered_list.append(positions[i])
        end_ordered_list.append(positions[-1])
        # Now, we have the start and end of the all ordered list, merge the ordered list
        for i in range(len(start_ordered_list)):
            # Start and end of the ordered list
            start = start_ordered_list[i]
            end = end_ordered_list[i]
            # Find the position of the first <
            num_indentations = re.search(r'<', list_text[start])
            num_indentations = num_indentations.start()
            # Get the number of <ol> and </ol> into list_text[start]
            num_ol_level0 = len(re.findall(r'<ol>', list_text[start]))
            num_ol_end_level0 = len(re.findall(r'</ol>', list_text[start]))
            level = 0
            ul_start_position = re.search(r'<ol>', list_text[start])
            ul_start_position = ul_start_position.start()
            # Find the position of the first </ol>
            ul_end_position = re.search(r'</ol>', list_text[start])
            ul_end_position = ul_end_position.start()
            # Find the position of the first <oli>
            li_start_position = re.search(r'<oli>', list_text[start])
            li_start_position = li_start_position.start()
            # Find the position of the first </oli>
            li_end_position = re.search(r'</oli>', list_text[start])
            li_end_position = li_end_position.start()
            # Create the unordered list
            ordered_list = []
            ordered_list.append(list_text[start][:ul_start_position])
            ordered_list.append("\n" + "\t"*(num_indentations+1) + "<ol>")
            num_ol_old = num_ol_level0
            # num_ol_end_old = num_ol_end_level0
            for j, pos in enumerate(positions):
                if pos >= start and pos <= end:
                    # Get the number of <ol> and </ol> into list_text[start]
                    num_ol = len(re.findall(r'<ol>', list_text[pos]))
                    # num_ol_end = len(re.findall(r'</ol>', list_text[pos]))
                    if num_ol > num_ol_old: 
                        level += 1
                        num_ol_old = num_ol
                        ordered_list[-1] = ordered_list[-1][:-5]
                        ordered_list.append("\n" + "\t"*(num_indentations+1+(level*2)) + "<ol>")
                    if num_ol < num_ol_old: 
                        level -= 1
                        num_ol_old = num_ol
                        ordered_list.append("\n" + "\t"*(num_indentations+1+((level+1)*2)) + "</ol>")
                    li_start = re.search(r'<oli>', list_text[pos])
                    li_start = li_start.start()
                    ol_end = re.search(r'</ol>', list_text[pos])
                    ol_end = ol_end.start()
                    ordered_list.append("\n" + "\t"*(num_indentations+2+(level*2)) + "<li>" + list_text[pos][li_start+5:ol_end-6] + "</li>")
                    list_text[pos] = ""
            ordered_list.append("\n" + "\t"*(num_indentations+1) + "</ol>")
            ordered_list.append("\n" + "\t"*(num_indentations) + "</p>")
            list_text[start] = "".join(ordered_list)
        # Write the text in the file
        with open(file, 'w') as f:
            for line in list_text:
                f.write(line + "\n")
        f.close()   # close file

def format_tables(file):
    ###
    # This function formats the tables in a html file
    # Input:
    #   file: html file
    # Output:
    #   file: html file
    ###
    with open(file, 'r') as f: # open file and read get the text
        text = f.read()
    list_text = text.split('\n')    # split text by \n
    f.close()   # close file
    positions = []
    for i in range(len(list_text)):
        if re.findall('<p style="margin-left: 0px;">\|.+\|</p>', list_text[i]):
            positions.append(i)
    positions = np.array(positions)
    if len(positions) > 0:
        diffs = np.diff(positions)
        median = np.median(diffs)
        start_table = []
        end_table = []
        start_table.append(positions[0])
        for i in range(len(diffs)):
            if diffs[i] > median:
                start_table.append(positions[i+1])
                end_table.append(positions[i])
        end_table.append(positions[-1])
        # Create table
        for i in range(len(start_table)):
            start = start_table[i]
            end = end_table[i]
            # Get index into positions when item is equal to start
            idx = int(np.where(positions == start)[0])
            start_content = positions[idx+2]
            # Find the position of the first <
            num_indentations = re.search(r'<', list_text[start])
            num_indentations = num_indentations.start()
            # Find the position of the first |
            pipe_start_position = re.search(r'\|', list_text[start])
            pipe_start_position = pipe_start_position.start()
            # Find the position of the first </p>
            p_end_position = re.search(r'</p>', list_text[start])
            p_end_position = p_end_position.start()
            # Get the table header
            table_header = list_text[start][pipe_start_position+1:p_end_position-1].split('|')
            table = "\t"*(num_indentations+0) + "<table>"
            table += "\n" + "\t"*(num_indentations+1) + "<tr>"
            for j in range(len(table_header)):
                table += "\n" + "\t"*(num_indentations+2) + "<th>" + table_header[j] + "</th>"  
            table += "\n" + "\t"*(num_indentations+1) + "</tr>"
            for j, pos in enumerate(positions):
                if pos >= start_content and pos <= end:
                    pipe_start = re.search(r'\|', list_text[pos])
                    pipe_start = pipe_start.start()
                    p_end = re.search(r'</p>', list_text[pos])
                    p_end = p_end.start()
                    table_row = list_text[pos][pipe_start+1:p_end-1].split('|')
                    table += "\n" + "\t"*(num_indentations+1) + "<tr>"
                    for k in range(len(table_row)):
                        table += "\n" + "\t"*(num_indentations+2) + "<td>" + table_row[k] + "</td>"
                    table += "\n" + "\t"*(num_indentations+1) + "</tr>"
                    list_text[pos] = ""
            list_text[positions[idx+1]] = ""
            table += "\n" + "\t"*(num_indentations+0) + "</table>"
            list_text[start] = table
            # Write the text in the file
            with open(file, 'w') as f:
                for line in list_text:
                    f.write(line + "\n")
            f.close()   # close file

