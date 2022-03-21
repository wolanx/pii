# Generated from PiiDsl.g4 by ANTLR 4.9.2
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .PiiDslParser import PiiDslParser
else:
    from PiiDslParser import PiiDslParser

# This class defines a complete listener for a parse tree produced by PiiDslParser.
class PiiDslListener(ParseTreeListener):

    # Enter a parse tree produced by PiiDslParser#program.
    def enterProgram(self, ctx: PiiDslParser.ProgramContext):
        pass

    # Exit a parse tree produced by PiiDslParser#program.
    def exitProgram(self, ctx: PiiDslParser.ProgramContext):
        pass

    # Enter a parse tree produced by PiiDslParser#LineExpr.
    def enterLineExpr(self, ctx: PiiDslParser.LineExprContext):
        pass

    # Exit a parse tree produced by PiiDslParser#LineExpr.
    def exitLineExpr(self, ctx: PiiDslParser.LineExprContext):
        pass

    # Enter a parse tree produced by PiiDslParser#AssignExpr.
    def enterAssignExpr(self, ctx: PiiDslParser.AssignExprContext):
        pass

    # Exit a parse tree produced by PiiDslParser#AssignExpr.
    def exitAssignExpr(self, ctx: PiiDslParser.AssignExprContext):
        pass

    # Enter a parse tree produced by PiiDslParser#ArgExpr.
    def enterArgExpr(self, ctx: PiiDslParser.ArgExprContext):
        pass

    # Exit a parse tree produced by PiiDslParser#ArgExpr.
    def exitArgExpr(self, ctx: PiiDslParser.ArgExprContext):
        pass

    # Enter a parse tree produced by PiiDslParser#EqualityExpr.
    def enterEqualityExpr(self, ctx: PiiDslParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by PiiDslParser#EqualityExpr.
    def exitEqualityExpr(self, ctx: PiiDslParser.EqualityExprContext):
        pass

    # Enter a parse tree produced by PiiDslParser#IdExpr.
    def enterIdExpr(self, ctx: PiiDslParser.IdExprContext):
        pass

    # Exit a parse tree produced by PiiDslParser#IdExpr.
    def exitIdExpr(self, ctx: PiiDslParser.IdExprContext):
        pass

    # Enter a parse tree produced by PiiDslParser#LitExpr.
    def enterLitExpr(self, ctx: PiiDslParser.LitExprContext):
        pass

    # Exit a parse tree produced by PiiDslParser#LitExpr.
    def exitLitExpr(self, ctx: PiiDslParser.LitExprContext):
        pass

    # Enter a parse tree produced by PiiDslParser#ParenExpr.
    def enterParenExpr(self, ctx: PiiDslParser.ParenExprContext):
        pass

    # Exit a parse tree produced by PiiDslParser#ParenExpr.
    def exitParenExpr(self, ctx: PiiDslParser.ParenExprContext):
        pass

    # Enter a parse tree produced by PiiDslParser#OpExpr.
    def enterOpExpr(self, ctx: PiiDslParser.OpExprContext):
        pass

    # Exit a parse tree produced by PiiDslParser#OpExpr.
    def exitOpExpr(self, ctx: PiiDslParser.OpExprContext):
        pass

    # Enter a parse tree produced by PiiDslParser#UnaryMinusExpr.
    def enterUnaryMinusExpr(self, ctx: PiiDslParser.UnaryMinusExprContext):
        pass

    # Exit a parse tree produced by PiiDslParser#UnaryMinusExpr.
    def exitUnaryMinusExpr(self, ctx: PiiDslParser.UnaryMinusExprContext):
        pass

    # Enter a parse tree produced by PiiDslParser#arguments.
    def enterArguments(self, ctx: PiiDslParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by PiiDslParser#arguments.
    def exitArguments(self, ctx: PiiDslParser.ArgumentsContext):
        pass

    # Enter a parse tree produced by PiiDslParser#identifier.
    def enterIdentifier(self, ctx: PiiDslParser.IdentifierContext):
        pass

    # Exit a parse tree produced by PiiDslParser#identifier.
    def exitIdentifier(self, ctx: PiiDslParser.IdentifierContext):
        pass

    # Enter a parse tree produced by PiiDslParser#literal.
    def enterLiteral(self, ctx: PiiDslParser.LiteralContext):
        pass

    # Exit a parse tree produced by PiiDslParser#literal.
    def exitLiteral(self, ctx: PiiDslParser.LiteralContext):
        pass

    # Enter a parse tree produced by PiiDslParser#numLit.
    def enterNumLit(self, ctx: PiiDslParser.NumLitContext):
        pass

    # Exit a parse tree produced by PiiDslParser#numLit.
    def exitNumLit(self, ctx: PiiDslParser.NumLitContext):
        pass


del PiiDslParser
