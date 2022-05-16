import numpy as np
import matplotlib.pyplot as plt

l=[]
n=1000

choice=list(range(-180,180))
n_choices=float(len(choice))
min_prob=1/n_choices

# print(n_choices,min_prob)
remaining_prob=1-((min_prob+0.01)*40)

# print(remaining_prob/320.0)
probablities=[remaining_prob/320.0]*int(n_choices)
# print(probablities)
probablities[160:200]=[min_prob+0.01]*40

print(probablities)
for _ in range(n):
    random_num=np.random.choice(choice,p=probablities)
    l.append(random_num)

# print(l)
plt.hist(l,bins=100)
plt.show()

