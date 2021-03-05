# Generated from C:\ddey_documents\GitHub_Python\antler_data_parsing\DataParser\parser\Parser.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\5")
        buf.write("\26\4\2\t\2\4\3\t\3\4\4\t\4\3\2\7\2\n\n\2\f\2\16\2\r\13")
        buf.write("\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\2\2\5\2\4\6\2\2\2\23")
        buf.write("\2\13\3\2\2\2\4\20\3\2\2\2\6\23\3\2\2\2\b\n\5\4\3\2\t")
        buf.write("\b\3\2\2\2\n\r\3\2\2\2\13\t\3\2\2\2\13\f\3\2\2\2\f\16")
        buf.write("\3\2\2\2\r\13\3\2\2\2\16\17\7\2\2\3\17\3\3\2\2\2\20\21")
        buf.write("\7\3\2\2\21\22\7\4\2\2\22\5\3\2\2\2\23\24\7\5\2\2\24\7")
        buf.write("\3\2\2\2\3\13")
        return buf.getvalue()


class Parser ( Parser ):

    grammarFileName = "Parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "PCIEBAR_VALUE", "PCIEBAR_VALUE_MODE_FINAL_VALUE", 
                      "BIOS_ID" ]

    RULE_seriallog = 0
    RULE_pciexbar = 1
    RULE_biosid = 2

    ruleNames =  [ "seriallog", "pciexbar", "biosid" ]

    EOF = Token.EOF
    PCIEBAR_VALUE=1
    PCIEBAR_VALUE_MODE_FINAL_VALUE=2
    BIOS_ID=3

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SeriallogContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(Parser.EOF, 0)

        def pciexbar(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(Parser.PciexbarContext)
            else:
                return self.getTypedRuleContext(Parser.PciexbarContext,i)


        def getRuleIndex(self):
            return Parser.RULE_seriallog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSeriallog" ):
                listener.enterSeriallog(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSeriallog" ):
                listener.exitSeriallog(self)




    def seriallog(self):

        localctx = Parser.SeriallogContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_seriallog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==Parser.PCIEBAR_VALUE:
                self.state = 6
                self.pciexbar()
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 12
            self.match(Parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PciexbarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PCIEBAR_VALUE(self):
            return self.getToken(Parser.PCIEBAR_VALUE, 0)

        def PCIEBAR_VALUE_MODE_FINAL_VALUE(self):
            return self.getToken(Parser.PCIEBAR_VALUE_MODE_FINAL_VALUE, 0)

        def getRuleIndex(self):
            return Parser.RULE_pciexbar

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPciexbar" ):
                listener.enterPciexbar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPciexbar" ):
                listener.exitPciexbar(self)




    def pciexbar(self):

        localctx = Parser.PciexbarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_pciexbar)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.match(Parser.PCIEBAR_VALUE)
            self.state = 15
            self.match(Parser.PCIEBAR_VALUE_MODE_FINAL_VALUE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BiosidContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BIOS_ID(self):
            return self.getToken(Parser.BIOS_ID, 0)

        def getRuleIndex(self):
            return Parser.RULE_biosid

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBiosid" ):
                listener.enterBiosid(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBiosid" ):
                listener.exitBiosid(self)




    def biosid(self):

        localctx = Parser.BiosidContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_biosid)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.match(Parser.BIOS_ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





