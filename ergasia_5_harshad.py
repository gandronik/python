def athroisma_psifiwn(x):
  athr_psif=0
  athroismata = list(str(x))
  for athr in athroismata:
        athr_psif += int(athr)
  return athr_psif
  		
def harshad(x):
    return not x % athroisma_psifiwn(x)

harshad_arithmoi=[]  
ginomeno_arithmoi=[]

for x in range(1, 1001):
  if harshad(x) == True:
    harshad_arithmoi.append(x)
    
print "Arithmoi Harshad:\n"
print(harshad_arithmoi)

def ginomeno_psifiwn(x):
	ginomena= list(str(x))
	gin_psif= 1
	for gin in ginomena:
		gin_psif *= int(gin)
	return gin_psif

for x in range (1,1001):
	if ginomeno_psifiwn(x)!=0:
		if x % ginomeno_psifiwn(x) == 0:
			ginomeno_arithmoi.append(x)

print "\nArithmoi pou to ginomeno twn psifiwn tous diairei ton eauto tous:\n"
print (ginomeno_arithmoi)
