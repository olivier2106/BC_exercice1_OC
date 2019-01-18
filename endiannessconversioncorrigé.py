def conversion(mot):
	hx=hex(mot)
	bigendian='0x0'+hx[2:len(hx)]
	b=list(bigendian)
	s=b[0:2]
	t=b[2:len(b)]
	c=[]
	n=len(t)
	for i in range(0,n+1,2):
		bin=''.join(t[i:i+2])
		c.append(bin)
	c.reverse()
	d=s+c
	littlendian=''.join(d)
	return({"bigendian":bigendian,"littlendian":littlendian})
  
  
