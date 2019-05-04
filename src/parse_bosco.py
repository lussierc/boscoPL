# reserved keywords
reserved = {
    'treat' : 'TREAT', 'double' : 'DOUBLE', 'goodboi' : 'GOODBOI', 'noise' : 'NOISE',
    'woof' : 'WOOF', 'null' : 'NULL', 'dig' : 'DIG', 'if' : 'IF', 'else' : 'ELSE',
    'return' : 'RETURN', 'break' : 'BREAK', 'speak' : 'SPEAK', 'bone' : 'BONE',
    'FetchTreat' : 'FETCHTREAT', 'FetchNoise' : 'FETCHNOISE'
}

# tokens that will be used for operations and organization of code
tokens = [
    'ID','PLUS', 'MINUS', 'DIV', 'MULT', 'REM', 'AND', 'OR',
    'ASSIGN', 'GREATER', 'LESS', 'GREATEREQ', 'LESSEQ', 'EQUALS', 'NEQUALS',
    'NOT', 'COLON', 'COMMA', 'BAR', 'LPAREN', 'RPAREN'
]

tokens += list(reserved.values())

# define the values that can be in a double
def t_DOUBLE(t):
    r'[0-9]*\.[0-9]+'
    return t

# define the values that can be in an int
def t_TREAT(t):
    r'[0-9]+'
    return t

# defines the values that can make up a string
def t_NOISE(t):
    r'\"(.*?)\"'
    return t

def t_GOODBOI(t):
    r'true\b|false\b'
    return t

# define the values that can be part of an identifier
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]{0,32}'
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
t_LPAREN = r'\)'
t_RPAREN = r'\('

# characters that are not looked at when scanning
t_ignore = " \t"

# defines what a single and multi-line comment should look like
def t_COMMENT(t):
    r'\?\? (.*)'
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

"""Parser stuff"""
import ply.yacc as yacc

precedence = (
     ('left', 'PLUS', 'MINUS'),
     ('left', 'MULT', 'DIV'),
 )

def p_Program(p):
    'Program : Decl'

def p_Decl(p):
    '''Decl : ClassDecl
            | FuncDecl
            | VarDecl
            | R_Decl'''

def p_R_Decl(p):
    '''R_Decl : Decl R_Decl
              | Empty'''

def p_ClassDecl(p):
    '''ClassDecl : WOOF ID COLON Field COLON'''

def p_FuncDecl(p):
    '''FuncDecl : BONE ID MINUS Formals MINUS StmtBlock'''

def p_VarDecl(p):
    '''VarDecl : Var BAR'''

def p_R_VarDecl(p):
    '''R_VarDecl : VarDecl R_VarDecl
                 | Empty'''

def p_Var(p):
    '''Var : Type ID
           | Type ID ASSIGN Expr'''

def p_R_Var(p):
    '''R_Var : COMMA Var R_Var
             | Empty'''

def p_Type(p):
    '''Type : TREAT
            | DOUBLE
            | GOODBOI
            | NOISE'''

def p_Formals(p):
    '''Formals : Var
               | Var R_Var
               | Empty'''

def p_Field(p):
    '''Field : VarDecl
             | FuncDecl
             | R_Field'''

def p_R_Field(p):
    '''R_Field : Field R_Field
               | Empty'''

def p_StmtBlock(p):
    '''StmtBlock : RPAREN R_VarDecl R_Stmt LPAREN'''

def p_Stmt(p):
    '''Stmt : R_Expr BAR
            | IfStmt
            | LoopStmt
            | BreakStmt
            | ReturnStmt
            | PrintStmt
            | StmtBlock'''

def p_R_Stmt(p):
    '''R_Stmt : Stmt R_Stmt
              | Empty'''

def p_IfStmt(p):
    '''IfStmt : IF MINUS Expr StmtBlock
              | IF MINUS Expr Stmt ELSE Stmt'''

def p_LoopStmt(p):
    'LoopStmt : DIG Expr BAR Expr BAR Expr StmtBlock'

def p_ReturnStmt(p):
    '''ReturnStmt : RETURN R_Expr BAR'''

def p_BreakStmt(p):
    'BreakStmt : BREAK BAR'

def p_PrintStmt(p):
    '''PrintStmt : SPEAK MINUS R_Expr BAR'''

def p_Expr_Math(p):
    '''Expr : Expr PLUS Expr
            | Expr MINUS Expr
            | Expr MULT Expr
            | Expr DIV Expr
            | Expr REM Expr
            | MINUS Expr'''

def p_Expr_Logic(p):
    '''Expr : Expr LESS Expr
            | Expr LESSEQ Expr
            | Expr GREATER Expr
            | Expr GREATEREQ Expr
            | Expr EQUALS Expr
            | Expr NEQUALS Expr
            | Expr AND Expr
            | Expr OR Expr
            | NOT Expr'''

def p_Expr(p):
    '''Expr : LValue ASSIGN Expr
            | RPAREN Expr LPAREN
            | FETCHTREAT RPAREN LPAREN
            | FETCHNOISE RPAREN LPAREN
            | Constant
            | LValue'''


def p_R_Expr(p):
    '''R_Expr : Expr R_Expr
              | COMMA Expr R_Expr
              | Empty'''

def p_LValue(p):
    '''LValue : ID'''

def p_Constant(p):
    '''Constant : TREAT
                | DOUBLE
                | GOODBOI
                | NOISE
                | NULL'''

def p_Empty(p):
    'Empty :'
    pass

def p_error(p):
    print("Syntax error in input")

# checks if there is a file path supplied as an argument, if not asks for one on run
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
# Give the lexer some input
lexer.input(data)
# tokenizes and prints out each token
while True:
 tok = lexer.token()
 if not tok:
     break
 print(tok)

try:
    debug=int(sys.argv[2])
except:
    debug=1
print("=======Parsing=======")
parser = yacc.yacc()

parser.parse(data,debug=debug)
print("===Finished Parsing===")
