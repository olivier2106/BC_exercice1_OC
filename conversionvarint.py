def conversion(mot):
#conversion en he hexadecimal
	hx=hex(mot)
#on complete par des zeros si c'est pas paire
	if (len(hx)%2==0):
		debut='0x'
	else:
		debut='0x0'
	bigendian=debut+hx[2:len(hx)]
#trouver le little on separe d'abord le ox du reste puis on reverse les paquet de deux chiffre
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
	octet=[]
	zero=[]
#varint ici  inferieur à 253 on garde le bigendian sinon  on insere l'inndicateur  du nombre d'octets
	if mot<253:
		varint=bigendian
	else:
		zer= n%4    #calcul du nobre d'octets et des zeros pour completer
		f='0'*zer
		zero.append(f)
		if ((n+zer)==4):
			octet.append('fd')
		if((n+zer)==8):
			octet.append('fe')
		if ((n+zer)==16):
			octet.append('ff')
		print(zero)
		varint=s+octet+c+zero 
		varint=''.join(varint)
	return({"bigendian":bigendian,"littlendian":littlendian,"varint":varint})
  
  
