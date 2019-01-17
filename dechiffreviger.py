L=['vpk','cjw','nng','stc','gf']
def dechiffre(code,cle):
	dechif=""
	for s in code:
		c=[]
		for i in range(len(s)):
			c.append(chr((ord(s[i])-ord(cle[i])+97)%123))#critére pour que le decalage soit dans l'alphabet
		decode=''.join(c)
		dechif+=decode
	return(dechif)