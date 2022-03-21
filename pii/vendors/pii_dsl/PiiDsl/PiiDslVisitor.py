# Generated from PiiDsl.g4 by ANTLR 4.9.2
from antlr4 import *

if __name__ is not None and "." in __name__:
    from .PiiDslParser import PiiDslParser
else:
    from PiiDslParser import PiiDslParser

# This class defines a complete generic visitor for a parse tree produced by PiiDslParser.


class PiiDslVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by PiiDslParser#program.
    def visitProgram(self, ctx: PiiDslParser.ProgramContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PiiDslParser#LineExpr.
    def visitLineExpr(self, ctx: PiiDslParser.LineExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PiiDslParser#AssignExpr.
    def visitAssignExpr(self, ctx: PiiDslParser.AssignExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PiiDslParser#ArgExpr.
    def visitArgExpr(self, ctx: PiiDslParser.ArgExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PiiDslParser#EqualityExpr.
    def visitEqualityExpr(self, ctx: PiiDslParser.EqualityExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PiiDslParser#IdExpr.
    def visitIdExpr(self, ctx: PiiDslParser.IdExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PiiDslParser#LitExpr.
    def visitLitExpr(self, ctx: PiiDslParser.LitExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PiiDslParser#ParenExpr.
    def visitParenExpr(self, ctx: PiiDslParser.ParenExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PiiDslParser#OpExpr.
    def visitOpExpr(self, ctx: PiiDslParser.OpExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PiiDslParser#UnaryMinusExpr.
    def visitUnaryMinusExpr(self, ctx: PiiDslParser.UnaryMinusExprContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PiiDslParser#arguments.
    def visitArguments(self, ctx: PiiDslParser.ArgumentsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PiiDslParser#identifier.
    def visitIdentifier(self, ctx: PiiDslParser.IdentifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PiiDslParser#literal.
    def visitLiteral(self, ctx: PiiDslParser.LiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by PiiDslParser#numLit.
    def visitNumLit(self, ctx: PiiDslParser.NumLitContext):
        return self.visitChildren(ctx)


del PiiDslParser
