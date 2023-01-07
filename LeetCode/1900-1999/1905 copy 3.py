'''
5799. Number of Wonderful Substrings

2021.06.20 Sunday 20:23
'''
from typing import List
from collections import Counter


word = "aba"
word = "aabb"
# word = "he"
n = len(word)

ans = 0
for l in range(n):
    if l == 0:
        ans += n
    else:
        for i in range(n-l):
            if i == 0:
                c = Counter(word[i:i+l+1])
                odd_a_count = sum([c[k] % 2 == 1  for k in c])
            else:
                if c[word[i-1]] % 2 == 1:
                    odd_a_count -= 1
                else:
                    odd_a_count += 1
                c[word[i-1]] -= 1

                if c[word[i+l]] % 2 == 0:
                    odd_a_count += 1
                else:
                    odd_a_count -= 1
                c[word[i+l]] += 1

            if odd_a_count <= 1:
                ans += 1

print(ans)
