import numpy as np

age = np.loadtxt("participants.tsv", skiprows=1, usecols=[1], delimiter='\t')

mean_age = sum(age)/len(age)

np.savetxt("demeaned_age.txt", age-mean_age)

print("done!")


assert mean_age < 100
assert mean_age > 10 
