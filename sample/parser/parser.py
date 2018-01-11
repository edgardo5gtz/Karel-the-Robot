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
        functions()


def main_function():
    global index
    global tokens
    if demand('program'):
        if demand('LPAREN'):
            if demand('RPAREN'):
                if demand('LCURL'):
                    body()
                    if not demand('RCURL'):
                        raise RuntimeError('Missing }} after line {}'.format(tokens.pop(index - 1).line))
                else:
                    raise RuntimeError('Missing {{ in line {}'.format(tokens.pop(index).line))
            else:
                raise RuntimeError('Missing ) in line {}'.format(tokens.pop(index).line))
        else:
            raise RuntimeError('Missing ( in line {}'.format(tokens.pop(index).line))
    else:
        raise RuntimeError('Missing program in line {}'.format(tokens.pop(index).line))


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
    if expression():
        body()


def expression():
    if verify('if'):
        if_expression()
    elif verify('while'):
        while_expression()
    elif verify('iterate'):
        iterate_expression()
    elif verify('ID') or verify('CONDITION'):
        call_function()
    else:
        return False


def call_function():
    global index
    global tokens
    name_function()
    if demand('LPAREN'):
        if not demand('RPAREN'):
            raise RuntimeError('Missing ( after line {}'.format(tokens.pop(index-1).line))
    else:
        raise RuntimeError('Missing ) after line {}'.format(tokens.pop(index - 1).line))


def name_function():
    global index
    global tokens
    if verify('ID'):
        customer_function()
    elif verify('INSTRUCTION'):
        official_function()
    else:
        raise RuntimeError('Missing name function after line {}'.format(tokens.pop(index-1).line))


def if_expression():
    global index
    global tokens
    if demand('if'):
        if demand('LPAREN'):
            if demand('CONDITION'):
                if demand('RPAREN'):
                    if demand('LCURL'):
                        body()
                        if not demand('RCURL'):
                            raise RuntimeError('Missing }} after line {}'.format(tokens.pop(index - 1).line))
                    else:
                        raise RuntimeError('Missing {{ in line {}'.format(tokens.pop(index).line))
                else:
                    raise RuntimeError('Missing ) in line {}'.format(tokens.pop(index).line))
            else:
                raise RuntimeError('Missing or incorrect condition in line {}'.format(tokens.pop(index).line))
        else:
            raise RuntimeError('Missing ( in line {}'.format(tokens.pop(index).line))
    else:
        raise RuntimeError('Missing if in line {}'.format(tokens.pop(index).line))


def else_expression():
    global index
    global tokens
    if demand('else'):
        if demand('LCURL'):
            body()
            if not demand('RCURL'):
                raise RuntimeError('Missing }} after line {}'.format(tokens.pop(index).line))
        else:
            raise RuntimeError('Missing {{ in line {}'.format(tokens.pop(index).line))
    else:
        raise RuntimeError('Missing else in line {}'.format(tokens.pop(index).line))


def while_expression():
    global index
    global tokens
    if demand('while'):
        if demand('LPAREN'):
            if demand('CONDITION'):
                if demand('RPAREN'):
                    if demand('LCURL'):
                        body()
                        if not demand('RCURL'):
                            raise RuntimeError('Missing }} after line {}'.format(tokens.pop(index - 1).line))
                    else:
                        raise RuntimeError('Missing {{ in line {}'.format(tokens.pop(index).line))
                else:
                    raise RuntimeError('Missing ) in line {}'.format(tokens.pop(index).line))
            else:
                raise RuntimeError('Missing or incorrect condition in line {}'.format(tokens.pop(index).line))
        else:
            raise RuntimeError('Missing ( in line {}'.format(tokens.pop(index).line))
    else:
        raise RuntimeError('Missing while in line {}'.format(tokens.pop(index).line))


def iterate_expression():
    global index
    global tokens
    if demand('iterate'):
        if demand('LPAREN'):
            if demand('NUMBER'):
                if demand('RPAREN'):
                    if demand('LCURL'):
                        body()
                        if not demand('RCURL'):
                            raise RuntimeError('Missing }} after line {}'.format(tokens.pop(index - 1).line))
                    else:
                        raise RuntimeError('Missing {{ in line {}'.format(tokens.pop(index).line))
                else:
                    raise RuntimeError('Missing ) in line {}'.format(tokens.pop(index).line))
            else:
                raise RuntimeError('Missing or incorrect condition in line {}'.format(tokens.pop(index).line))
        else:
            raise RuntimeError('Missing ( in line {}'.format(tokens.pop(index).line))
    else:
        raise RuntimeError('Missing while in line {}'.format(tokens.pop(index).line))


def official_function():
    if not demand("INSTRUCTION"):
        raise RuntimeError('Missing official function after line {}'.format(tokens.pop(index-1).line))


def customer_function():
    if not demand("ID"):
        raise RuntimeError('Missing customer function after line {}'.format(tokens.pop(index-1).line))


def demand(token_type):
    global index
    global tokens
    try:
        element = tokens.pop(index)
    except IndexError:       # If the last token of any definition is not written
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
    except IndexError:      # If the last token of any definition is not written
        index -= 1
        return False
    tokens.insert(index, element)
    return True if token_type == element.type else False


if __name__ == '__main__':
    pass
