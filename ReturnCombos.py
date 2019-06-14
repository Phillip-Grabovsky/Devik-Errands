#-----------Author: Phillip Grabovsky------------
#File: ReturnCombos
#Desc: takes in M, a number of sites. Generates
#   a complete list of every all electron spins
#   in all M sites. Electron spins in this
#   program can be 0, up, down, or 2. Also returns
#   N and S, N is the total particle number, S is
#   total spin. This likely has some quantum
#   meaning, but it's just a computational errand
#   for a microscopically inclined friend of mine.

M = 4
spins = [0,1,-1,2]
numSpins = len(spins)
combos = []
for i in range(numSpins**M):
    combos.append([])

for order in range(M):
    numToAdd = numSpins**order
    index = 0
    while index < len(combos):
        for spin in spins:
            for i in range(numToAdd):
                combos[index].append(spin)
                index+=1

print(combos)
