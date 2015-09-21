from itertools import permutations
import math

with open('p098_words.txt','r') as f:
    words = f.read().replace('"','').split(',')
    sorted_words = [''.join(sorted(ele)) for ele in words]


anagrams = dict()
size = 5
for word in sorted_words:
    if sorted_words.count(word) > 1 and word not in anagrams and len(word) == size:
            anagrams[word] = [words[i] for i in xrange(len(words)) if sorted_words[i] == word and words[i]!=words[i][::-1]]

for key in anagrams:
    letters = list(sorted(set(''.join(anagrams[key]))))
    for perm in permutations(range(10),len(letters)):
        nums = []
        for word in anagrams[key]:
            num = ''
            for letter in word:
                num += str(perm[letters.index(letter)])
            nums.append(int(num))

        if all([math.sqrt(ele).is_integer() and len(str(ele))==size for ele in nums]):
            print max(sorted(nums))