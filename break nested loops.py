(1) for - else

for i,j in enumerate(m):
  for s,k in enumerate(n):
    if value < 0:
      print('found negative element')
      break
  else: # no break -- else block only executed when there is no break for the inner loop
    continue
  break

# you can use this pattern again and again for nested loops
else:
  continue
break

---------------------------------------------------------------------------------------------

(2) exception for flow control

class FoundElement(Exception):
  pass

for i,j in enumerate(m):
  try:
    for s,k in enumerate(n):
      if value < 0:
        print('found negative element')
        raise FoundElement
  except FoundElement:
    break

# works for multiple levels of nested for oops. you just raise from the innermost and catch
# inside the outermost for loop
# no need to worry about catch it in the intermediate for loops

modified version - use built-in exception
for i,j in enumerate(m):
  try:
    for s,k in enumerate(n):
      if value < 0:
        print('found negative element')
        raise StopIteration
  except StopIteration:
    break
---------------------------------------------------------------------------------------------

(3) function + return

def find_negative(matrix):
  for i,j in enumerate(m):
    for s,k in enumerate(n):
      if value < 0:
        return i, s , k
  return (None,)*3

i, s, k = find_negatiev(m)
if i is not None:
  print('found negative element')
