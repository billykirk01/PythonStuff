import re
import string
import operator

frequency = {}

with open('input.txt', 'r') as rf:
    text_string = rf.read().lower()

match_pattern = re.findall(r'\b[a-z]{4,25}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1

sorted_frequency = sorted(frequency.items(), key=lambda x: (-x[1],x[0]))

with open('output.txt', 'w') as wf:
    for word, count in sorted_frequency:
        wf.write(str(count))
        wf.write(' ')
        wf.write(word)
        wf.write('\n')
