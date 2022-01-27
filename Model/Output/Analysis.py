"""
    This script analyzes the output from the knoledge commons ABM
-------------------------------------------------------------------------------
created on:
    Thu 27 Jan 2022
-------------------------------------------------------------------------------
last change:
    Thu 27 Jan 2022
-------------------------------------------------------------------------------
notes:
-------------------------------------------------------------------------------
contributors:
    Jose:
        name:       Jose Betancourt
        email:      jose.betancourtvalencia@yale.edu
-------------------------------------------------------------------------------
"""
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Garamond"],
    "font.size": 15,
})


attributes = np.load('Attributes.npy')
membership = np.load('Membership.npy')

# Get the sizes of each group
sz = []
for ar in membership:
    unique, counts = np.unique(ar, return_counts=True)
    dist = np.zeros(4, dtype=int)
    for j, i in enumerate(unique):
        dist[i+1] = counts[j]
    sz.append(dist)
sz = np.array(sz)

t_vals = np.arange(membership.shape[0])
for i in range(4):
    plt.plot(t_vals, sz[:,i], label='Group %s'%(i) if i!=0 else 'Loners')
plt.legend()
plt.xlabel('$t$')
plt.ylabel('Group size')
plt.savefig('GroupSize.png', dpi=600, bbox_inches='tight')
plt.show()

# Get characteristics of each group
char_x = []
char_y = []
char_z = []
for ar in membership:
    means_x = []
    means_y = []
    means_z = []
    for i in range(4):
        aux = attributes[np.where(ar==i-1)]
        means_x.append(np.mean(aux[:,0]) if len(aux)>0 else np.nan)
        means_y.append(np.mean(aux[:,1]) if len(aux)>0 else np.nan)
        means_z.append(np.mean(aux[:,2]) if len(aux)>0 else np.nan)
    char_x.append(means_x)
    char_y.append(means_y)
    char_z.append(means_z)
char_x = np.array(char_x)
char_y = np.array(char_y)
char_z = np.array(char_z)

for i in range(4):
    plt.plot(t_vals, char_x[:,i], label='Group %s'%(i) if i!=0 else 'Loners')
plt.legend()
plt.xlabel('$t$')
plt.ylabel('Avg. Interest')
plt.savefig('AvgInt.png', dpi=600, bbox_inches='tight')
plt.show()


for i in range(4):
    plt.plot(t_vals, char_y[:,i], label='Group %s'%(i) if i!=0 else 'Loners')
plt.legend()
plt.xlabel('$t$')
plt.ylabel('Avg. Field')
plt.savefig('AvgField.png', dpi=600, bbox_inches='tight')
plt.show()


for i in range(4):
    plt.plot(t_vals, char_z[:,i], label='Group %s'%(i) if i!=0 else 'Loners')
plt.legend()
plt.xlabel('$t$')
plt.ylabel('Avg. Skill')
plt.savefig('AvgSkill.png', dpi=600, bbox_inches='tight')
plt.show()