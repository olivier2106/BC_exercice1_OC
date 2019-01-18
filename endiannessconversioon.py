def conversion(mot):
  bigendian=hex(mot)
  b=list(bigendian)
  s=b[0:2]
  t=b[2:len(b)]
  t.reverse()
  d=s+t
  littlendian=''.join(d)
  return({"bigendian":bigendian,"littlendian":littlendian})
  
  
