import re


def sub_elements(text):
    text = re.sub(r'\\begin{itemize}', r'<ul>', text)
    text = re.sub(r'\\end{itemize}',r'</ul>', text)
    text = re.sub(r'\\{(.*?)\\}', r'{\1}', text)
    text = re.sub(r'\\item \\texttt{(.+?)}(.+?)\n', r'<li>\1\2</li>', text)

    pattern = re.compile(r'\\emph{(.+?)}')
    text = re.sub(pattern, r'<i>\1</i>', text)

    text = re.sub(r'\\LaTeX{}', r'LaTeX', text)

    text = re.sub(r'\\texttt{(.+?)}', r'\1', text)
    text = re.sub(r'\\textbackslash ', r'\\', text)
    text = re.sub(r'\\textbackslash', r'\\', text)

    text = re.sub(r'\\begin{center}', r'<center>', text)
    text = re.sub(r'\\end{center}', r'</center>', text)
    text = re.sub(r'\\begin{tabular}{\| l \| l \|}', r'<br><table border="1" align="center">', text)
    text = re.sub(r'\\end{tabular}', r'</table>', text)
    tables = re.findall(r'<table border="1" align="center">(.+?)</table>', text, re.S)
    sub_tables = [sub_table(i) for i in tables]
    for i in range(len(tables)):
        text = text.replace(tables[i], sub_tables[i])
    return text

def sub_table(text):
    pattern = re.compile(r'(%.+?)\n')
    text = re.sub(pattern, r'', text)
    text = re.sub(r'hline', r'', text)
    text = re.sub(r'<i>(.+?)</i>', r'\1', text)
    lines = re.findall(r'\b(.+?) & (.+?) \\\\', text)
    tables = ''
    for i in lines:
        tables += '<tr>\n<td width=400>' + i[0] + '</td><td width=100>' + i[1] + '</td></tr>\n'
    return tables

def get_document(content):
    document_pattern = re.compile(r'\\begin{document}(.+?)\\end{document}',re.S)
    document = re.findall(document_pattern, content)
    return document[0]


def get_title(content):
    title_pattern = re.compile(r'\\title{(.+?)}', re.S)
    title = re.findall(title_pattern, content)
    return title[0]


def get_abstract(content):
    abstract_pattern = re.compile(r'\\begin{abstract}(.+?)\\end{abstract}',
                                  re.S)
    abstract = re.findall(abstract_pattern, content)
    return abstract[0]


def get_sections(content):
    section_pattern = re.compile(r'\\([sub]*section){(.+?)}', re.S)
    section = re.findall(section_pattern, content)
    return section


def get_section(section_list, content):
    section_html = ''
    for i in range(len(section_list)):
        if section_list[i][0] == "section":
            section_html += "<h2>%s</h2>" % section_list[i][1]
        elif section_list[i][0] == "subsection":
            section_html += "<h3>%s</h3>" % section_list[i][1]
        elif section_list[i][0] == "subsubsection":
            section_html += "<h4>%s</h4>\n" % section_list[i][1]
        if i == len(section_list) - 1:
            section_pattern = re.compile(
                r"\\%s(.+?)\\begin" %
                (section_list[-1][0] + "{" + section_list[-1][1] + "}"), re.S)
        else:
            section_pattern = re.compile(
                r"\\%s}(.+?)\\%s}" %
                (section_list[i][0] + "{" + section_list[i][1],
                 section_list[i + 1][0] + "{" + section_list[i + 1][1]), re.S)
        section_text = re.findall(section_pattern, content)[0]
        section_html += "<p>%s</p><br>\n" % section_text

    return section_html



def make_html(path):
    latex_content = open(path, 'r').read()
    latex_content = sub_elements(latex_content)
    html_content = ""

    document = get_document(latex_content)

    title = get_title(document)
    html_content += "<h1 align='center'>%s</h1>\n\n" % title

    abstract = get_abstract(document)
    html_content += "<p>\n<b>Abstract</b>\n<p>%s\n</p>\n</p>\n\n" % abstract

    sections = get_sections(document)
    html_content+= get_section(sections, document)
    return html_content