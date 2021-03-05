from DataParser.parser.Parser import Parser
from DataParser.parser.ParserListener import ParserListener

class Listener(ParserListener):
    def __init__(self, data_structure):
        self.data = data_structure

    # Enter a parse tree produced by Parser#pciexbar.
    def enterPciexbar(self, ctx: Parser.PciexbarContext):
        l = [ctx.children[0].getText(), ctx.children[1].getText()]
        self.data.add_data(TrainingStep='Attributes', Key=l[0], Value=l[1])