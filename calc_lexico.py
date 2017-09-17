import ply.lex as lex
import sys

tokens = ['PLUS','MINUS','DIVIDE','MULTIPLY','AMPERSAND','LPAREN','RPAREN','NUM','ID'] 

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'    # Check for reserved words
    return t

t_PLUS      = r'\+'
t_MINUS     = r'\-'
t_DIVIDE    = r'/'
t_MULTIPLY  = r'\*'
t_AMPERSAND = r'\&'
t_LPAREN    = r'\('
t_RPAREN    = r'\)'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def test(data, lexer):
    lexer.input(data)
    while True:
        tok = lexer.token()
        print (tok)
        if not tok:
            break

def t_NUM(t):
    r'\d+'
    t.value = int(t.value) 
    return t

t_ignore  = ' \t'

def t_error(t):
    print ("Lexical error: " + str(t.value[0]))
    t.lexer.skip(1)

lexer=lex.lex()

if __name__=='__main__':
    if (len(sys.argv) > 1):
        fin = sys.argv[1]
    else:
        fin='prueba.cal'
    f= open(fin,'r')
    data=f.read()
    print(data)
    #lexer.input(data)
    test(data, lexer)
    #input()
