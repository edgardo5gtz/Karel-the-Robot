from unittest import TestCase
from sample.parser import parser
from sample.lexer import lexer


class TestElseExpression(TestCase):
    def setUp(self):
        self.assert_succesful_parsing = "else { }"   # Successful parsing
        self.assert_raise_lcurl_except = "else }"    # Raise lcurl exception
        self.assert_raise_rcurl_except = "else {"    # Raise rcurl exception

    def test_else_expression_successful_parsing(self):
        parser.index = 0
        parser.tokens = TestElseExpression.set_list_of_tokens(self.assert_succesful_parsing)
        try:
            parser.else_expression()
        except Exception as error:
            self.fail("Unexpected failure as {}".format(error))

    def test_else_expression_raise_lcurl_exception(self):
        parser.index = 0
        parser.tokens = TestElseExpression.set_list_of_tokens(self.assert_raise_lcurl_except)
        self.assertRaises(RuntimeError, parser.else_expression)

    def test_else_expression_raise_rcurl_exception(self):
        parser.index = 0
        parser.tokens = TestElseExpression.set_list_of_tokens(self.assert_raise_rcurl_except)
        self.assertRaises(RuntimeError, parser.else_expression)

    @staticmethod
    def set_list_of_tokens(code):
        list_of_tokens = list()
        for token in lexer.tokenize(code):
            list_of_tokens.append(token)
        return list_of_tokens

