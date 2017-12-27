"""
Author: Edgardo Gutierrez Trujillo

"""

tokens = list()
index = 0


def parse():
    program()
    print("End parsing")


def program():
    global index
    global tokens
    if demand('class'):
        if demand('program'):
            if demand('LCURL'):
                functions()
                main_function()
                if not demand('RCURL'):
                    raise RuntimeError('Missing }} after line {}'.format(tokens.pop(index).line))
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
                        raise RuntimeError('Missing }} after line {}'.format(tokens.pop(index-1).line))
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
    if demand('ID'):
        pass
    else:
        raise RuntimeError("Missing the function name in line".format(tokens.pop(index).line))


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
    try:
        element = tokens.pop(index)
    except IndexError:
        index -= 1
        return False
    tokens.insert(index, element)
    if token_type == element.type:
        index += 1
        return True
    return False


def verify(token_type):
    global tokens
    global index
    try:
        element = tokens.pop(index)
    except IndexError:
        index -= 1
        return False
    tokens.insert(index, element)
    return True if token_type == element.type else False


if __name__ == '__main__':
    pass
