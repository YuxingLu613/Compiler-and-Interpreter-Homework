import ply.lex as lex

reserved={
    'if':'IF',
    'int':'INT',
    'while':'WHILE',
    'if':'IF',
    'cout':'COUT',
    'endl':'ENDL',
}
tokens=[
    "NUMBER",
    "STRING",
    'EQUAL',
    "SEMICOLON",
    "LESSTHAN",
    "INPUT",
    "LBIGBRACE",
    "RBIGBRACE",
    "QUOTE",
    "ID",
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
]+list(reserved.values())

print(tokens)

t_EQUAL= r'='
t_SEMICOLON = r'\;'
t_LESSTHAN = r'\<'
t_INPUT = r'\<\<'
t_LBIGBRACE = r'\{'
t_RBIGBRACE = r'\}'
t_QUOTE= r'\"'
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_STRING(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    t.type = reserved.get(t.value,"ID")  
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data='''
int asd = 0;
int bc = 10;
while ( asd < bc)
{
	if(bc - asd < 2)
		cout<<"they are close."<<endl;
	asd = asd + 1;
}
'''

lexer.input(data)

while True:
	tok = lexer.token()
	if not tok: break # No more input
	print(tok)