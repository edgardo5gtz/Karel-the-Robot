from sample.lexer import lexer as lex

code = ''' class program {}
   '''
list_of_tokens = list()
index = 0

for token in lex.tokenize(code):
    list_of_tokens.append(token)


def parse(tokens):
    program(tokens)
    print("End parsing")
    return True


def program(tokens):
    global index
    if demand('class'):
        if demand('program'):
            if demand('LCURL'):
                functions()
                main_function()
                if not demand('RCURL'):
                    raise RuntimeError('Missing }} in line {}'.format(tokens.pop(index).line))
            else:
                raise RuntimeError('Missing {{ in line {}'.format(tokens.pop(index).line))
        else:
            raise RuntimeError('Missing program in line {}'.format(tokens.pop(index).line))
    else:
        raise RuntimeError('Missing class in line {}'.format(tokens.pop(index).line))


def functions():
    pass


def functions_prima():
    pass


def main_function():
    pass


def function_solo():
    pass


def body():
    pass


def body_prime():
    pass


def expression():
    pass


def call_function():
    pass


def name_function():
    pass


def if_expression():
    pass


def else_expression():
    pass


def while_expression():
    pass


def iterate_expression():
    pass


def official_function():
    pass


def customer_function():
    pass


def demand(token_type):
    global index
    global list_of_tokens
    element = list_of_tokens.pop(index)
    list_of_tokens.insert(index, element)
    if token_type == element.type:
        index += 1
        return True
    return False


def verify(token_type):
    global list_of_tokens
    return True if token_type == list_of_tokens.index(index).get('type') else False
