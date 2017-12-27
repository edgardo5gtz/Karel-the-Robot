"""
Author: Edgardo Gutierrez Trujillo

"""

tokens = list()
index = 0


def parse():
    program()
    print("End parsing")
    return True


def program():
    global index
    global tokens
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
    if verify("void"):
        function_solo()
        functions_prima()


def functions_prima():
    pass


def main_function():
    pass


def function_solo():
    global index
    global tokens
    if demand('void'):
        name_function()
        if demand('LPAREN'):
            if demand('RPAREN'):
                if demand('LCURL'):
                    body()
                    if not demand('RCURL'):
                        raise RuntimeError('Missing }} in line {}'.format(tokens.pop(index).line))
                else:
                    raise RuntimeError('Missing {{ in line {}'.format(tokens.pop(index).line))
            else:
                raise RuntimeError('Missing ) in line {}'.format(tokens.pop(index).line))
        else:
            raise RuntimeError('Missing ( in line {}'.format(tokens.pop(index).line))
    else:
        raise RuntimeError('Missing void in line {}'.format(tokens.pop(index).line))


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
    global tokens
    element = tokens.pop(index)
    tokens.insert(index, element)
    if token_type == element.type:
        index += 1
        return True
    return False


def verify(token_type):
    global tokens
    global index
    element = tokens.pop(index)
    tokens.insert(index, element)
    return True if token_type == element.type else False


if __name__ == '__main__':
    pass
