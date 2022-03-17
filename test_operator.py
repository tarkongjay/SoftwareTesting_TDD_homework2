import math
def oprator(x,y,z):
  if y == 0 :
    if z == 4 or z == 5 :
     return "cannot divide by zero"
    elif z == 1 :
      return x + y
    elif z == 2 :
      return x-y
    elif z == 3 :
      return x*y
    elif z == 4 :
      return x/y
    elif z == 5 :
      return x%y 

  elif z == 1 :
   return x + y
  elif z == 2 :
   return x-y
  elif z == 3 :
   return x*y
  elif z == 4 :
    return x/y
  elif z == 5 :
    return x%y 
 

def test_answer() : 
  assert  oprator(12,3,1) ==  15
  assert  oprator(12,3,2) ==  9
  assert  oprator(12,3,3) ==  36
  assert  oprator(12,3,4) ==  4
  assert  oprator(12,3,5) ==  0
  assert  oprator(4,0,5) ==  "cannot divide by zero"
  assert  oprator(12,0,5) ==  "cannot divide by zero"
  assert  oprator(12,0,1) ==  12
  assert  oprator(12,0,2) ==  12
  assert  oprator(12,0,3) ==  0

  assert  oprator(20,22,1) ==  42
  assert  oprator(29,19,2) ==  10
  assert  oprator(56,9,3) ==  504
  assert  oprator(98,2,4) ==  49
  assert  oprator(50,10,5) ==  0
  assert  oprator(100,0,4) ==  "cannot divide by zero"
  assert  oprator(9,0,5) ==  "cannot divide by zero"
  assert  oprator(58,0,1) ==  58
  assert  oprator(89,0,2) ==  89
  assert  oprator(76,0,3) ==  0
