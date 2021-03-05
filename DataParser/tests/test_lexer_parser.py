import unittest
import os

from DataParser.main import build_lexer_parser, Antler_Parsing
from DataParser import getTokensFromText
from DataParser.parser.Lexer import Lexer as MyLexer
from antlr4 import Token,InputStream

this_file_dir = os.path.dirname(os.path.abspath(__file__))

class TestMain(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #compile lexer and parser based on rule
        build_lexer_parser()
        print('done with generation of G4\n')

    def test_lexer(self):
        to_parse = 'PCIEXBAR is E0000000\nanan PCIEXBAR is E0000001'
        tokens = getTokensFromText(to_parse, MyLexer)
        #self.assertEqual(2, len(tokens))  # // includes EOF
        expected_tokens = [MyLexer.PCIEBAR_VALUE,MyLexer.PCIEBAR_VALUE_MODE_FINAL_VALUE,MyLexer.PCIEBAR_VALUE,MyLexer.PCIEBAR_VALUE_MODE_FINAL_VALUE,Token.EOF]
        for i, expected_token in enumerate(expected_tokens):
            self.assertEqual(expected_token, tokens[i].type, f'TOKEN ({i}) failed to compare')


    def test_parser(self):
        text_to_parse = '''MiniBIOS MRC hello world
                                NemData Address/Size: 0xFEF80000 / 0x40000
                                TopStackAddr: 0xFEFB7F58
                                sizeof (MrcParameters): 100617
                                  sizeof (MrcInput):     20026
                                  sizeof (MrcOutput):    34354
                                  sizeof (MrcSave):      46221
                                sizeof (MrcIntOutput):   16179
                                MCHBAR is FED00000
                                PCIEXBAR is E0000000
                                Cpu Model/Stepping: 0x806C0
                                TigerLake ULT/ULX: Stepping A0
                                Microcode Update: 0x00000048
                                Post Code: DD00h
                                EcBoardInfo: 0x1
                                '''
        all_tokens = getTokensFromText(text_to_parse, MyLexer)
        easier = [(token.type, token) for token in all_tokens]
        #need to pass it to parser
        obj = Antler_Parsing(os.path.join(this_file_dir, 'test_lexer_parser.py'))
        # alps_obj =alps_core.AlpsCore(os.path.join(this_files_dir, 'test_dib.py'),
        #                    'tigerlake',testid=fake_testid, subtestid='', logid='', description='')
        # alps_obj.file_stream = InputStream(text_to_parse)
        # alps_obj.setupParseLog()
        # alps_obj.main()
        # alps_obj.parseLog()
        # alps_obj.unified_data_model_post_processing()
        # attributes = [d for d in alps_obj.data_structure if 'TrainingStep' in d and d['TrainingStep'] == 'Attributes']
        # basic_attr_dict = [(row['Key'],row['Value']) for row in attributes]
        #
        # pass
