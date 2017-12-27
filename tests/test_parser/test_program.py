from unittest import TestCase
from sample.parser import parser
from sample.lexer.lexer import tokenize


class TestProgram(TestCase):
    def setUp(self):
        self.assert_succesful_parsing = "class program { }"   # Successful parsing
        self.assert_raise_class_except = "program {}"         # Raise class exception
        self.assert_raise_program_except = "class {}"         # Raise program exception
        self.assert_raise_lcurl_except = "class program }"    # Raise lcurl exception
        self.assert_raise_rcurl_except = "class program {"    # Raise rcurl exception

    def test_program_successful_parsing(self):
        parser.index = 0
        parser.tokens = TestProgram.set_list_of_tokens(self.assert_succesful_parsing)
        try:
            parser.parse()
        except Exception as error:
            self.fail("Unexpected failure as {}".format(error))

    def test_program_raise_class_exception(self):
        parser.index = 0
        parser.tokens = TestProgram.set_list_of_tokens(self.assert_raise_class_except)
        self.assertRaises(RuntimeError, parser.parse)

    def test_program_raise_program_exception(self):
        parser.index = 0
        parser.tokens = TestProgram.set_list_of_tokens(self.assert_raise_program_except)
        self.assertRaises(RuntimeError, parser.parse)

    def test_program_raise_lcurl_exception(self):
        parser.index = 0
        parser.tokens = TestProgram.set_list_of_tokens(self.assert_raise_lcurl_except)
        self.assertRaises(RuntimeError, parser.parse)

    def test_program_raise_rcurl_exception(self):
        parser.index = 0
        parser.tokens = TestProgram.set_list_of_tokens(self.assert_raise_rcurl_except)
        self.assertRaises(RuntimeError, parser.parse)

    @staticmethod
    def set_list_of_tokens(code):
        list_of_tokens = list()
        for token in tokenize(code):
            list_of_tokens.append(token)
        return list_of_tokens
