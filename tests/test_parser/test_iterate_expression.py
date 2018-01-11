from unittest import TestCase
from sample.parser import parser
from sample.lexer import lexer


class TestIterateExpression(TestCase):
    def setUp(self):
        self.assert_successful_parsing = "iterate( 3 ) {}"
        self.assert_raise_program_except = "( 4) {}"
        self.assert_raise_lparent_except = "iterate 5 ) {}"
        self.assert_raise_rparent_except = "iterate ( 44 {}"
        self.assert_raise_lcurl_except = "iterate ( 34 ) }"
        self.assert_raise_rcurl_except = "iterate ( 5 ) {"
        self.assert_raise_no_condition_except = "iterate ( ) {}"
        self.assert_raise_incorrect_condition_except = "iterate( no-beepers-in-beeper-bag ) {}"

    def test_iterate_expression_successful_parsing(self):
        parser.index = 0
        parser.tokens = TestIterateExpression.set_list_of_tokens(self.assert_successful_parsing)
        try:
            parser.iterate_expression()
        except Exception as error:
            self.fail("Unexpected failure: {}".format(error))

    def test_iterate_expression_raise_name_function_exception(self):
        parser.index = 0
        parser.tokens = TestIterateExpression.set_list_of_tokens(self.assert_raise_program_except)
        self.assertRaises(RuntimeError, parser.iterate_expression)

    def test_iterate_expression_raise_lparen_exception(self):
        parser.index = 0
        parser.tokens = TestIterateExpression.set_list_of_tokens(self.assert_raise_lparent_except)
        self.assertRaises(RuntimeError, parser.iterate_expression)

    def test_iterate_expression_raise_rparen_exception(self):
        parser.index = 0
        parser.tokens = TestIterateExpression.set_list_of_tokens(self.assert_raise_rparent_except)
        self.assertRaises(RuntimeError, parser.iterate_expression)

    def test_iterate_expression_raise_lcurl_exception(self):
        parser.index = 0
        parser.tokens = TestIterateExpression.set_list_of_tokens(self.assert_raise_lcurl_except)
        self.assertRaises(RuntimeError, parser.iterate_expression)

    def test_iterate_expression_raise_rcurl_exception(self):
        parser.index = 0
        parser.tokens = TestIterateExpression.set_list_of_tokens(self.assert_raise_rcurl_except)
        self.assertRaises(RuntimeError, parser.iterate_expression)

    def test_iterate_expression_raise_no_condition_except(self):
        parser.index = 0
        parser.tokens = TestIterateExpression.set_list_of_tokens(self.assert_raise_no_condition_except)
        self.assertRaises(RuntimeError, parser.iterate_expression)

    def test_iterate_expression_raise_incorrect_condition_except(self):
        parser.index = 0
        parser.tokens = TestIterateExpression.set_list_of_tokens(self.assert_raise_no_condition_except)
        self.assertRaises(RuntimeError, parser.iterate_expression)

    @staticmethod
    def set_list_of_tokens(code):
        list_of_tokens = list()
        for token in lexer.tokenize(code):
            list_of_tokens.append(token)
        return list_of_tokens

