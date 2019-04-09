# reserved keywords
reserved = {
    'woof' : 'WOOF',  'bone' : 'BONE', 'speak' : 'SPEAK', 'dig' : 'DIG',
    'int' : 'INT', 'double' : 'DOUBLE', 'bool' : 'BOOL', 'string' : 'STRING',
    'fetch' : 'FETCH', 'fetchInt' : 'FETCHINT'
}

# tokens that will be used for operations and organization of code
tokens = [
    'ID','PLUS', 'MINUS','DIV','MULT', 'REM', 'AND','OR',
    'ASSIGN', 'GREATER','LESS', 'GREATEREQ','LESSEQ','EQUALS', 'NEQUALS',
    'NOT', 'COLON', 'COMMA', 'BAR'
]

tokens += list(reserved.values())

# define the values that can be in an int
# TODO: get hexadecimal format working
def t_INT(t):
    r'((0X){1}([0-9A-F]|[0-9a-f])+|\d+)'
    return t

# define the values that can be in a double
def t_DOUBLE(t):
    r'[-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)'
    return t

# defines the values that can make up a string
def t_STRING(t):
    r'\"(.*?)\"'
    return t

# def t_BOOL(t):
#     r'(' + TRUE + r'|' +FALSE + r')'
#     return t

# define the values that can be part of an identifier
# TODO: put cap on number of characters (31)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]{0,31}'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

# assigns values to each token that is not a reserved word
t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_DIV = r'/'
t_MULT = r'\*'
t_REM = r'%'
t_EQUALS = r'=='
t_NEQUALS = r'!='
t_NOT = r'!'
t_GREATER = r'\>'
t_LESS = r'\<'
t_GREATEREQ = r'/>='
t_LESSEQ = r'\<='
t_AND = r'&&'
t_OR = r'\|\|'
t_COLON = r'\:'
t_COMMA = r','
t_BAR = r'\|'

# characters that are not looked at when scanning
t_ignore = " \t"

# defines what a single and multi-line comment should look like
def t_COMMENT(t):
    r'\?\? (.*?)'
    t.lexer.lineno += t.value.count("\n")
    pass

# counts lines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

# if there is an error
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# checks if there is a file path supplied as an argument, if not asks for one on run
try:
    import sys
    path = sys.argv[1]
except:
    print("No file supplied as an argument, please give one now")
    path = input(">> ")


# gets each line in the inputed # checks if there is a file path supplied as an argument, if not asks for one on run
try:
    import sys
    path = sys.argv[1]
except:
    print("No file supplied as an argument, please give one now")
    path = input(">> ")


# gets each line in the inputed file and passes it to the parser
data = ""
try:
    with open(path) as f:
        data = f.read()
except:
    print("File not found")
import ply.lex as lex
lexer = lex.lex()
# Give the lexer some input file and passes it to the parser
lexer.input(data)
data = ""
try:
    with open(path) as f:
        data = f.read()
except:
    print("File not found")
import ply.lex as lex
lexer = lex.lex()
# Give the lexer some input
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
