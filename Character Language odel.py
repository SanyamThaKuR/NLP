import torch
import matplotlib.pyplot as plt

file = 'names.txt'
words = open(file, 'r').read().splitlines()
N = torch.zeros((27, 27), dtype=torch.int32)
individual_characters = sorted(list(set("".join(words))))
s_to_i = {s: i + 1 for i, s in enumerate(individual_characters)}
s_to_i['.'] = 0
i_to_s = {i: s for s, i in s_to_i.items()}

for word in words:
    character = ['.'] + list(word) + ['.']
    for n1, n2 in zip(character, character[1:]):
        iX1 = s_to_i[n1]
        iX2 = s_to_i[n2]
        N[iX1,iX2] += 1

plt.figure(figsize=(16, 16))
plt.imshow(N, cmap='Blues_r')
for i in range(27):
    for j in range(27):
        chstr = i_to_s[i] + i_to_s[j]
        plt.text(j, i, chstr, ha="center", va="bottom", color='gray')
        plt.text(j, i, N[i, j].item(), ha="center", va="top", color='gray')
plt.axis('off')
plt.show()
