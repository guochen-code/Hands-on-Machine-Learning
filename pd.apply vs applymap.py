# (1) apply works on a row/column basis of a dataframe 
# (2) applymap works element-wise on a dataframe
# (3) map works element-wise on a series / dataframe has no attribute map*******

def toInch(val):
  try:
    return float(val)/2.54
  except:
    return val
  
  df.applymap(toInch)

##################### apply works on a row/column basis #######################
def den(rb, rf=1, rm=2.71):
    return (rm-rb)/(rm-rf)
dfl['Den_por'] = dfl['RHOB'].apply(den, rf=1, rm=2.71)


##################### lambda #####################
x=lambda a,b: (a+b)/2
df_dropped['PHIT']=x(df_dropped['NPHI'],df_dropped['Den_por'])
