import pygments
from pygments import lexers
from pygments import formatters
# from pygments import highlight
# from pygments.lexers import PythonLexer
# from pygments.formatters import HtmlFormatter

import re

lexer = lexers.PythonLexer()
formatter = formatters.HtmlFormatter()

def highlight_code(code):
    html_code = pygments.highlight(code, lexer, formatter)
    # Remove the <div class="highlight"> tag and </div> tag
    html_code = html_code.replace('<div class="highlight">', '')
    html_code = html_code.replace('</div>', '')
    # Remove the <pre> tag and </pre> tag
    html_code = html_code.replace('<pre>', '')
    html_code = html_code.replace('</pre>', '')
    # Remove the <span></span> tag
    html_code = html_code.replace('<span></span>', '')
    # Replace <span class="kn"> by <span style="color: #833aa0;">
    html_code = html_code.replace('<span class="kn">', '<span style="color: #833aa0;">')
    # Replace <span class="k"> by <span style="color: #a04cc1;">
    html_code = html_code.replace('<span class="k">', '<span style="color: #a04cc1;">')
    # Replace <span class="nn"> by <span style="color: #4fcd7d;">
    html_code = html_code.replace('<span class="nn">', '<span style="color: #4fcd7d;">')
    # Replace <span class="nb"> by <span style="color: #dfd84a;">
    html_code = html_code.replace('<span class="nb">', '<span style="color: #dfd84a;">')
    # Replace <span class="p"> by <span style="color: #e3e11d;">
    html_code = html_code.replace('<span class="p">', '<span style="color: #e3e11d;">')
    # Replace <span class="n"> by <span style="color: #6b97e8;">
    html_code = html_code.replace('<span class="n">', '<span style="color: #6b97e8;">')
    # Replace <span class="o"> by <span>
    html_code = html_code.replace('<span class="o">', '<span>')
    # Replace <span class="mi"> by <span style="color: #7e7a38;">
    html_code = html_code.replace('<span class="mi">', '<span style="color: #7e7a38;">')
    # Replace <span class="s2"> by <span style="color: #7e7a34;">
    html_code = html_code.replace('<span class="s2">', '<span style="color: #7e7a34;">')
    # Replace <span class="mf"> by <span style="color: #a09e19;">
    html_code = html_code.replace('<span class="mf">', '<span style="color: #a09e19;">')
    # Replace <span class="sa"> by <span style="color: #1b1477;">
    html_code = html_code.replace('<span class="sa">', '<span style="color: #1b1477;">')
    # Replace <span class="se"> by <span style="color: #a6a831;">
    html_code = html_code.replace('<span class="se">', '<span style="color: #a6a831;">')
    # Replace <span class="si"> by <span style="color: #3b75c2;">
    html_code = html_code.replace('<span class="si">', '<span style="color: #3b75c2;">')
    # Replace <span class="kc"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="kc">', '<span style="color: #7f6e38;">')
    # Replace <span class="s1"> by <span style="color: #8d783e;">
    html_code = html_code.replace('<span class="s1">', '<span style="color: #8d783e;">')
    # Replace <span class="ow"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="ow">', '<span style="color: #7f6e38;">')
    # Replace <span class="c1"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="c1">', '<span style="color: #7f6e38;">')
    # Replace <span class="cm"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="cm">', '<span style="color: #7f6e38;">')
    # Replace <span class="s"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="s">', '<span style="color: #7f6e38;">')
    # Replace <span class="c"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="c">', '<span style="color: #7f6e38;">')
    # Replace <span class="err"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="err">', '<span style="color: #7f6e38;">')
    # Replace <span class="gd"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="gd">', '<span style="color: #7f6e38;">')
    # Replace <span class="ge"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="ge">', '<span style="color: #7f6e38;">')
    # Replace <span class="gp"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="gp">', '<span style="color: #7f6e38;">')
    # Replace <span class="gs"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="gs">', '<span style="color: #7f6e38;">')
    # Replace <span class="gu"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="gu">', '<span style="color: #7f6e38;">')
    # Replace <span class="gt"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="gt">', '<span style="color: #7f6e38;">')
    # Replace <span class="kc"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="kc">', '<span style="color: #7f6e38;">')
    # Replace <span class="kd"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="kd">', '<span style="color: #7f6e38;">')
    # Replace <span class="kn"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="kn">', '<span style="color: #7f6e38;">')
    # Replace <span class="kp"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="kp">', '<span style="color: #7f6e38;">')
    # Replace <span class="kr"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="kr">', '<span style="color: #7f6e38;">')
    # Replace <span class="kt"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="kt">', '<span style="color: #7f6e38;">')
    # Replace <span class="m"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="m">', '<span style="color: #7f6e38;">')
    # Replace <span class="nf"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="nf">', '<span style="color: #7f6e38;">')
    # Replace <span class="vm"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="vm">', '<span style="color: #7f6e38;">')
    # Replace <span class="sd"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="sd">', '<span style="color: #7f6e38;">')
    # Replace <span class="nd"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="nd">', '<span style="color: #7f6e38;">')
    # Replace <span class="nl"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="nl">', '<span style="color: #7f6e38;">')
    # Replace <span class="nn"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="nn">', '<span style="color: #7f6e38;">')
    # Replace <span class="nt"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="nt">', '<span style="color: #7f6e38;">')
    # Replace <span class="nv"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="nv">', '<span style="color: #7f6e38;">')
    # Replace <span class="ow"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="ow">', '<span style="color: #7f6e38;">')
    # Replace <span class="w"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="w">', '<span style="color: #7f6e38;">')
    # Replace <span class="nc"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="nc">', '<span style="color: #7f6e38;">')
    # Replace <span class="fm"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="fm">', '<span style="color: #7f6e38;">')
    # Replace <span class="bp"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="bp">', '<span style="color: #7f6e38;">')
    # Replace <span class="ne"> by <span style="color: #7f6e38;">
    html_code = html_code.replace('<span class="ne">', '<span style="color: #7f6e38;">')
    # If <span class is in the code show one warning
    if '<span class' in html_code:
        # Locate the position of the first <span class
        pos = html_code.find('<span class')
        raise SystemError(f'<span class="..." is still in the code: {html_code[pos:pos+100]}')
    return html_code