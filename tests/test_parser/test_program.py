from unittest import TestCase
from sample.parser import parser
from sample.lexer.lexer import tokenize

class TestProgram(TestCase):
    def setUp(self):
        self.code_input = open("test_parser_input.txt", "r")
        self.list_of_tokens = list()
        for token in tokenize(self.code_input.read()):
            self.list_of_tokens.append(token)

    def test_program(self):
        result = parser.parse(self.list_of_tokens)
        self.close_files()
        self.assertTrue(result)

    def close_files(self):
        self.code_input.close()
