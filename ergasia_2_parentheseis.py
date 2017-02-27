def Elegxos(x):
  stack = []
  push, pop = "(", ")"
  for p in x :
    if p in push :
      stack.append(p)
    elif p in pop :
      if not len(stack) :
        return False
      else :
        stackTop = stack.pop()
        balancing = push[pop.index(p)]
        if stackTop != balancing :
          return False
  return not len(stack)
  
akolouthia= str(raw_input("Dwse mou mia akolouthia parenthesewn: "))
print Elegxos(akolouthia)
