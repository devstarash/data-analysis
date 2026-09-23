import re
FILE_NAME = 'a.txt'
verb_adverb_pairs = []
with open(FILE_NAME, mode='r') as file:
    for line in file:
        pattern = r'(?:^\S+(?:ть|шь|л|ует)\s+\S+[оуеия]$|^\S+[оуеия]\s+\S+(?:ть|шь|л|ует)$)'
        catched = re.findall(pattern, line)
        if catched:
            verb_adverb_pairs.extend(catched)
print(f'Количество пар : {len(verb_adverb_pairs)}')
print(verb_adverb_pairs)