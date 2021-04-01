import re

content=open("content.html","r",encoding='utf-8').read()
title=re.findall(r"<title>.*</title>", content)[0].lstrip("<title>").rstrip("</title>")
texts=re.findall(r"<p>.*</p>",content)
print(title)
print(texts)