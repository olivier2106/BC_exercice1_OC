def calculatrice(entr):
	stack=[]
	entrs=entr.split(" ")
	op1=entrs[0]
	op2=entrs[1]
	operation=entrs[2]
	if operation=='+':
		s=int(op1)+int(op2)
	elif operation=='*':
		s=int(op1)*int(op2)
			
	elif operation=='/':
		s=int(op1)/int(op2)
	elif operation=='-':
		s=int(op1)-int(op2)
			
	if len(entrs)==3:
		return(s)
	else:
		return(calculatrice(str(s)+" "+" ".join(entrs[3:len(entrs)])))