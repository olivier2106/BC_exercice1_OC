entrees='1941e985075825e09de53b08cdd346bb67075ef0ce5c94f98853292d4bf94c10d010000006b483045022100ab44ef425e6d85c03cf301bc16465e3176b55bba9727706819eaf07cf84cf52d02203f7dc7ae9ab36bead14dd3c83c8c030bf8ce596e692021b66441b39b4b35e64e012102f63ae3eba460a8ed1be568b0c9a6c947abe9f079bcf861a7fdb2fd577ed48a81Feffffff'
def decompose(entree):
	l=list(entree)
	hash=l[0:128]
	hash=''.join(hash)
	index=l[128:144]
	index=''.join(index)
	print(len(l))
	n=len(l)-4
	print(n)
	scriptsig=l[144:n]
	scriptsig=''.join(scriptsig)
	sequence=l[n:len(l)]
	sequence=''.join(sequence)
	print("hash:",hash)
	print("index:",index)
	print("scriptsig:",scriptsig)
	print("seqence:",sequence)