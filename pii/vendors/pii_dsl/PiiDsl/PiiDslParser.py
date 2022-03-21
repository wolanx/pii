# Generated from PiiDsl.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\23")
        buf.write("K\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\6\2\22\n\2\r\2\16\2\23\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3\33\n\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4&\n\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4\63\n")
        buf.write("\4\f\4\16\4\66\13\4\3\5\3\5\3\5\3\5\7\5<\n\5\f\5\16\5")
        buf.write("?\13\5\5\5A\n\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b\2")
        buf.write("\3\6\t\2\4\6\b\n\f\16\2\5\3\2\r\16\3\2\17\20\3\2\4\t\2")
        buf.write("N\2\21\3\2\2\2\4\32\3\2\2\2\6%\3\2\2\2\b\67\3\2\2\2\n")
        buf.write("D\3\2\2\2\fF\3\2\2\2\16H\3\2\2\2\20\22\5\4\3\2\21\20\3")
        buf.write("\2\2\2\22\23\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24\3")
        buf.write("\3\2\2\2\25\33\5\6\4\2\26\27\5\n\6\2\27\30\7\3\2\2\30")
        buf.write("\31\5\6\4\2\31\33\3\2\2\2\32\25\3\2\2\2\32\26\3\2\2\2")
        buf.write("\33\5\3\2\2\2\34\35\b\4\1\2\35\36\7\20\2\2\36&\5\6\4\t")
        buf.write('\37&\5\n\6\2 &\5\f\7\2!"\7\21\2\2"#\5\6\4\2#$\7\22\2')
        buf.write("\2$&\3\2\2\2%\34\3\2\2\2%\37\3\2\2\2% \3\2\2\2%!\3\2\2")
        buf.write("\2&\64\3\2\2\2'(\f\b\2\2()\t\2\2\2)\63\5\6\4\t*+\f\7")
        buf.write("\2\2+,\t\3\2\2,\63\5\6\4\b-.\f\6\2\2./\t\4\2\2/\63\5\6")
        buf.write("\4\7\60\61\f\n\2\2\61\63\5\b\5\2\62'\3\2\2\2\62*\3\2")
        buf.write("\2\2\62-\3\2\2\2\62\60\3\2\2\2\63\66\3\2\2\2\64\62\3\2")
        buf.write("\2\2\64\65\3\2\2\2\65\7\3\2\2\2\66\64\3\2\2\2\67@\7\21")
        buf.write("\2\28=\5\6\4\29:\7\f\2\2:<\5\6\4\2;9\3\2\2\2<?\3\2\2\2")
        buf.write("=;\3\2\2\2=>\3\2\2\2>A\3\2\2\2?=\3\2\2\2@8\3\2\2\2@A\3")
        buf.write("\2\2\2AB\3\2\2\2BC\7\22\2\2C\t\3\2\2\2DE\7\n\2\2E\13\3")
        buf.write("\2\2\2FG\5\16\b\2G\r\3\2\2\2HI\7\13\2\2I\17\3\2\2\2\t")
        buf.write("\23\32%\62\64=@")
        return buf.getvalue()


class PiiDslParser(Parser):

    grammarFileName = "PiiDsl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = [
        "<INVALID>",
        "'='",
        "'<'",
        "'>'",
        "'<='",
        "'>='",
        "'=='",
        "'!='",
        "<INVALID>",
        "<INVALID>",
        "','",
        "'*'",
        "'/'",
        "'+'",
        "'-'",
        "'('",
        "')'",
    ]

    symbolicNames = [
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "<INVALID>",
        "Id",
        "DecimalLiteral",
        "D",
        "MUL",
        "DIV",
        "ADD",
        "SUB",
        "LP",
        "RP",
        "WS",
    ]

    RULE_program = 0
    RULE_statement = 1
    RULE_expr = 2
    RULE_arguments = 3
    RULE_identifier = 4
    RULE_literal = 5
    RULE_numLit = 6

    ruleNames = ["program", "statement", "expr", "arguments", "identifier", "literal", "numLit"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    Id = 8
    DecimalLiteral = 9
    D = 10
    MUL = 11
    DIV = 12
    ADD = 13
    SUB = 14
    LP = 15
    RP = 16
    WS = 17

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class ProgramContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PiiDslParser.StatementContext)
            else:
                return self.getTypedRuleContext(PiiDslParser.StatementContext, i)

        def getRuleIndex(self):
            return PiiDslParser.RULE_program

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterProgram"):
                listener.enterProgram(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitProgram"):
                listener.exitProgram(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitProgram"):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)

    def program(self):

        localctx = PiiDslParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.statement()
                self.state = 17
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (
                    (
                        ((_la) & ~0x3F) == 0
                        and (
                            (1 << _la)
                            & (
                                (1 << PiiDslParser.Id)
                                | (1 << PiiDslParser.DecimalLiteral)
                                | (1 << PiiDslParser.SUB)
                                | (1 << PiiDslParser.LP)
                            )
                        )
                        != 0
                    )
                ):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return PiiDslParser.RULE_statement

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class LineExprContext(StatementContext):
        def __init__(self, parser, ctx: ParserRuleContext):  # actually a PiiDslParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PiiDslParser.ExprContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLineExpr"):
                listener.enterLineExpr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLineExpr"):
                listener.exitLineExpr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLineExpr"):
                return visitor.visitLineExpr(self)
            else:
                return visitor.visitChildren(self)

    class AssignExprContext(StatementContext):
        def __init__(self, parser, ctx: ParserRuleContext):  # actually a PiiDslParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(PiiDslParser.IdentifierContext, 0)

        def expr(self):
            return self.getTypedRuleContext(PiiDslParser.ExprContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAssignExpr"):
                listener.enterAssignExpr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAssignExpr"):
                listener.exitAssignExpr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitAssignExpr"):
                return visitor.visitAssignExpr(self)
            else:
                return visitor.visitChildren(self)

    def statement(self):

        localctx = PiiDslParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 24
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 1, self._ctx)
            if la_ == 1:
                localctx = PiiDslParser.LineExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                self.expr(0)
                pass

            elif la_ == 2:
                localctx = PiiDslParser.AssignExprContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 20
                self.identifier()
                self.state = 21
                self.match(PiiDslParser.T__0)
                self.state = 22
                self.expr(0)
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return PiiDslParser.RULE_expr

        def copyFrom(self, ctx: ParserRuleContext):
            super().copyFrom(ctx)

    class ArgExprContext(ExprContext):
        def __init__(self, parser, ctx: ParserRuleContext):  # actually a PiiDslParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(PiiDslParser.ExprContext, 0)

        def arguments(self):
            return self.getTypedRuleContext(PiiDslParser.ArgumentsContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterArgExpr"):
                listener.enterArgExpr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitArgExpr"):
                listener.exitArgExpr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitArgExpr"):
                return visitor.visitArgExpr(self)
            else:
                return visitor.visitChildren(self)

    class EqualityExprContext(ExprContext):
        def __init__(self, parser, ctx: ParserRuleContext):  # actually a PiiDslParser.ExprContext
            super().__init__(parser)
            self.left = None  # ExprContext
            self.op = None  # Token
            self.right = None  # ExprContext
            self.copyFrom(ctx)

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PiiDslParser.ExprContext)
            else:
                return self.getTypedRuleContext(PiiDslParser.ExprContext, i)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEqualityExpr"):
                listener.enterEqualityExpr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEqualityExpr"):
                listener.exitEqualityExpr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitEqualityExpr"):
                return visitor.visitEqualityExpr(self)
            else:
                return visitor.visitChildren(self)

    class IdExprContext(ExprContext):
        def __init__(self, parser, ctx: ParserRuleContext):  # actually a PiiDslParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def identifier(self):
            return self.getTypedRuleContext(PiiDslParser.IdentifierContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterIdExpr"):
                listener.enterIdExpr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitIdExpr"):
                listener.exitIdExpr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitIdExpr"):
                return visitor.visitIdExpr(self)
            else:
                return visitor.visitChildren(self)

    class LitExprContext(ExprContext):
        def __init__(self, parser, ctx: ParserRuleContext):  # actually a PiiDslParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def literal(self):
            return self.getTypedRuleContext(PiiDslParser.LiteralContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLitExpr"):
                listener.enterLitExpr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLitExpr"):
                listener.exitLitExpr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLitExpr"):
                return visitor.visitLitExpr(self)
            else:
                return visitor.visitChildren(self)

    class ParenExprContext(ExprContext):
        def __init__(self, parser, ctx: ParserRuleContext):  # actually a PiiDslParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def LP(self):
            return self.getToken(PiiDslParser.LP, 0)

        def expr(self):
            return self.getTypedRuleContext(PiiDslParser.ExprContext, 0)

        def RP(self):
            return self.getToken(PiiDslParser.RP, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterParenExpr"):
                listener.enterParenExpr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitParenExpr"):
                listener.exitParenExpr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitParenExpr"):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)

    class OpExprContext(ExprContext):
        def __init__(self, parser, ctx: ParserRuleContext):  # actually a PiiDslParser.ExprContext
            super().__init__(parser)
            self.left = None  # ExprContext
            self.op = None  # Token
            self.right = None  # ExprContext
            self.copyFrom(ctx)

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PiiDslParser.ExprContext)
            else:
                return self.getTypedRuleContext(PiiDslParser.ExprContext, i)

        def MUL(self):
            return self.getToken(PiiDslParser.MUL, 0)

        def DIV(self):
            return self.getToken(PiiDslParser.DIV, 0)

        def ADD(self):
            return self.getToken(PiiDslParser.ADD, 0)

        def SUB(self):
            return self.getToken(PiiDslParser.SUB, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterOpExpr"):
                listener.enterOpExpr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitOpExpr"):
                listener.exitOpExpr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitOpExpr"):
                return visitor.visitOpExpr(self)
            else:
                return visitor.visitChildren(self)

    class UnaryMinusExprContext(ExprContext):
        def __init__(self, parser, ctx: ParserRuleContext):  # actually a PiiDslParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(PiiDslParser.SUB, 0)

        def expr(self):
            return self.getTypedRuleContext(PiiDslParser.ExprContext, 0)

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterUnaryMinusExpr"):
                listener.enterUnaryMinusExpr(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitUnaryMinusExpr"):
                listener.exitUnaryMinusExpr(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitUnaryMinusExpr"):
                return visitor.visitUnaryMinusExpr(self)
            else:
                return visitor.visitChildren(self)

    def expr(self, _p: int = 0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PiiDslParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [PiiDslParser.SUB]:
                localctx = PiiDslParser.UnaryMinusExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 27
                self.match(PiiDslParser.SUB)
                self.state = 28
                self.expr(7)
                pass
            elif token in [PiiDslParser.Id]:
                localctx = PiiDslParser.IdExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 29
                self.identifier()
                pass
            elif token in [PiiDslParser.DecimalLiteral]:
                localctx = PiiDslParser.LitExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                self.literal()
                pass
            elif token in [PiiDslParser.LP]:
                localctx = PiiDslParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 31
                self.match(PiiDslParser.LP)
                self.state = 32
                self.expr(0)
                self.state = 33
                self.match(PiiDslParser.RP)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 50
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input, 4, self._ctx)
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 48
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input, 3, self._ctx)
                    if la_ == 1:
                        localctx = PiiDslParser.OpExprContext(
                            self, PiiDslParser.ExprContext(self, _parentctx, _parentState)
                        )
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 37
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 38
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not (_la == PiiDslParser.MUL or _la == PiiDslParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 39
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = PiiDslParser.OpExprContext(
                            self, PiiDslParser.ExprContext(self, _parentctx, _parentState)
                        )
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 40
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 41
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not (_la == PiiDslParser.ADD or _la == PiiDslParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 42
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 3:
                        localctx = PiiDslParser.EqualityExprContext(
                            self, PiiDslParser.ExprContext(self, _parentctx, _parentState)
                        )
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 43
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 44
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not (
                            (
                                ((_la) & ~0x3F) == 0
                                and (
                                    (1 << _la)
                                    & (
                                        (1 << PiiDslParser.T__1)
                                        | (1 << PiiDslParser.T__2)
                                        | (1 << PiiDslParser.T__3)
                                        | (1 << PiiDslParser.T__4)
                                        | (1 << PiiDslParser.T__5)
                                        | (1 << PiiDslParser.T__6)
                                    )
                                )
                                != 0
                            )
                        ):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 45
                        localctx.right = self.expr(5)
                        pass

                    elif la_ == 4:
                        localctx = PiiDslParser.ArgExprContext(
                            self, PiiDslParser.ExprContext(self, _parentctx, _parentState)
                        )
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 46
                        if not self.precpred(self._ctx, 8):
                            from antlr4.error.Errors import FailedPredicateException

                            raise FailedPredicateException(self, "self.precpred(self._ctx, 8)")
                        self.state = 47
                        self.arguments()
                        pass

                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 4, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class ArgumentsContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LP(self):
            return self.getToken(PiiDslParser.LP, 0)

        def RP(self):
            return self.getToken(PiiDslParser.RP, 0)

        def expr(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(PiiDslParser.ExprContext)
            else:
                return self.getTypedRuleContext(PiiDslParser.ExprContext, i)

        def D(self, i: int = None):
            if i is None:
                return self.getTokens(PiiDslParser.D)
            else:
                return self.getToken(PiiDslParser.D, i)

        def getRuleIndex(self):
            return PiiDslParser.RULE_arguments

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterArguments"):
                listener.enterArguments(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitArguments"):
                listener.exitArguments(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitArguments"):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)

    def arguments(self):

        localctx = PiiDslParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_arguments)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(PiiDslParser.LP)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((_la) & ~0x3F) == 0 and (
                (1 << _la)
                & (
                    (1 << PiiDslParser.Id)
                    | (1 << PiiDslParser.DecimalLiteral)
                    | (1 << PiiDslParser.SUB)
                    | (1 << PiiDslParser.LP)
                )
            ) != 0:
                self.state = 54
                self.expr(0)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la == PiiDslParser.D:
                    self.state = 55
                    self.match(PiiDslParser.D)
                    self.state = 56
                    self.expr(0)
                    self.state = 61
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

            self.state = 64
            self.match(PiiDslParser.RP)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IdentifierContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Id(self):
            return self.getToken(PiiDslParser.Id, 0)

        def getRuleIndex(self):
            return PiiDslParser.RULE_identifier

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterIdentifier"):
                listener.enterIdentifier(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitIdentifier"):
                listener.exitIdentifier(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitIdentifier"):
                return visitor.visitIdentifier(self)
            else:
                return visitor.visitChildren(self)

    def identifier(self):

        localctx = PiiDslParser.IdentifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_identifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(PiiDslParser.Id)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class LiteralContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def numLit(self):
            return self.getTypedRuleContext(PiiDslParser.NumLitContext, 0)

        def getRuleIndex(self):
            return PiiDslParser.RULE_literal

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLiteral"):
                listener.enterLiteral(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLiteral"):
                listener.exitLiteral(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLiteral"):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)

    def literal(self):

        localctx = PiiDslParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.numLit()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class NumLitContext(ParserRuleContext):
        __slots__ = "parser"

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DecimalLiteral(self):
            return self.getToken(PiiDslParser.DecimalLiteral, 0)

        def getRuleIndex(self):
            return PiiDslParser.RULE_numLit

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterNumLit"):
                listener.enterNumLit(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitNumLit"):
                listener.exitNumLit(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitNumLit"):
                return visitor.visitNumLit(self)
            else:
                return visitor.visitChildren(self)

    def numLit(self):

        localctx = PiiDslParser.NumLitContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_numLit)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(PiiDslParser.DecimalLiteral)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    def sempred(self, localctx: RuleContext, ruleIndex: int, predIndex: int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx: ExprContext, predIndex: int):
        if predIndex == 0:
            return self.precpred(self._ctx, 6)

        if predIndex == 1:
            return self.precpred(self._ctx, 5)

        if predIndex == 2:
            return self.precpred(self._ctx, 4)

        if predIndex == 3:
            return self.precpred(self._ctx, 8)
