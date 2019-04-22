# Project Report
## Zachary Andrews, Devin Spitalny, Christian Lussier

Grammar:
```
Program ::== Decl+
Decl ::= BoneDecl | WoofDecl | VarDecl
WoofDecl ::= woof ID: Field* :
BoneDecl ::= bone ID- Formals: StmtBlock
Var ::= Type ID
VarDecl ::= Var\|
StmtBlock ::= : VarDecl* Stmt* :
Stmt ::= 〈Expr〉 \| | IfStmt | WhileStmt | ForStmt | BreakStmt | ReturnStmt | SpeakStmt | StmtBlock
Field ::= VarDecl | FuncDecl
Formals ::= Variable+, | ε
SpeakStmt ::= Speak- Expr+, \|
IfStmt ::= if ( Expr ) Stmt 〈else Stmt〉
ReturnStmt ::= return〈Expr〉\|
BreakStmt ::= break\|
DigStmt ::= dig- Type ID Expr|Expr|Expr: Stmt
Expr ::= LValue = Expr | Constant | LValue | this | ( Expr ) | Expr+Expr | Expr-Expr | Expr*Expr | Expr/Expr | Expr%Expr | - Expr | Expr < Expr | Expr <= Expr | Expr > Expr | Expr >= Expr | Expr == Expr | Expr != Expr | Expr && Expr | Expr || Expr | ! Expr | FetchInteger ( ) | FetchLine ( )
LValue ::= indent (Actuals) | Expr . indent (Actuals)
Actuals ::= Expr+, | ε
Type ::= int | double | bool | string
Constant ::= intConstant | doubleConstant | boolConstant | stringConstant | null
```
