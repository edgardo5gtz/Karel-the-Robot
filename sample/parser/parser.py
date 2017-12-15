from sample import lexer as lex

code = ''' class program {
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
list_of_tokens = list()
index = 0

for token in lex.tokenize(code):
    list_of_tokens.append(token)


def parse(tokens):
    program(tokens)


def program(tokens):
    if demand('class'):
        pass


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
    if token_type == list_of_tokens.index(index).get('type'):
        index += 1
        return True
    return False


def verify(token_type):
    global list_of_tokens
    return True if token_type == list_of_tokens.index(index).get('type') else False
