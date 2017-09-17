import ply.yacc as yacc
from calc_lexico import tokens
import calc_lexico
import sys

def p_program(p):
	'program : declaration_list'
	pass

def p_declaration_list_1(p):
	'declaration_list : declaration_list  declaration'
	pass

def p_declaration_list_2(p):
	'declaration_list : declaration'
	pass

def p_declaration(p):
    'declaration : expression AMPERSAND'
    pass

def p_expression_plus(p):
    'expression : expression PLUS term'
    #p[0] = p[1] + p[3]
    pass

def p_expression_minus(p):
    'expression : expression MINUS term'
    #p[0] = p[1] - p[3]
    pass

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]
    pass

def p_term(p):
    'term :term MULTIPLY factor'
    #p[0] = p[1] * p[3]
    pass

def p_term_div(p):
    'term : term DIVIDE factor'
    #p[0] = p[1] / p[3]
    pass

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]
    pass

def p_factor_num(p):
    'factor : NUM'
    p[0] = p[1]
    pass

def p_factor_id(p):
    'factor : ID'
    p[0] = p[1]
    pass

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    #p[0] = p[2]
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    pass

# Build the parser
parser = yacc.yacc()

if __name__ == '__main__':

	if (len(sys.argv) > 1):
		fin = sys.argv[1]
	else:
		fin = 'prueba.cal'

	f = open(fin, 'r')
	data = f.read()
	#print (data)
	parser.parse(data, tracking=True)
	print("Tu parser reconocio correctamente todo")