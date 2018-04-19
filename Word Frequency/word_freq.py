import re
import string
import operator

frequency = {}
input_file = open('input.txt', 'r')
text_string = input_file.read().lower()
match_pattern = re.findall(r'\b[a-z]{4,25}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1

sorted_frequency = sorted(frequency.items(), key=lambda x: (-x[1],x[0]))

output_file = open('output.txt', 'w')

for word, count in sorted_frequency:
    output_file.write(str(count))
    output_file.write(' ')
    output_file.write(word)
    output_file.write('\n')
