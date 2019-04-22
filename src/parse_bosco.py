# reserved keywords
reserved = {
    'int' : 'INT', 'double' : 'DOUBLE', 'bool' : 'BOOL', 'string' : 'STRING',
    'woof' : 'WOOF', 'null' : 'NULL', 'dig' : 'DIG', 'if' : 'IF', 'else' : 'ELSE',
    'return' : 'RETURN', 'break' : 'BREAK', 'speak' : 'SPEAK', 'bone' : 'BONE',
    'FetchInt' : 'FETCHINT', 'FetchLine' : 'FETCHLINE'
}

# tokens that will be used for operations and organization of code
tokens = [
    'ID','PLUS', 'MINUS','DIV','MULT', 'REM', 'AND','OR',
    'ASSIGN', 'GREATER','LESS', 'GREATEREQ','LESSEQ','EQUALS', 'NEQUALS',
    'NOT', 'COLON', 'COMMA', 'BAR', 'LPAREN', 'RPAREN'
]

tokens += list(reserved.values())

# define the values that can be in a double
def t_DOUBLE(t):
    r'[0-9]*\.[0-9]+'
    return t

# define the values that can be in an int
def t_INT(t):
    r'[0-9]+'
    return t

# defines the values that can make up a string
def t_STRING(t):
    r'\"(.*?)\"'
    return t

def t_BOOL(t):
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

def p_Program(t):
    '''Program : Decl'''

def p_Decl(t):
    '''Decl : WoofDecl
            | BoneDecl
            | VarDecl
            | R_Decl'''

def p_R_Decl(t):
    '''R_Decl : Decl R_Decl
              | Empty'''

def p_WoofDecl(t):
    '''WoofDecl : WOOF ID COLON Field COLON'''

def p_BoneDecl(t):
    '''BoneDecl : BONE ID MINUS Field StmtBlock'''

def p_Var(t):
    '''Var : Type ID'''

def p_VarDecl(t):
    '''VarDecl : Var BAR
               | R_VarDecl'''

def p_R_VarDecl(t):
    '''R_VarDecl : VarDecl R_VarDecl
                 | Empty'''

def p_StmtBlock(t):
    '''StmtBlock : COLON R_VarDecl R_Stmt COLON'''
    # t[0] = t[1]

def p_Stmt(t):
    '''Stmt : R_Expr BAR
            | IfStmt
            | DigStmt
            | BreakStmt
            | ReturnStmt
            | SpeakStmt
            | StmtBlock'''

def p_R_Stmt(p):
    '''R_Stmt : Stmt R_Stmt
              | Empty'''

def p_Field(t):
    '''Field : BoneDecl
             | VarDecl
             | R_Field'''

def p_R_Field(t):
    '''R_Field : Field R_Field
               | Empty'''

def p_SpeakStmt(p):
    '''SpeakStmt : SPEAK RPAREN R_Expr LPAREN BAR'''

def p_IfStmt(p):
    '''IfStmt : IF MINUS Expr COLON Stmt
              | IF MINUS Expr COLON Stmt ELSE COLON Stmt'''

def p_ReturnStmt(p):
    '''ReturnStmt : RETURN R_Expr BAR'''

def p_BreakStmt(p):
    '''BreakStmt : BREAK BAR'''

def p_DigStmt(p):
    '''DigStmt : DIG MINUS Type ID Expr BAR Expr BAR Expr COLON Stmt'''

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
            | FETCHINT MINUS BAR
            | FETCHLINE MINUS BAR
            | Constant'''

def p_R_Expr(t):
    '''R_Expr : Expr R_Expr
              | COMMA Expr R_Expr
              | Empty'''

def p_LValue(t):
    '''LValue : ID'''

def p_Constant(t):
    '''Constant : INT
                | DOUBLE
                | BOOL
                | STRING
                | NULL'''

def p_Type(t):
    '''Type : INT
            | DOUBLE
            | BOOL
            | STRING
            | ID'''

def p_Empty(t):
    '''Empty :'''
    pass

def p_error(t):
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

parser = yacc.yacc()
parser.parse(data)
