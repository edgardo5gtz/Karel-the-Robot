from unittest import TestCase
from sample.parser import parser
from sample.lexer import lexer


class TestWhileExpression(TestCase):
    def setUp(self):
        self.assert_successful_parsing = "while( no-beepers-in-beeper-bag ) {}"
        self.assert_raise_program_except = "( no-beepers-in-beeper-bag ) {}"
        self.assert_raise_lparent_except = "while no-beepers-in-beeper-bag ) {}"
        self.assert_raise_rparent_except = "while( no-beepers-in-beeper-bag {}"
        self.assert_raise_lcurl_except = "while( no-beepers-in-beeper-bag ) }"
        self.assert_raise_rcurl_except = "while( no-beepers-in-beeper-bag ) {"
        self.assert_raise_no_condition_except = "while( ) {}"
        self.assert_raise_incorrect_condition_except = "if( no-beepers-in-beeper-ba ) {}"

    def test_while_expression_successful_parsing(self):
        parser.index = 0
        parser.tokens = TestWhileExpression.set_list_of_tokens(self.assert_successful_parsing)
        try:
            parser.while_expression()
        except Exception as error:
            self.fail("Unexpected failure: {}".format(error))

    def test_while_expression_raise_name_function_exception(self):
        parser.index = 0
        parser.tokens = TestWhileExpression.set_list_of_tokens(self.assert_raise_program_except)
        self.assertRaises(RuntimeError, parser.while_expression)

    def test_while_expression_raise_lparen_exception(self):
        parser.index = 0
        parser.tokens = TestWhileExpression.set_list_of_tokens(self.assert_raise_lparent_except)
        self.assertRaises(RuntimeError, parser.while_expression)

    def test_while_expression_raise_rparen_exception(self):
        parser.index = 0
        parser.tokens = TestWhileExpression.set_list_of_tokens(self.assert_raise_rparent_except)
        self.assertRaises(RuntimeError, parser.while_expression)

    def test_while_expression_raise_lcurl_exception(self):
        parser.index = 0
        parser.tokens = TestWhileExpression.set_list_of_tokens(self.assert_raise_lcurl_except)
        self.assertRaises(RuntimeError, parser.while_expression)

    def test_while_expression_raise_rcurl_exception(self):
        parser.index = 0
        parser.tokens = TestWhileExpression.set_list_of_tokens(self.assert_raise_rcurl_except)
        self.assertRaises(RuntimeError, parser.while_expression)

    def test_while_expression_raise_no_condition_except(self):
        parser.index = 0
        parser.tokens = TestWhileExpression.set_list_of_tokens(self.assert_raise_no_condition_except)
        self.assertRaises(RuntimeError, parser.while_expression)

    def test_while_expression_raise_incorrect_condition_except(self):
        parser.index = 0
        parser.tokens = TestWhileExpression.set_list_of_tokens(self.assert_raise_no_condition_except)
        self.assertRaises(RuntimeError, parser.while_expression)

    @staticmethod
    def set_list_of_tokens(code):
        list_of_tokens = list()
        for token in lexer.tokenize(code):
            list_of_tokens.append(token)
        return list_of_tokens

