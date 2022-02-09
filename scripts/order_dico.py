#!/usr/bin/env python
DICT_PATH = '.github/workflows/personal-dictionary.txt'

with open(DICT_PATH, mode='r') as f:
    file = f.read().split()
    head_limit = 4
    head = file[0:head_limit]
    file_ordered = sorted(file[head_limit:])
    last = file_ordered[-1]

with open(DICT_PATH, mode='w') as f:
    [f.write(h+' ') for h in head]
    f.write('\n')
    [f.write(l+'\n') for l in file_ordered[:-1]]
    f.write(last)
