#methode meilleur pourboire avec  toutes les combinaisons possible
oct=[2000,6000,800,700,1200,1000,1300,600]
#liste des octets

pourb=[13000,9000,2000,1500,3500,2800,5000,1500]
#liste des pourboires correspondant
def combinpourboir(seq,pbl,maxs):  
#fonction qui calcule la meilleur performnce etant donnés
#les listes d'octets et pourboires et  la taille max
	p = []                           
	i, imax = 0, 2**len(seq)-1
	maxpb=0
#determination des meilleurs combinaisons
	while i<=imax:
		s = []
		pb=0
		j, jmax = 0, len(seq)-1
		while j<=jmax:
			if (i>>j)&1==1:
				s.append(seq[j])
				pb+=pbl[j]
			j+=1
		if(sum(s)<=maxs) and (pb > maxpb):
			maxpb=pb
			p=s 
		i+= 1 
	return (p,maxpb,sum(p))
#appel de la fonction meilleur cobinaison pour une taille  max de 6000 octets
combinpourboir(oct,pourb,6000)