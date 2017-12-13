import lexer.lexer as lex

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

for token in lex.tokenize(code):
    list_of_tokens.append(token)


def parse(code):
    pass