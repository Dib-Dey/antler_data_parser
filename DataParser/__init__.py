from antlr4 import CommonTokenStream, InputStream

def getTokensFromText(input_string_to_parse, tLexer):
    input_stream = InputStream(input_string_to_parse)
    lexer = tLexer(input_stream) #lexer object is created
    stream = CommonTokenStream(lexer)
    stream.fill()
    return stream.tokens