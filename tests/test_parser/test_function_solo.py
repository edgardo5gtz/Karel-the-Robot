from unittest import TestCase
from sample.parser import parser
from sample.lexer import lexer


class TestFunctionSolo(TestCase):
    def setUp(self):
        self.assert_successful_parsing = "void funo() {}"
        self.assert_raise_name_function_except = "void () {}"
        self.assert_raise_lparent_except = "void funo) {}"
        self.assert_raise_rparent_except = "void funo( {}"
        self.assert_raise_lcurl_except = "void funo() }"
        self.assert_raise_rcurl_except = "void funo() {"

    def test_function_solo_successful_parsing(self):
        parser.index = 0
        parser.tokens = TestFunctionSolo.set_list_of_tokens(self.assert_successful_parsing)
        try:
            parser.function_solo()
        except Exception as error:
            self.fail("Unexpected failure: {}".format(error))

    def test_function_solo_raise_name_function_exception(self):
        parser.index = 0
        parser.tokens = TestFunctionSolo.set_list_of_tokens(self.assert_raise_name_function_except)
        self.assertRaises(RuntimeError, parser.function_solo)

    def test_function_solo_raise_lparen_exception(self):
        parser.index = 0
        parser.tokens = TestFunctionSolo.set_list_of_tokens(self.assert_raise_lparent_except)
        self.assertRaises(RuntimeError, parser.function_solo)

    def test_function_solo_raise_rparen_exception(self):
        parser.index = 0
        parser.tokens = TestFunctionSolo.set_list_of_tokens(self.assert_raise_rparent_except)
        self.assertRaises(RuntimeError, parser.function_solo)

    def test_function_solo_raise_lcurl_exception(self):
        parser.index = 0
        parser.tokens = TestFunctionSolo.set_list_of_tokens(self.assert_raise_lcurl_except)
        self.assertRaises(RuntimeError, parser.function_solo)

    def test_function_solo_raise_rcurl_exception(self):
        parser.index = 0
        parser.tokens = TestFunctionSolo.set_list_of_tokens(self.assert_raise_rcurl_except)
        self.assertRaises(RuntimeError, parser.function_solo)

    @staticmethod
    def set_list_of_tokens(code):
        list_of_tokens = list()
        for token in lexer.tokenize(code):
            list_of_tokens.append(token)
        return list_of_tokens
