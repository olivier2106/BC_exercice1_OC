def chiffrecesare(chaine,n):
	c=[]
	for i in range(len(chaine)):
		c.append(chr((ord(chaine[i])+int(n))%123))#critére pour que le decalage ne soit un autre caractére
	cesar=''.join(c)
	return(cesar)