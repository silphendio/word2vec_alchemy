#!/usr/bin/python3
import json

with open("nounlist.txt") as f:
    nouns = {line.strip() for line in f.readlines()}

embeddings = {}


with open("glove.6B.300d.txt") as f:
    lines = f.readlines()
    for line in lines:
        values = line.strip().split()
        noun = values[0]

        if noun in nouns:
            embeddings[noun] = [float(v) for v in values[1:]]

with open('noun_embeddings.json', 'w') as f:
    json.dump(embeddings, f)
