from unittest import TestCase
from sample.parser import parser
from sample.lexer import lexer


class TestIfExpression(TestCase):
    def setUp(self):
        self.assert_successful_parsing = "if( no-beepers-in-beeper-bag ) {}"
        self.assert_raise_program_except = "( no-beepers-in-beeper-bag ) {}"
        self.assert_raise_lparent_except = "program no-beepers-in-beeper-bag ) {}"
        self.assert_raise_rparent_except = "program( no-beepers-in-beeper-bag {}"
        self.assert_raise_lcurl_except = "program( no-beepers-in-beeper-bag ) }"
        self.assert_raise_rcurl_except = "program( no-beepers-in-beeper-bag ) {"
        self.assert_raise_no_condition_except = "if( ) {}"
        self.assert_raise_incorrect_condition_except = "if( no-beepers-in-beeper-ba ) {}"

    def test_if_expression_successful_parsing(self):
        parser.index = 0
        parser.tokens = TestIfExpression.set_list_of_tokens(self.assert_successful_parsing)
        try:
            parser.if_expression()
        except Exception as error:
            self.fail("Unexpected failure: {}".format(error))

    def test_if_expression_raise_name_function_exception(self):
        parser.index = 0
        parser.tokens = TestIfExpression.set_list_of_tokens(self.assert_raise_program_except)
        self.assertRaises(RuntimeError, parser.if_expression)

    def test_if_expression_raise_lparen_exception(self):
        parser.index = 0
        parser.tokens = TestIfExpression.set_list_of_tokens(self.assert_raise_lparent_except)
        self.assertRaises(RuntimeError, parser.if_expression)

    def test_if_expression_raise_rparen_exception(self):
        parser.index = 0
        parser.tokens = TestIfExpression.set_list_of_tokens(self.assert_raise_rparent_except)
        self.assertRaises(RuntimeError, parser.if_expression)

    def test_if_expression_raise_lcurl_exception(self):
        parser.index = 0
        parser.tokens = TestIfExpression.set_list_of_tokens(self.assert_raise_lcurl_except)
        self.assertRaises(RuntimeError, parser.if_expression)

    def test_if_expression_raise_rcurl_exception(self):
        parser.index = 0
        parser.tokens = TestIfExpression.set_list_of_tokens(self.assert_raise_rcurl_except)
        self.assertRaises(RuntimeError, parser.if_expression)

    def test_if_expression_raise_no_condition_except(self):
        parser.index = 0
        parser.tokens = TestIfExpression.set_list_of_tokens(self.assert_raise_no_condition_except)
        self.assertRaises(RuntimeError, parser.if_expression)

    def test_if_expression_raise_incorrect_condition_except(self):
        parser.index = 0
        parser.tokens = TestIfExpression.set_list_of_tokens(self.assert_raise_no_condition_except)
        self.assertRaises(RuntimeError, parser.if_expression)

    @staticmethod
    def set_list_of_tokens(code):
        list_of_tokens = list()
        for token in lexer.tokenize(code):
            list_of_tokens.append(token)
        return list_of_tokens
