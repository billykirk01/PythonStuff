from bs4 import BeautifulSoup
import os

with open('input.html', 'r') as rf:
    text_string = rf.read()

soup = BeautifulSoup(text_string, 'html.parser')

with open('output.txt', 'w') as wf:
    wf.write(os.linesep.join([s for s in soup.get_text().splitlines() if s]))

