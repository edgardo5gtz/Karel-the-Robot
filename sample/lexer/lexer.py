# Tokenizer example from https://docs.python.org/3/library/re.html
#
# Adapted for Karel Grammar by Edgardo Gutierrez Trujillo
#

import collections
import re

Token = collections.namedtuple('Token', ['type', 'value', 'line'])


def tokenize(code):
    keywords = {'class', 'if', 'iterate', 'while', 'void', 'else', 'program'}
    token_specification = [                         # Specification order matters for matching priority
        ('NUMBER',      r'\d+'),                    # Integers
        ('LPAREN',      r'\('),                     # Left parenthesis
        ('RPAREN',      r'\)'),                     # Right parenthesis
        ('LCURL',       r'\{'),                     # Left curly brace
        ('RCURL',       r'\}'),                     # Right curly brace
        ('INSTRUCTION', r'move|'                    # Built-in instructions
                        r'pickbeeper|'
                        r'putbeeper|'
                        r'turnleft|'
                        r'end'),
        ('CONDITION',   r'front-is-clear|'          # Built-in conditions
                        r'left-is-clear|'
                        r'right-is-clear|'
                        r'front-is-blocked|'
                        r'left-is-blocked|'
                        r'right-is-blocked|'
                        r'next-to-a-beeper|'
                        r'not-next-to-a-beeper|'
                        r'facing-north|'
                        r'facing-south|'
                        r'facing-east|'
                        r'facing-west|'
                        r'not-facing-north|'
                        r'not-facing-south|'
                        r'not-facing-east|'
                        r'not-facing-west|'
                        r'any-beepers-in-beeper-bag|'
                        r'no-beepers-in-beeper-bag'),
        ('ID',          r'[A-Za-z][A-Za-z_]*'),     # Identifiers
        ('NEWLINE',     r'\n'),                     # Line endings
        ('SKIP',        r'[ \t]+'),                 # Skip over spaces and tabs
        ('MISMATCH',    r'.'),                      # Any other character
    ]
    tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
    line_num = 1
    for mo in re.finditer(tok_regex, code):
        kind = mo.lastgroup
        value = mo.group(kind)
        if kind == 'NEWLINE':
            line_num += 1
        elif kind == 'SKIP':
            pass
        elif kind == 'MISMATCH':
            raise RuntimeError(f'{value!r} unexpected on line {line_num}')
        else:
            if kind == 'ID' and value in keywords:
                kind = value
            yield Token(kind, value, line_num)


if __name__ == '__main__':
    
    statements = ''' class program {
      void funo() {
        turnleft()
        turnleft()
        turnleft()
      }
      void fdos() {
        move()
        move()
        move()
        funo()
      }
      program() {
        move()
        fdos()
        move()
        end()
      }
    }
    '''

    for token in tokenize(statements):
        print(token)
