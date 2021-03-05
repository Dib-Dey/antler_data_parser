import os
import subprocess
import importlib
from antlr4 import FileStream, CommonTokenStream
import DataParser.parser.listner_for_overriding
this_file_dir = os.path.dirname(os.path.abspath(__file__))


def build_lexer_parser():
    cur_dir = this_file_dir
    parser_dir = os.path.join(cur_dir, "parser")
    java_paths = [r'C:\Program Files\JetBrains\PyCharm Community Edition 2020.1\jbr\bin\java.exe',
                  r'C:\Program Files\JetBrains\PyCharm Community Edition 2020.1.1\jbr\bin\java.exe',
                  r'C:\Program Files\JetBrains\PyCharm Community Edition 2020.2.2\jbr\bin\java.exe']
    for item in java_paths:
        if os.path.exists(item):
            java_path = item
            break
    # find antler compilation jar file
    antlr_path = os.path.join(cur_dir, 'utils', 'antlr-4.8-complete.jar')
    # Lexer and Parser files
    g4_files = ['Lexer.g4', 'Parser.g4']
    for g4_file in g4_files:
        print('starting G4 build of : {}'.format(g4_file))
        cmd = '"{}" -Xmx500M -cp "{}" org.antlr.v4.Tool {} -Dlanguage=Python3' \
            .format(java_path,
                    antlr_path,
                    os.path.join(parser_dir, g4_file))
        # print(cmd)
        process = subprocess.Popen(cmd, cwd=parser_dir, shell=True, stdout=subprocess.PIPE,
                                   stderr=subprocess.STDOUT)
        stdout, stderr = process.communicate()
        exitCode = process.returncode
        if exitCode != 0:
            print(stdout)
            assert False, stderr
        else:
            prefix = 'antlr build output: {}'
            if stdout:
                print(prefix.format(stdout))
            if stderr:
                print(prefix.format(stderr))
    print('G4 build finished\n')

class Antler_Parsing:
    def __init__(self,input):
        self.input = input
        self.file_stream = FileStream(self.input)
        self.setupParseLog()
        self.data_structure = []

    def add_data(self, **kwargs):
        self.data_structure.append(dict(kwargs))

    def setupParseLog(self):
        self.lexer = importlib.import_module('DataParser.parser.Lexer').Lexer(self.file_stream)
        self.stream = CommonTokenStream(self.lexer)
        self.parser = importlib.import_module('DataParser.parser.Lexer').Parser(self.stream)
        self.printer = importlib.import_module('DataParser.parser.listner_for_overriding').Listener(data_structure=self)
        pass
    #
    #     self.stream = CommonTokenStream(self.lexer)
    #     self.parser = importlib.import_module('antler.parser.Parser'.format(self.rule_set)).Parser(self.stream)
    #     self.printer = importlib.import_module('pysvtools.alps.parsers.{}.listener'.format(self.rule_set)).Listener(data_structure=self)
    #     self.parser.removeErrorListeners()
    #     if self.quiet_errors:
    #         self.errorListener = None
    #         self.lexer.removeErrorListeners()
    #     else:
    #         self.errorListener = AlpsErrorListener()
    #         self.parser.addErrorListener(self.errorListener)

if __name__ == '__main__':
    #obj = Antler_Parsing()
    build_lexer_parser()
