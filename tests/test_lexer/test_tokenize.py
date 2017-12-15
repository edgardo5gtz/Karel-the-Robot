from unittest import TestCase
from sample.lexer import lexer as lex


class TestLexer(TestCase):
    def setUp(self):
        self.code_input = open("test_lexer_input.txt", 'r')
        self.assertion_output = open("test_lexer_assertions.txt", 'r')
        self.lexer_output = open("test_lexer_output.txt", 'w')

    def test_tokenize(self):
        list_of_tokens = lex.tokenize(self.code_input.read())
        output = list()
        for token in list_of_tokens:
            output.append(str(token))
        answer = self.assertion_output.read().splitlines()
        self.close_files()
        self.assertListEqual(output, answer)

    def close_files(self):
        self.code_input.close()
        self.assertion_output.close()
        self.lexer_output.close()