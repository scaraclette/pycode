from basic import Stack

# INFIX TO POSTFIX
def infixToPostfix(infixexpr):
  prec = {"**": 4, "*":3, "/":3, "+":2, "-":2, "(":1}
  # Stack for operators 
  opStack = Stack()

  # final results
  postfixList = []
  tokenList = infixexpr.split()

  for token in tokenList:
    if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
      postfixList.append(token)
    elif token == "(":
      opStack.push(token)
    elif token == ")":
      topToken = opStack.pop()
      while topToken != "(":
        postfixList.append(topToken)
        topToken = opStack.pop()
    else:
      while (not opStack.isEmpty()) and (prec[opStack.peek()] >= prec[token]):
        postfixList.append(opStack.pop())
      opStack.push(token)
          
  while not opStack.isEmpty():
    postfixList.append(opStack.pop())
  return " ".join(postfixList)

# POSTFIX EVAL
def postfixEval(postfixExpr):
  operandStack = Stack()
  tokenList = postfixExpr.split()

  for token in tokenList:
    if token.isnumeric():
      operandStack.push(token)
    else: # is non numeric
      first = float(operandStack.pop())
      second = float(operandStack.pop())
      operandStack.push(doMath(token, second, first))

  return operandStack.pop()

def doMath(op, second, first):
  if op == "*":
    return second * first
  elif op == "/":
    return second / first
  elif op == "+":
    return second + first
  else:
    return second - first

# print(infixToPostfix("( A * B + C ) * D"))
print(infixToPostfix("A * B ** ( C - D )"))
# print(postfixEval('10 3 * 2 1 + +'))
