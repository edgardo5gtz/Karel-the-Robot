from unittest import TestCase
from sample.parser import parser
from sample.lexer import lexer


class TestMainFunction(TestCase):
    def setUp(self):
        self.assert_successful_parsing = "program() {}"
        self.assert_raise_program_except = "() {}"
        self.assert_raise_lparent_except = "program) {}"
        self.assert_raise_rparent_except = "program( {}"
        self.assert_raise_lcurl_except = "program() }"
        self.assert_raise_rcurl_except = "program() {"

    def test_main_function_successful_parsing(self):
        parser.index = 0
        parser.tokens = TestMainFunction.set_list_of_tokens(self.assert_successful_parsing)
        try:
            parser.main_function()
        except Exception as error:
            self.fail("Unexpected failure: {}".format(error))

    def test_main_function_raise_name_function_exception(self):
        parser.index = 0
        parser.tokens = TestMainFunction.set_list_of_tokens(self.assert_raise_program_except)
        self.assertRaises(RuntimeError, parser.main_function)

    def test_main_function_raise_lparen_exception(self):
        parser.index = 0
        parser.tokens = TestMainFunction.set_list_of_tokens(self.assert_raise_lparent_except)
        self.assertRaises(RuntimeError, parser.main_function)

    def test_main_function_raise_rparen_exception(self):
        parser.index = 0
        parser.tokens = TestMainFunction.set_list_of_tokens(self.assert_raise_rparent_except)
        self.assertRaises(RuntimeError, parser.main_function)

    def test_main_function_raise_lcurl_exception(self):
        parser.index = 0
        parser.tokens = TestMainFunction.set_list_of_tokens(self.assert_raise_lcurl_except)
        self.assertRaises(RuntimeError, parser.main_function)

    def test_main_function_raise_rcurl_exception(self):
        parser.index = 0
        parser.tokens = TestMainFunction.set_list_of_tokens(self.assert_raise_rcurl_except)
        self.assertRaises(RuntimeError, parser.main_function)

    @staticmethod
    def set_list_of_tokens(code):
        list_of_tokens = list()
        for token in lexer.tokenize(code):
            list_of_tokens.append(token)
        return list_of_tokens

