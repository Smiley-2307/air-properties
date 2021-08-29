import cantera as ct

#air mixture
gas = ct.Solution('air.yaml')

print('T = ', gas.T)

gas()
  
#print out the values of cp , cv and gamma of air  
print('Cp = ',gas.cp)
print('Cv = ',gas.cv)
print('gamma = ',gas.cp/gas.cv)




