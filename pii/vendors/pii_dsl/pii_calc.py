from typing import Dict

from antlr4 import InputStream, CommonTokenStream

from pii.log import log
from pii.vendors.pii_dsl.PiiDsl.PiiDslLexer import PiiDslLexer
from pii.vendors.pii_dsl.PiiDsl.PiiDslParser import PiiDslParser
from pii.vendors.pii_dsl.PiiDsl.PiiDslVisitor import PiiDslVisitor
from pii.vendors.pii_dsl.functions import funcs


class MyPiiDslVisitor(PiiDslVisitor):
    def __init__(self, ctx: dict):
        self.model: Dict = ctx

    def visitProgram(self, ctx: PiiDslParser.ProgramContext):
        return super().visitProgram(ctx)

    def visitLineExpr(self, ctx: PiiDslParser.LineExprContext):
        return super().visitLineExpr(ctx)

    def visitAssignExpr(self, ctx: PiiDslParser.AssignExprContext):
        k = self.visit(ctx.identifier())
        v = self.visit(ctx.expr())
        self.model.__setitem__(k, v)

    def visitArgExpr(self, ctx: PiiDslParser.ArgExprContext):
        fName = ctx.expr().getText()
        args = ctx.arguments().expr()
        return self.doFunc(fName, args)

    def visitEqualityExpr(self, ctx: PiiDslParser.EqualityExprContext):
        a = self.visit(ctx.left)
        b = self.visit(ctx.right)

        op = ctx.op.text
        if op == "<":
            return a < b
        elif op == ">":
            return a > b
        elif op == "<=":
            return a <= b
        elif op == ">=":
            return a >= b
        elif op == "==":
            return a == b
        elif op == "!=":
            return a != b

    def visitIdExpr(self, ctx: PiiDslParser.IdExprContext):
        k = ctx.getText()
        return self.model.get(k)

    def visitLitExpr(self, ctx: PiiDslParser.LitExprContext):
        n = ctx.getText()
        return int(n)

    def visitParenExpr(self, ctx: PiiDslParser.ParenExprContext):
        return self.visit(ctx.expr())

    def visitUnaryMinusExpr(self, ctx: PiiDslParser.UnaryMinusExprContext):
        return -1 * self.visit(ctx.expr())

    def visitArguments(self, ctx: PiiDslParser.ArgumentsContext):
        return super().visitArguments(ctx)

    def visitIdentifier(self, ctx: PiiDslParser.IdentifierContext):
        return ctx.getText()

    def visitLiteral(self, ctx: PiiDslParser.LiteralContext):
        return super().visitLiteral(ctx)

    def visitNumLit(self, ctx: PiiDslParser.NumLitContext):
        return float(ctx.getText())

    def visitOpExpr(self, ctx: PiiDslParser.OpExprContext):
        a = self.visit(ctx.left)
        b = self.visit(ctx.right)

        op = ctx.op.text
        if op == "+":
            return a + b
        elif op == "-":
            return a - b
        elif op == "*":
            return a * b
        elif op == "/":
            if b == 0:
                return 0
            return a / b

    def doFunc(self, fName: str, args: list):
        try:
            fn = funcs.get(fName)
            if fn is None:
                raise Exception(f"no fn：{fName}")
            argsKey = [one.getText() for one in args]
            argsVal = [self.visit(one) for one in args]
            ret = fn(self.model, args, argsKey, argsVal)
            return ret
        except Exception as e:
            log.error(e)
            return None


class PiiDsl:
    def __init__(self, line: str):
        input_stream = InputStream(line)

        # lexing
        lexer = PiiDslLexer(input_stream)
        stream = CommonTokenStream(lexer)

        # parsing
        parser = PiiDslParser(stream)
        self.tree = parser.program()

    def out(self, ctx: dict = None):
        if ctx is None:
            ctx = {}
        visitor = MyPiiDslVisitor(ctx)
        ret = visitor.visit(self.tree)
        return ret
