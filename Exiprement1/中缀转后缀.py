expression = input()  
explst = list(expression)  
  
order = {}  
order["*"] = 2  
order["/"] = 2  
order["+"] = 1  
order["-"] = 1  
sym = []  
newexp = []  
  
for token in explst:  
    if token in "0123456789":  
        newexp.append(token)  
    else:  
        if sym == []:  
            sym.append(token)  
        else:  
            while sym != [] and order[token] <= order[sym[-1]]:  
                newexp.append(sym.pop())  
            sym.append(token)  
while sym != []:  
    newexp.append(sym.pop())  
print " ".join(newexp)  