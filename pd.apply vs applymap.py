# (1) apply works on a row/column basis of a dataframe 
# (2) applymap works element-wise on a dataframe
# (3) map works element-wise on a series / dataframe has no attribute map*******

def toInch(val):
  try:
    return float(val)/2.54
  except:
    return val
  
  df.applymap(toInch)
