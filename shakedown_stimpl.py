from stimpl import *

if __name__=='__main__':
  program = Print(Assign(Variable("i"), StringLiteral("Hello, World")))
  run_stimpl(program)
