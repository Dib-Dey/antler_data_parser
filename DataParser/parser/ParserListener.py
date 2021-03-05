# Generated from C:\ddey_documents\GitHub_Python\antler_data_parsing\DataParser\parser\Parser.g4 by ANTLR 4.8
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .Parser import Parser
else:
    from Parser import Parser

# This class defines a complete listener for a parse tree produced by Parser.
class ParserListener(ParseTreeListener):

    # Enter a parse tree produced by Parser#seriallog.
    def enterSeriallog(self, ctx:Parser.SeriallogContext):
        pass

    # Exit a parse tree produced by Parser#seriallog.
    def exitSeriallog(self, ctx:Parser.SeriallogContext):
        pass


    # Enter a parse tree produced by Parser#pciexbar.
    def enterPciexbar(self, ctx:Parser.PciexbarContext):
        pass

    # Exit a parse tree produced by Parser#pciexbar.
    def exitPciexbar(self, ctx:Parser.PciexbarContext):
        pass


    # Enter a parse tree produced by Parser#biosid.
    def enterBiosid(self, ctx:Parser.BiosidContext):
        pass

    # Exit a parse tree produced by Parser#biosid.
    def exitBiosid(self, ctx:Parser.BiosidContext):
        pass



del Parser