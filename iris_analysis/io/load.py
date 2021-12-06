import csv
from collections import defaultdict

def loader(load_path):
    data = defaultdict(list)

    with open(load_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader: 
            for (k,v) in row.items(): 
                if k != 'variety':
                    data[k].append(v)

    return data