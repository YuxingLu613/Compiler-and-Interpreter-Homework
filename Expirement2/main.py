from Latex2Html import make_html
from Html2Pdf import html2pdf

html_content=make_html('Expirement2\\example.tex')
print(html_content)
html2pdf(html_content,"Expirement2\\result.pdf")